from PySide6.QtCore import QObject, Qt, Slot, QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput

from models import SongModel


class PlayerController(QObject):
    def __init__(self, songModel: SongModel):
        super().__init__()

        self._song_model = songModel

        audio_output = QAudioOutput()

        audio_output.setVolume(1)

        self._media_player = QMediaPlayer()
        self._media_player.setAudioOutput(audio_output)

    @Slot(int)
    def play(self, index: int):
        if self._song_model.rowCount() - 1 < index:
            return

        self._song_model.mark_as_playing(index)
        self._play_song(index)

    def pause(self):
        print("Pausing song")

    def stop(self):
        print("Stopping song")

    def next(self):
        print("Playing next song")

    def previous(self):
        print("Playing previous song")

    def _play_song(self, index: int):
        song_path = self._song_model.data(
            self._song_model.index(index), Qt.DisplayRole + 3
        )

        self._media_player.setSource(QUrl.fromLocalFile(song_path))
