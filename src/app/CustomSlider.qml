import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Slider {
    id: slider
    from: 0
    to: 1

    handle: Rectangle {
        x: slider.leftPadding + slider.visualPosition * (slider.availableWidth - width)
        y: slider.topPadding + slider.availableHeight / 2 - height / 2
        width: 18
        height: 18
        implicitHeight: 18
        implicitWidth: 18
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