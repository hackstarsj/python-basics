import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QPushButton,QHBoxLayout,QFileDialog

def openSaveDialog():
    option=QFileDialog.Options()
    #first param is qwidget
    #second param is Window Title
    #third title is Default File Name
    #fourth param is FileType
    #fifth is options

    #for override native save dialog
    option|=QFileDialog.DontUseNativeDialog

    file=QFileDialog.getSaveFileName(widget,"Save File Window Title","defualt.txt","All Files (*)",options=option)
    print(file[0])

def openFileDialog():
    option=QFileDialog.Options()
    file=QFileDialog.getOpenFileName(widget,"Open Single File","Default File","All Files(*)",options=option)
    print(file[0])

def openMultiFile():
    option=QFileDialog.Options()
    option|=QFileDialog.DontUseNativeDialog
    file=QFileDialog.getOpenFileNames(widget,"Select Multi File","default","All Files (*)",options=option)
    print(file[0])

app=QApplication(sys.argv)

mainWindow=QMainWindow()
widget=QWidget()

button_save=QPushButton("Save Dialog")
button_save.clicked.connect(openSaveDialog)

button_single_file_dialog=QPushButton("Open File")
button_single_file_dialog.clicked.connect(openFileDialog)

button_multi_file=QPushButton("Select Files")
button_multi_file.clicked.connect(openMultiFile)

horizontal_layout=QHBoxLayout()
horizontal_layout.addWidget(button_save)
horizontal_layout.addWidget(button_single_file_dialog)
horizontal_layout.addWidget(button_multi_file)

widget.setLayout(horizontal_layout)
mainWindow.setCentralWidget(widget)
mainWindow.show()

sys.exit(app.exec_())