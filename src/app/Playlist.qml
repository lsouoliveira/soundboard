import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Rectangle {
    color: "#181818"

    ColumnLayout {
        anchors.fill: parent
        spacing: 10

        Rectangle {
            color: "transparent"
            Layout.fillWidth: true
            Layout.topMargin: 50
            Layout.leftMargin: 50
            Layout.rightMargin: 50
            Layout.preferredHeight: childrenRect.height
            Layout.alignment: Qt.AlignTop

            ColumnLayout {
                spacing: 10
                width: parent.width

                Text {
                    text: "PLAYLIST" 
                    color: "#ffffff"
                    font.family: "Source Sans Pro"
                    font.weight: Font.Normal
                    opacity: 0.4
                    font.pointSize: 16
                    Layout.alignment: Qt.AlignVCenter | Qt.AlignTop
                }

                Text {
                    id: emptyPlaylistText
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignTop
                    font.family: "Source Sans Pro"
                    font.weight: Font.Normal
                    font.pixelSize: 16
                    color: "white"
                    text: "No songs in playlist"
                }
            }
        }

        Rectangle {
            id: songList
            color: "transparent"
            Layout.fillWidth: true
            Layout.fillHeight: true
            Layout.bottomMargin: 50
            visible: false

            SongList {
                model: PlayerView.playlist_model
            }
        }

        Connections {
            target: PlayerView.playlist_model

            function onRowsInserted() {
                emptyPlaylistText.visible = false
                songList.visible = true
            }

            function onRowsRemoved() {
                emptyPlaylistText.visible = true
                songList.visible = false
            }
        }
    }
}
