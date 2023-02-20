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
            text: "Supir Angkot Goblog"
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

            Slider {
                id: slider
                Layout.fillWidth: true
                padding: 0

                handle: Rectangle {
                    x: slider.leftPadding + slider.visualPosition * (slider.availableWidth - width)
                    y: slider.topPadding + slider.availableHeight / 2 - height / 2
                    width: 18
                    height: 18
                    radius: 9
                    color: "white"
                }

                background: Rectangle {
                    x: 0 
                    y: slider.topPadding + slider.availableHeight / 2 - height / 2
                    implicitWidth: 200
                    implicitHeight: 4
                    width: slider.availableWidth
                    height: implicitHeight
                    radius: 2
                    color: "#424242"

                    Rectangle {
                        width: slider.visualPosition * parent.width
                        height: parent.height
                        color: "#71C6FF"
                        radius: 2
                    }
                }
            }

            RowLayout {
                Layout.fillWidth: true

                Text {
                    Layout.fillWidth: true
                    text: "0:18"
                    color: "#ffffff"
                    opacity: 0.4
                    font.family: "Source Sans Pro"
                    font.weight: Font.DemiBold
                    font.pointSize: 14
                }

                Text {
                    text: "0:29"
                    color: "#ffffff"
                    opacity: 0.4
                    font.family: "Source Sans Pro"
                    font.weight: Font.DemiBold
                    font.pointSize: 14
                }
            }
        }

        RowLayout {
            Layout.leftMargin: 50
            Layout.rightMargin: 50
            Layout.bottomMargin: 50
            Layout.fillWidth: true
            Layout.alignment: Qt.AlignHCenter

            Rectangle {
                Layout.preferredWidth: 72
                Layout.preferredHeight: 72
                color: "white"
                radius: 36

                Image {
                    id: icon_default
                    source: "images/play-arrow.png"
                    width: 28
                    height: 28
                    x: parent.x + parent.width / 2 - (width * (1 / 3))
                    y: parent.y + parent.height / 2 - (height / 2)
                }

                Image {
                    id: icon_pressed
                    source: "images/pause.png"
                    width: 28
                    height: 28
                    visible: false
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.horizontalCenter: parent.horizontalCenter
                }

                transform: Scale {
                    id: scale
                }
                
                MouseArea {
                    width: parent.width
                    height: parent.height
                    hoverEnabled: true
                    onPressed: {
                        scale.xScale = 0.9
                        scale.yScale = 0.9
                        scale.origin.x = parent.width / 2 
                        scale.origin.y = parent.height / 2
                        icon_default.visible = !icon_default.visible
                        icon_pressed.visible = !icon_pressed.visible
                    }
                    onReleased: {
                        scale.xScale = 1
                        scale.yScale = 1
                    }
                }
            }
        }
    }
}
