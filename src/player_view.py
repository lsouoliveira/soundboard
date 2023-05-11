import magic
import mimetypes
from tinytag import TinyTag
import os

from PySide6.QtCore import QObject, Slot, QUrl, Signal, Property
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput, QMediaMetaData

from models import PlaylistModel, ToastModel, PlayerModel
from data import Song


class PlayerView(QObject):
    SUPPORTED_AUDIO_FORMATS = ["mp3", "wav", "ogg", "flac", "m4a", "aac", "wma"]

    def __init__(
        self,
        playlist_model: PlaylistModel,
        toast_model: ToastModel,
        player_model: PlayerModel,
    ):
        super().__init__()

        self._playlist_model = playlist_model
        self._toast_model = toast_model
        self._player_model = player_model

        self._setup_player()

    def _setup_player(self):
        self._audio_output = QAudioOutput()
        self._player = QMediaPlayer()
        self._player.setAudioOutput(self._audio_output)

        self._player.errorChanged.connect(self._handle_error_changed)
        self._player.positionChanged.connect(self._handle_player_position_changed)
        self._player.mediaStatusChanged.connect(self._handle_media_status_changed)
        self._player_model.volume_changed.connect(self._handle_volume_changed)

    @Signal
    def playlist_changed(self):
        pass

    @Signal
    def toast_changed(self):
        pass

    @Signal
    def player_changed(self):
        pass

    @Property(QObject, notify=playlist_changed)
    def playlist_model(self):
        return self._playlist_model

    @Property(QObject, notify=toast_changed)
    def toast_model(self):
        return self._toast_model

    @Property(QObject, notify=player_changed)
    def player_model(self):
        return self._player_model

    @Slot(int)
    def play(self, index: int):
        if index >= self._playlist_model.rowCount():
            return

        song = self._playlist_model.song(index)

        self._playlist_model.mark_as_playing(index)
        self._player_model.play(song.name, song.duration)
        self._play_song(index)

    @Slot()
    def toggle_playback(self):
        if self._player_model.is_playing:
            self._player.pause()
        else:
            self._player.play()

        self._player_model.toggle_playback()

    @Slot(str)
    def add_file(self, file_path: str):
        file_path = file_path.replace("\\", "/")

        mime = magic.from_file(file_path, mime=True)
        file_extension = (
            mimetypes.guess_extension(mime) or os.path.splitext(file_path)[-1]
        )

        if not file_extension:
            return

        file_extension = file_extension.lower()[1:]

        if file_extension in self.SUPPORTED_AUDIO_FORMATS:
            metadata = self._extract_metadata(file_path)

            if not metadata:
                return

            song = Song(
                name=metadata["title"],
                duration=float(metadata["duration"]) * 1000,
                path=file_path,
            )

            self._playlist_model.add(song)

    @Signal
    def position_changed(self):
        pass

    @Property(float, notify=position_changed)
    def position(self):
        return self._player.position()

    @position.setter
    def position(self, value: float):
        self._player.setPosition(int(value))

        self.position_changed.emit()

    @Slot(list)
    def add_files(self, qurls):
        for qurl in qurls:
            self.add_file(qurl.toLocalFile())

    def _play_song(self, index: int):
        song_path = self._playlist_model.path(index)

        self._player.setSource(QUrl(song_path.replace("\\", "/")))
        self._audio_output.setVolume(self._player_model.volume)
        self._player.play()

    def _handle_error_changed(self):
        self._toast_model.show("Something went wrong")

    def _handle_player_position_changed(self, position: int):
        self._player_model.position = position

    def _extract_metadata(self, file_path: str):
        tag = TinyTag.get(file_path)

        return {
            "title": tag.title or os.path.basename(file_path),
            "duration": tag.duration,
        }

    def _handle_media_status_changed(self, media_status):
        if media_status == QMediaPlayer.MediaStatus.EndOfMedia:
            self._player_model.stop()

    def _handle_volume_changed(self):
        self._audio_output.setVolume(self._player_model.volume)
