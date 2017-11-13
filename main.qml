import QtQuick 2.2
import QtQuick.Window 2.1
import QtQuick.Controls 1.2
import QtQuick.Dialogs 1.1

Rectangle {
    id:rec_white
    width: 300
    height: 300

    Button {
        signal messageRequired
        objectName: "myButton"
        y : 70
        text : "About"
        onClicked: GenAndSolve.generate_and_solve_Task()

        }


}