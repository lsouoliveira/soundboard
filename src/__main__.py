# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

from PySide6.QtQml import QQmlApplicationEngine, qmlRegisterType
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QObject, Slot, QUrl, Signal, Property
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput

from player_view import PlayerView
from models import PlaylistModel, ToastModel, PlayerModel
from utils import load_fonts, APP_PATH


def main():
    app = QApplication(sys.argv)

    load_fonts()

    engine = QQmlApplicationEngine()

    playlist_model = PlaylistModel()
    toast_model = ToastModel()
    player_model = PlayerModel()

    player_view = PlayerView(playlist_model, toast_model, player_model)

    qmlRegisterType(PlaylistModel, "PlaylistModel", 1, 0, "PlaylistModel")

    # Creating a context
    context = engine.rootContext()

    # Setting the context properties
    context.setContextProperty("PlayerView", player_view)

    # Loading the QML file
    engine.load(os.path.join(APP_PATH, "main.qml"))

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
