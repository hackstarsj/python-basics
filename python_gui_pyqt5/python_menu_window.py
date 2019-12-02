import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QPushButton,QAction

def EditClick():
    print("Edit Clicked")

def OpenClick():
    print("Open Clicked")

app=QApplication(sys.argv)

mainWindow=QMainWindow()
mainWindow.resize(300,200)

#creating mainmenu
mainMenu=mainWindow.menuBar()

#creating menu Item
fileMenu=mainMenu.addMenu("File")
#adding submenu

openMenu=fileMenu.addMenu("Open")
openAction=QAction("Open File")
openAction.triggered.connect(OpenClick)
openMenu.addAction(openAction)

fileMenu.addMenu("Close")

editMenu=mainMenu.addMenu("Edit")
viewMenu=mainMenu.addMenu("View")
helpMenu=mainMenu.addMenu("Help")

#adding click event on menu item
editAction=QAction("Edit")
editAction.triggered.connect(EditClick)
editMenu.addAction(editAction)

#showing menu
mainWindow.show()

sys.exit(app.exec_())
