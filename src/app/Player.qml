import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Rectangle {
    height: main.height 
    color: "#1b1b1b"

    ColumnLayout {
        id: main
        width: parent.width
        spacing: 25
        z: 2

        Text {
            Layout.leftMargin: 50
            Layout.rightMargin: 50
            Layout.topMargin: 50
            Layout.fillWidth: true
            text: PlayerView.player_model.title 
            color: "#ffffff"
            font.family: "Source Sans Pro"
            font.weight: Font.DemiBold
            font.pointSize: 32
        }

        ColumnLayout {
            Layout.fillWidth: true
            spacing: 12
            Layout.leftMargin: 50
            Layout.rightMargin: 50

            CustomSlider {
                id: slider
                Layout.fillWidth: true
                from: 0
                to: 1
                value: PlayerView.player_model.position / PlayerView.player_model.duration
            }

            RowLayout {
                Layout.fillWidth: true

                Text {
                    Layout.fillWidth: true
                    text: formatDuration(PlayerView.player_model.position)
                    color: "#ffffff"
                    opacity: 0.4
                    font.family: "Source Sans Pro"
                    font.weight: Font.DemiBold
                    font.pointSize: 14
                }

                Text {
                    text: formatDuration(PlayerView.player_model.duration)
                    color: "#ffffff"
                    opacity: 0.4
                    font.family: "Source Sans Pro"
                    font.weight: Font.DemiBold
                    font.pointSize: 14
                }
            }
        }

        RowLayout {
            Layout.fillWidth: true
            Layout.leftMargin: 50
            Layout.rightMargin: 50
            Layout.bottomMargin: 50

            Item {
                Layout.preferredWidth: 128
            }

            Item {
                Layout.fillWidth: true
            }

            Rectangle {
                Layout.preferredWidth: 72
                Layout.preferredHeight: 72
                color: "white"
                radius: 36

                ColumnLayout {
                    anchors.fill: parent

                    Image {
                        id: icon_default
                        source: "images/play-arrow.png"
                        Layout.preferredWidth: 28
                        Layout.preferredHeight: 28
                        visible: !PlayerView.player_model.is_playing
                        Layout.leftMargin: parent.width / 2 - width * 1 / 3
                        Layout.alignment: Qt.AlignVCenter
                    }

                    Image {
                        id: icon_pressed
                        source: "images/pause.png"
                        Layout.preferredWidth: 28
                        Layout.preferredHeight: 28
                        visible: PlayerView.player_model.is_playing
                        Layout.alignment: Qt.AlignVCenter | Qt.AlignHCenter
                    }
                }

                transform: Scale {
                    id: scale
                }
                
                MouseArea {
                    width: parent.width
                    height: parent.height
                    hoverEnabled: true
                    onClicked: {
                        if(PlayerView.player_model.is_playing) {
                            PlayerView.pause()
                        } else {
                            PlayerView.unpause()
                        }
                    }
                    onPressed: {
                        scale.xScale = 0.9
                        scale.yScale = 0.9
                        scale.origin.x = parent.width / 2 
                        scale.origin.y = parent.height / 2
                    }
                    onReleased: {
                        scale.xScale = 1
                        scale.yScale = 1
                    }
                }
            }

            Item {
                Layout.fillWidth: true
            }

            CustomSlider {
                Layout.preferredWidth: 128
                from: 0
                to: 1
                value: 1

                onValueChanged: {
                    PlayerView.player_model.volume = value
                }
            }
        }

    }
}
