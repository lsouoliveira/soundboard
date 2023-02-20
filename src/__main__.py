import sys
import os

from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QApplication

from controllers import PlayerController
from models import SongModel
from utils import load_fonts, APP_PATH
from data import Song


def main():
    app = QApplication(sys.argv)

    load_fonts()

    engine = QQmlApplicationEngine()

    # Creating a list of _songs
    songs = [
        Song("Song 1", "3:00", "path/to/song1.mp3"),
        Song("Song 2", "3:00", "path/to/song2.mp3"),
    ]

    # Creating a SongModel instance
    song_model = SongModel(songs)

    # Creating a PlayerController instance
    player_controller = PlayerController(song_model)

    # Creating a context
    context = engine.rootContext()

    # Setting the context properties
    context.setContextProperty("songModel", song_model)
    context.setContextProperty("playerController", player_controller)

    # Loading the QML file
    engine.load(os.path.join(APP_PATH, "main.qml"))

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
