import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ApplicationWindow {
    visible: true
    width: 700
    height: 640
    title: "Soundboard"
    color: "#11111111"

    ColumnLayout {
        anchors.fill: parent
        spacing: 0

        Player {
            Layout.fillWidth: true
        }

        Playlist {
            Layout.fillWidth: true
            Layout.fillHeight: true
        }

    }
}
