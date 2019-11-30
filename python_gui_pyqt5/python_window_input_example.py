import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QPushButton,QLineEdit

def getTextValue():
    print("You Type : "+inputbox.text())

    #removing value from inputbox
    inputbox.setText("")


app=QApplication(sys.argv)

#creating window
mainwindow=QMainWindow()
mainwindow.resize(500,500)
mainwindow.setWindowTitle("Python Window With Input Text")

#creating inputbox
inputbox=QLineEdit(mainwindow)

#resizing button
inputbox.resize(400,20)

#changing position
inputbox.move(10,50)

#creating button
button=QPushButton("Click this ",mainwindow)
button.resize(400,20)
button.move(10,70)
button.clicked.connect(getTextValue)

mainwindow.show()
sys.exit(app.exec_())