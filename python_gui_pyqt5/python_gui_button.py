import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton

def buttonClick():
    print("Button CLicked")

app=QApplication(sys.argv)
qwidget=QWidget()
qwidget.setWindowTitle("My First Window With Button")

#creating button
button=QPushButton("First Button",qwidget)
button.setToolTip("This Will Display Message When i Take Mouse on Button")

#move button position
button.move(200,100)


#adding click functionality
button.clicked.connect(buttonClick)

qwidget.show()
sys.exit(app.exec_())