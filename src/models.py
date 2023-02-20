from PySide6.QtCore import QAbstractListModel, QModelIndex, Qt

from data import Song


class SongModel(QAbstractListModel):
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

    def roleNames(self):
        return {
            Qt.DisplayRole: b"name",
            Qt.DisplayRole + 1: b"duration",
            Qt.DisplayRole + 2: b"is_playing",
            Qt.DisplayRole + 2: b"path",
        }

    def mark_as_playing(self, index: int):
        for i, song in enumerate(self._songs):
            if i == index:
                song.is_playing = True
            else:
                song.is_playing = False

        self.dataChanged.emit(self.index(0), self.index(len(self._songs) - 1))
