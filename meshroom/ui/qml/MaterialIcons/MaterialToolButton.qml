import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.11


/**
 * MaterialToolButton is a standard ToolButton using MaterialIcons font.
 * It also shows up its tooltip when hovered.
 */
ToolButton {
    id: control
    font.family: MaterialIcons.fontFamily
    padding: 4
    font.pointSize: 13
    ToolTip.visible: ToolTip.text && hovered
    ToolTip.delay: 100
    Component.onCompleted:  {
        contentItem.color = Qt.binding(function() { return checked ? palette.highlight : palette.text })
    }
    background: Rectangle {
        color: {
            if(pressed || checked || hovered)
            {
                if(pressed || checked)
                    return Qt.darker(parent.palette.base, 1.3)
                if(hovered)
                    return Qt.darker(parent.palette.base, 0.6)
            }
            return "transparent";
        }

        border.color: checked ? Qt.darker(parent.palette.base, 1.4) : "transparent"
    }
}
