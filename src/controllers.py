from PySide6.QtCore import QObject, Qt, Slot, QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput

from models import SongModel


class PlayerController(QObject):
    def __init__(self, songModel: SongModel):
        super().__init__()

        self.model = songModel
        self._media_player = self.create_player()

    def create_player(self):
        audio_output = QAudioOutput()
        audio_output.setVolume(1)

        player = QMediaPlayer()
        player.setAudioOutput(audio_output)

        return player

    @Slot(int)
    def play(self, index: int):
        self.model.mark_as_playing(index)
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
        song_path = self.model.path(index)

        self._media_player.setSource(QUrl.fromLocalFile(song_path))
