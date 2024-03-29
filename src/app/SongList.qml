import QtQuick 2.15
import QtQuick.Layouts 1.15
import QtQuick.Controls 2.15

ListView {
    id: list

    anchors.fill: parent
    model: songModel
    interactive: true
    boundsBehavior: Flickable.StopAtBounds 
    clip: true
    delegate: ColumnLayout {
        width: list.width 
        spacing: 0
        Layout.leftMargin: 50

        RowLayout {
            Layout.fillWidth: true
            Layout.leftMargin: 50
            Layout.rightMargin: 50

            Rectangle {
                Layout.fillWidth: true
                Layout.preferredHeight: songName.height + 40
                color: "transparent"

                Text {
                    id: songName
                    text: (index + 1) + ". " + model.name
                    font.family: "Source Sans Pro"
                    font.pointSize: 16
                    font.weight: Font.Normal
                    color: (model.is_playing ? "#71C6FF" : "white")
                    anchors.verticalCenter: parent.verticalCenter
                }

                MouseArea {
                    width: parent.width
                    height: parent.height
                    hoverEnabled: true
                    cursorShape: Qt.PointingHandCursor
                    onClicked: {
                        PlayerView.play(index)
                    }
                }
            }

            Text {
                text: formatDuration(model.duration)
                font.family: "Source Sans Pro"
                font.pointSize: 14
                opacity: 0.4
                font.weight: Font.Normal
                color: "white"
            }
        }

        Rectangle {
            Layout.fillWidth: true
            Layout.preferredHeight: 1 
            Layout.leftMargin: 50
            Layout.rightMargin: 50
            opacity: 0.05
            color: "white"
            visible: (index !== (list.count - 1))
        }
    }

    ScrollBar.vertical: ScrollBar {
        active: true
    }
}
