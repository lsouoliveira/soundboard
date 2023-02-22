from PySide6.QtCore import (
    QAbstractListModel,
    QModelIndex,
    Qt,
    QObject,
    Signal,
    Property,
    QTimer,
)
import dataclasses

from data import Song


class PlayerModel(QObject):
    def __init__(self):
        super().__init__()

        self._is_playing = False
        self._position = 0
        self._duration = 0
        self._title = "No song selected"

    @Signal
    def position_changed(self):
        pass

    @Signal
    def is_playing_changed(self):
        pass

    @Signal
    def song_changed(self):
        pass

    @Signal
    def duration_changed(self):
        pass

    @Signal
    def title_changed(self):
        pass

    @Property(int, notify=position_changed)
    def position(self):
        return self._position

    @position.setter
    def position(self, value: int):
        self._position = value
        self.position_changed.emit()

    @Property(bool, notify=is_playing_changed)
    def is_playing(self):
        return self._is_playing

    @is_playing.setter
    def is_playing(self, value: bool):
        self._is_playing = value
        self.is_playing_changed.emit()

    @Property(int, notify=duration_changed)
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value: int):
        self._duration = value
        self.duration_changed.emit()

    @Property(str, notify=title_changed)
    def title(self):
        return self._title

    @title.setter
    def title(self, value: str):
        self._title = value
        self.title_changed.emit()

    def play(self, song):
        self.position = 0
        self.title = song.name
        self.duration = song.duration
        self.is_playing = True


class PlaylistModel(QAbstractListModel):
    def __init__(self, songs: list[Song] = []):
        super().__init__()
        self._songs = songs

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        return len(self._songs)

    def data(self, index: QModelIndex, role: int = Qt.DisplayRole):
        if not index.isValid():
            return None

        if role == Qt.DisplayRole:
            return self._songs[index.row()].name

        if role == Qt.DisplayRole + 1:
            return self._songs[index.row()].duration

        if role == Qt.DisplayRole + 2:
            return self._songs[index.row()].is_playing

        if role == Qt.DisplayRole + 3:
            return self._songs[index.row()].path

    def song(self, index: int) -> Song:
        song = self._songs[index]

        return dataclasses.replace(song)

    def roleNames(self):
        return {
            Qt.DisplayRole: b"name",
            Qt.DisplayRole + 1: b"duration",
            Qt.DisplayRole + 2: b"is_playing",
            Qt.DisplayRole + 3: b"path",
        }

    def mark_as_playing(self, index: int):
        for i, song in enumerate(self._songs):
            if i == index:
                song.is_playing = True
            else:
                song.is_playing = False

        self.dataChanged.emit(self.index(0), self.index(len(self._songs) - 1))

    def path(self, index: int) -> str:
        return self.data(self.index(index), Qt.DisplayRole + 3)

    def add(self, song: Song):
        self.beginInsertRows(QModelIndex(), len(self._songs), len(self._songs))
        self._songs.append(song)
        self.endInsertRows()


class ToastModel(QObject):
    def __init__(self):
        super().__init__()

        self._message = ""
        self._is_visible = False

        self._timer = QTimer()
        self._timer.timeout.connect(self.hide)
        self._timer.setSingleShot(True)

    @Signal
    def messageChanged(self):
        pass

    @Signal
    def isVisibleChanged(self):
        pass

    @Property(str, notify=messageChanged)
    def message(self):
        return self._message

    @message.setter
    def message(self, message):
        self._message = message
        self.messageChanged.emit()

    @Property(bool, notify=isVisibleChanged)
    def is_visible(self):
        return self._is_visible

    @is_visible.setter
    def is_visible(self, is_visible):
        self._is_visible = is_visible
        self.isVisibleChanged.emit()

    def hide(self):
        self.is_visible = False

    def show(self, message, duration=3000):
        self.message = message
        self.is_visible = True

        self._timer.start(3000)
