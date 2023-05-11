import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ApplicationWindow {
    visible: true
    width: 700
    height: 640
    title: "Soundboard"
    color: "#00111111"
    flags: Qt.Dialog | Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.WindowMinMaxButtonsHint | Qt.WindowSystemMenuHint

    DropArea {
        anchors.fill: parent

        onDropped: (drop) => {
            PlayerView.add_files(drop.urls)
        }
    }

    Rectangle {
        anchors.fill: parent
        focus: true
        color: "transparent"

        MouseArea {
            anchors.fill: parent

            onClicked: {
                focus = true
            }
        }

        Keys.onPressed: (event) => {
            if(event.key >= Qt.Key_1 && event.key <= Qt.Key_1 + 8) {
                PlayerView.play(event.key - Qt.Key_1)
            }

            if(event.key === Qt.Key_Space) {
                PlayerView.toggle_playback()
            }
        }

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

        Rectangle {
            id: toast
            width: parent.width - 100
            height: 50 
            y: parent.height - height - 25
            x: parent.width / 2 - width / 2
            radius: 10
            color: "#e30909"
            visible: false 
            opacity: 0

            ColumnLayout {
                anchors.fill: parent
                anchors.margins: 10 
                spacing: 0

                Text {
                    id: toastText
                    color: "white"
                    font.pixelSize: 16
                    text: PlayerView.toast_model.message 
                }
            }

            Connections {
                target: PlayerView.toast_model

                function onIsVisibleChanged() {
                    toast.visible = true

                    if(!PlayerView.toast_model.is_visible) {
                        toastAnimation.from = 1
                        toastAnimation.to = 0
                    } else {
                        toastAnimation.from = 0
                        toastAnimation.to = 1
                    }

                    toastAnimation.running = true
                }
            }

            OpacityAnimator {
                id: toastAnimation
                target: toast;
                from: 0;
                to: 1;
                duration: 250
                running: false
                onFinished: {
                    toast.visible = PlayerView.toast_model.is_visible
                }
            }
        }
    }

    function formatDuration(duration) {
        duration = duration / 1000

        const hours = Math.floor(duration / 3600)
        const minutes = Math.floor(duration % 3600 / 60)
        const seconds = Math.floor(duration % 3600 % 60) 
        let formattedDuration = ""

        if (hours > 0) {
            formattedDuration += hours + ":"
        }

        if (minutes < 10) {
            formattedDuration += "0" + minutes + ":"
        } else {
            formattedDuration += minutes + ":"
        }

        if (seconds < 10) {
            formattedDuration += "0" + seconds
        } else {
            formattedDuration += seconds
        }

        return formattedDuration
    }
}