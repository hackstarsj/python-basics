import sys
from PyQt5.QtWidgets import QMainWindow,QWidget,QLineEdit,QApplication,QVBoxLayout,QTextEdit,QAction,QFileDialog

def OpenClick():
    #print("Save")
    openSaveDialog()

def editDoc():
    option=QFileDialog.Options()
    file=QFileDialog.getOpenFileName(widget,"Open Single File","Default File","All Files(*)",options=option)
    fil=file[0]
    data=open(fil,"r")
    linedit.setPlainText(data.read())
    data.close()



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
    file=open(file[0],"w")
    file.write(linedit.toPlainText())
    file.close()

app=QApplication(sys.argv)
screen = app.primaryScreen()
print('Screen: %s' % screen.name())
size = screen.size()
print('Size: %d x %d' % (size.width(), size.height()))
win=QMainWindow()

menu=win.menuBar()

openMenu=menu.addMenu("File")
openAction=QAction("Save")
openAction.triggered.connect(OpenClick)
openMenu.addAction(openAction)
editment=menu.addMenu("Edit")
openAction2=QAction("Open")
openAction2.triggered.connect(editDoc)
editment.addAction(openAction2)


win.resize(size.width(),size.height())
widget=QWidget()
widget.resize(size.width(),size.height())
linedit=QTextEdit()
linedit.resize(size.width(),size.height())
linedit.setMaximumHeight(size.height())
linedit.setMinimumHeight(size.height())
linedit.setMinimumWidth(size.width())
linedit.setMaximumWidth(size.width())
vertical=QVBoxLayout()
linedit.setFontPointSize(17)
#vertical.resize(size.width(),size.height())
vertical.addWidget(linedit)
#vertical.addStretch()
vertical.setContentsMargins(0,0,0,0)
vertical.setSpacing(0)
widget.setLayout(vertical)
win.setCentralWidget(widget)
win.show()

sys.exit(app.exec_())