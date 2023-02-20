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
            Layout.preferredHeight: childrenRect.height
            Layout.topMargin: 50
            Layout.leftMargin: 50
            Layout.rightMargin: 50

            Text {
                text: "PLAYLIST"
                color: "#ffffff"
                font.family: "Source Sans Pro"
                font.weight: Font.Normal
                opacity: 0.4
                font.pointSize: 16
                anchors.verticalCenter: parent.verticalCenter
            }
        }

        Rectangle {
            color: "transparent"
            Layout.fillWidth: true
            Layout.fillHeight: true
            Layout.bottomMargin: 50

            SongList {
                model: songModel
            }
        }
    }
}
