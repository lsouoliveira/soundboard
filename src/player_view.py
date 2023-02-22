import magic
import mimetypes
import eyed3

from PySide6.QtCore import QObject, Slot, QUrl, Signal, Property
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput

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
        self._player.positionChanged.connect(self._handle_position_changed)

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
        song = self._playlist_model.song(index)

        self._playlist_model.mark_as_playing(index)
        self._player_model.play(song)
        self._play_song(index)

    def pause(self):
        print("Pausing song")

    def stop(self):
        print("Stopping song")

    def next(self):
        print("Playing next song")

    def previous(self):
        print("Playing previous song")

    @Slot(str)
    def add_file(self, file_path: str):
        file_path = file_path.replace("\\", "/")

        mime = magic.from_file(file_path, mime=True)
        file_extension = mimetypes.guess_extension(mime)

        if not file_extension:
            return

        if file_extension[1:] in self.SUPPORTED_AUDIO_FORMATS:
            metadata = eyed3.load(file_path)

            song = Song(
                name=metadata.tag.title or file_path,
                duration=metadata.info.time_secs,
                path=file_path,
            )

            self._playlist_model.add(song)

    @Slot(list)
    def add_files(self, qurls):
        for qurl in qurls:
            self.add_file(qurl.toLocalFile())

    def _play_song(self, index: int):
        song_path = self._playlist_model.path(index)

        self._player.setSource(QUrl(song_path.replace("\\", "/")))
        self._audio_output.setVolume(100)
        self._player.play()

    def _handle_error_changed(self):
        self._toast_model.show("Something went wrong")
    
    def _handle_position_changed(self, position: int):
        self._player_model.position = position / 1000
