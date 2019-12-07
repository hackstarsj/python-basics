import sys
import os
import json
from PyQt5.QtWidgets import QMainWindow,QWidget,QLineEdit,QApplication,QVBoxLayout,QTextEdit,QAction,QFileDialog,QInputDialog,QTabWidget,QMenu
from PyQt5.QtGui import QTextCursor

def OpenClick():
    #print("Save")
    openSaveDialog()

def editDoc():
    option=QFileDialog.Options()
    file=QFileDialog.getOpenFileName(widget,"Open Single File","Default File","All Files(*)",options=option)
    fil=file[0]
    data=open(fil,"r")
    finame=os.path.basename(data.name)
    tablayout.setTabText(0,finame)
    linedit.setPlainText(data.read())
    data.close()

def editDocMultiple():
    option=QFileDialog.Options()
    file=QFileDialog.getOpenFileNames(widget,"Open Single File","Default File","All Files(*)",options=option)
    fil=file[0]
    for fi in fil:
        data=open(fi,"r+")
        tab=QWidget()
        layout=QVBoxLayout()
        tab.setLayout(layout)
        tex=QTextEdit()
        layout.addWidget(tex)
        layout.setContentsMargins(0,0,0,0)
        tex.setPlainText(data.read())
        name=os.path.basename(fi)
        tablayout.addTab(tab,name)
    #print(fil)
    # data=open(fil,"r")
    # finame=os.path.basename(data.name)
    # tablayout.setTabText(0,finame)
    # linedit.setPlainText(data.read())
    # data.close()


def initNotePad():
    global file
    if os.path.exists("./config.json"):
        file=open("./config.json","r")
        file_data=file.read()
        file.close()
        return file_data
    else:
        file_data={"size":17}
        file=open("./config.json","w")
        file.write(json.dumps(file_data))
        file.close()
        return file_data



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

def settingFontSize():
    global file_data
    global datasiz
    global file
    data=QInputDialog.getInt(widget,"Font Size","Font Size",datasiz['size'],12,48,1)
    if data[1]:

        text=linedit.toPlainText()
        file1=open("./config.json","w")
        file_data={"size":data[0]}
        file1.write(json.dumps(file_data))
        file1.close()
        datasiz=file_data


        linedit.setPlainText("")
        linedit.setFontPointSize(data[0])
        linedit.setPlainText(text)


global file
app=QApplication(sys.argv)
#screen = app.primaryScreen()
#print('Screen: %s' % screen.name())
#size = screen.size()
#print('Size: %d x %d' % (size.width(), size.height()))
win=QMainWindow()

menu=win.menuBar()

openMenu=menu.addMenu("File")
openAction=QAction("Save")
openAction.triggered.connect(OpenClick)
openMenu.addAction(openAction)

editment=menu.addMenu("Edit")


open2=QMenu("Open M")
openAction4=QAction("Open M")
openAction4.triggered.connect(editDocMultiple)
editment.addMenu(open2)
open2.addAction(openAction4)

open1=QMenu("Open")
openAction2=QAction("Open")
openAction2.triggered.connect(editDoc)
editment.addMenu(open1)
open1.addAction(openAction2)



setting=menu.addMenu("Setting")
openAction3=QAction("Font Size")
openAction3.triggered.connect(settingFontSize)
setting.addAction(openAction3)


#win.resize(size.width(),size.height())
widget=QWidget()
#widget.resize(size.width(),size.height())
linedit=QTextEdit()
#linedit.resize(size.width(),size.height())
#linedit.setMaximumHeight(size.height())
#linedit.setMinimumHeight(size.height())
#linedit.setMinimumWidth(size.width())
#linedit.setMaximumWidth(size.width())
tablayout=QTabWidget()
vertical=QVBoxLayout()
file_data=initNotePad()
#data1=(json.dumps(file_data['size']))
#poi=data1['size']
datasiz=json.loads(file_data)
linedit.setFontPointSize(datasiz['size'])
#vertical.resize(size.width(),size.height())
vertical.addWidget(linedit)
#vertical.addStretch()
vertical.setContentsMargins(0,0,0,0)
# vertical.setSpacing(0)
tab1=QWidget()
tab1.setLayout(vertical)
tablayout.addTab(tab1,"Untitled")


vertical1=QVBoxLayout()
vertical1.setContentsMargins(0,0,0,0)
vertical1.addWidget(tablayout)
widget.setLayout(vertical1)
win.setCentralWidget(widget)
win.show()

print(file_data)
win.showMaximized()
sys.exit(app.exec_())