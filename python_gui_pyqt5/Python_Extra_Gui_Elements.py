import sys
from PyQt5.QtWidgets import QMainWindow,QWidget,QPushButton,QLineEdit,QApplication,QVBoxLayout,QInputDialog,QLabel,QComboBox,QRadioButton,QHBoxLayout,QGroupBox,QCheckBox
from PyQt5.QtGui import QValidator,QIntValidator,QRegExpValidator,QPixmap
from PyQt5.QtCore import QRegExp

def radioCheck(radiobutton):
    if radiobutton.isChecked():
        print("Checked : "+str(radiobutton.color))
    else:
        print("Unchecked : "+str(radiobutton.color))

def radioCheck2(radiobutton):
    if radiobutton.isChecked():
        print("Checked : "+str(radiobutton.country))
    else:
        print("Unchecked : "+str(radiobutton.country))

def getCheckValue(checbox):
    if checbox.isChecked():
        print("Check Box Checked Value : "+str(checbox.text()))
    else:
        print("Check Box UnChecked Value : "+str(checbox.text()))

def showNumberDialog():
    #first Qwidget
    #second Window Title
    #third Label Name
    #fourth Default Value
    #fifth Min Value
    #Sixth Max Value
    #Sevent Step for increase
    data=QInputDialog.getInt(qWidget,"Number Dialog","Number",10,0,100,5)
    if data[1]:
        print("Pressed Ok : Value is "+str(data[0]))
    else:
        print("Pressed Cancel : Value is "+str(data[0]))

def showTextDialog():
    #first Qwidget
    #second Window Title
    #third Label Name
    #fourth QLineEdit.Normal
    #fifth Default Value

    data=QInputDialog.getText(qWidget,"Text Dialog","Text Label",QLineEdit.Normal,"Default Value")
    print(data)
    if data[1]:
        print("Pressed Ok : Value is "+str(data[0]))
    else:
        print("Pressed Cancel : Value is Empty")

def showChoiceDialog():
    #first Param is qWidget
    #second Param is Window Title
    #third Param is Label
    #fourth Param is tuple List
    #fifth Default Selected Item Position
    items=("Red","Blue","Green")
    data=QInputDialog.getItem(qWidget,"Color Dialog","Colors",items,2)
    if data[1]:
        print("Press Ok Value is  : "+str(data[0]))
    else:
        print("Press Cancel Value is  : " + str(data[0]))

def showItem(text):
    print("Input is : "+text)


app=QApplication(sys.argv)

qMainWindow=QMainWindow()
qMainWindow.resize(400,500)
qMainWindow.setWindowTitle("All Gui Element")
qWidget=QWidget()

vertlical_Layout=QVBoxLayout()
#Input Number Dialog Button
button_number_dialog=QPushButton("Show Number Dialog")
button_number_dialog.clicked.connect(showNumberDialog)
vertlical_Layout.addWidget(button_number_dialog)

button_text_dialog=QPushButton("Show Text Dialog")
button_text_dialog.clicked.connect(showTextDialog)
vertlical_Layout.addWidget(button_text_dialog)

button_choice_dialog=QPushButton("Show Choice Dialog")
button_choice_dialog.clicked.connect(showChoiceDialog)
vertlical_Layout.addWidget(button_choice_dialog)

#number input box
numberLabel=QLabel("Number Input")
numberLabel.setGeometry(200,20,10,10)
inputNumber=QLineEdit()
validator=QIntValidator()
inputNumber.setValidator(validator)
vertlical_Layout.addWidget(numberLabel)
vertlical_Layout.addWidget(inputNumber)

#Character Input A-Z Input
stringLabel=QLabel("ABC Input")
vertlical_Layout.addWidget(stringLabel)
letterInput=QLineEdit()
reg=QRegExp("[A-Za-z_]+")
validar_str=QRegExpValidator(reg)
letterInput.setValidator(validar_str)
vertlical_Layout.addWidget(letterInput)

#Drop Down Input
dropDown=QComboBox()
dropDown.addItem("Red")
dropDown.addItem("Blue")
dropDown.addItem("Green")
dropDown.addItem("Yellow")
dropDown.activated[str].connect(showItem)
vertlical_Layout.addWidget(dropDown)

#radio Button Groups
radiobutton1=QRadioButton("Red")
radiobutton1.color="Red"
radiobutton1.toggled.connect(lambda:radioCheck(radiobutton1))

radiobutton2=QRadioButton("Blue")
radiobutton2.color="Blue"
radiobutton2.toggled.connect(lambda:radioCheck(radiobutton2))

radiobutton3=QRadioButton("Green")
radiobutton3.color="Green"
radiobutton3.toggled.connect(lambda:radioCheck(radiobutton3))

horizonatLayout=QHBoxLayout()
horizonatLayout.addWidget(radiobutton1)
horizonatLayout.addWidget(radiobutton2)
horizonatLayout.addWidget(radiobutton3)
groupBox1=QGroupBox()
groupBox1.setLayout(horizonatLayout)
vertlical_Layout.addWidget(groupBox1)

#radio Button Groups 2
radiobutton4=QRadioButton("India")
radiobutton4.country="India"
radiobutton4.toggled.connect(lambda:radioCheck2(radiobutton4))

radiobutton5=QRadioButton("Africa")
radiobutton5.country="Africa"
radiobutton5.toggled.connect(lambda:radioCheck2(radiobutton5))

radiobutton6=QRadioButton("Australia")
radiobutton6.country="Australia"
radiobutton6.toggled.connect(lambda:radioCheck2(radiobutton6))

horizonatLayout2=QHBoxLayout()
horizonatLayout2.addWidget(radiobutton4)
horizonatLayout2.addWidget(radiobutton5)
horizonatLayout2.addWidget(radiobutton6)
groupBox2=QGroupBox()
groupBox2.setLayout(horizonatLayout2)
vertlical_Layout.addWidget(groupBox2)


#check box
checkbox1=QCheckBox("PHP")
checkbox1.stateChanged.connect(lambda:getCheckValue(checkbox1))
checkbox2=QCheckBox("Python")
checkbox2.stateChanged.connect(lambda:getCheckValue(checkbox2))
checkbox3=QCheckBox("Java")
checkbox3.stateChanged.connect(lambda:getCheckValue(checkbox3))
horizonatLayout3=QHBoxLayout()
horizonatLayout3.addWidget(checkbox1)
horizonatLayout3.addWidget(checkbox2)
horizonatLayout3.addWidget(checkbox3)
vertlical_Layout.addLayout(horizonatLayout3)

#showing image
image_lablel=QLabel()
img_px=QPixmap("../fire.png")
image_lablel.setPixmap(img_px)
image_lablel.resize(200,200)
vertlical_Layout.addWidget(image_lablel)



qWidget.setLayout(vertlical_Layout)
qMainWindow.setCentralWidget(qWidget)
qMainWindow.show()

sys.exit(app.exec_())