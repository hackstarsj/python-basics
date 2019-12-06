import sys
from decimal import Decimal
from PyQt5.QtWidgets import QWidget,QMainWindow,QApplication,QPushButton,QLineEdit,QGridLayout

def clickEvent(value):
    neval=input.text()+""+value
    input.setText(neval)

def calculate():
    data=input.text()
    cal=eval(data)
    dec=Decimal(cal)
    cal=round(dec,2)
    input.setText(str(cal))


def backspaceclick():
    data=input.text()
    newdata=data[:-1]
    input.setText(newdata)


app=QApplication(sys.argv)

mainwindow=QMainWindow()
mainwindow.setWindowTitle("Calculator")
widget=QWidget()

gridlayout=QGridLayout()

backspace=QPushButton("<")
one_b=QPushButton("1")
two_b=QPushButton("2")
three_b=QPushButton("3")
four_b=QPushButton("4")
five_b=QPushButton("5")
six_b=QPushButton("6")
seven_b=QPushButton("7")
eight_b=QPushButton("8")
nine_b=QPushButton("9")
zero_b=QPushButton("0")

plus=QPushButton("+")
minus=QPushButton("-")
divide=QPushButton("/")
mul=QPushButton("*")
dots=QPushButton(".")
equal=QPushButton("=")

input=QLineEdit()

gridlayout.addWidget(input,0,0,1,3)
gridlayout.addWidget(backspace,0,3)
gridlayout.addWidget(one_b,1,0)
gridlayout.addWidget(two_b,1,1)
gridlayout.addWidget(three_b,1,2)
gridlayout.addWidget(four_b,2,0)
gridlayout.addWidget(five_b,2,1)
gridlayout.addWidget(six_b,2,2)
gridlayout.addWidget(seven_b,3,0)
gridlayout.addWidget(eight_b,3,1)
gridlayout.addWidget(nine_b,3,2)
gridlayout.addWidget(dots,4,0)
gridlayout.addWidget(zero_b,4,1)
gridlayout.addWidget(equal,4,2)

gridlayout.addWidget(plus,1,3)
gridlayout.addWidget(minus,2,3)
gridlayout.addWidget(divide,3,3)
gridlayout.addWidget(mul,4,3)

gridlayout.setSpacing(0)
gridlayout.setVerticalSpacing(0)
gridlayout.setHorizontalSpacing(0)


one_b.clicked.connect(lambda:clickEvent("1"))
two_b.clicked.connect(lambda:clickEvent("2"))
three_b.clicked.connect(lambda:clickEvent("3"))
four_b.clicked.connect(lambda:clickEvent("4"))
five_b.clicked.connect(lambda:clickEvent("5"))
six_b.clicked.connect(lambda:clickEvent("6"))
seven_b.clicked.connect(lambda:clickEvent("7"))
eight_b.clicked.connect(lambda:clickEvent("8"))
nine_b.clicked.connect(lambda:clickEvent("9"))
zero_b.clicked.connect(lambda:clickEvent("0"))
plus.clicked.connect(lambda:clickEvent("+"))
minus.clicked.connect(lambda:clickEvent("-"))
divide.clicked.connect(lambda:clickEvent("/"))
mul.clicked.connect(lambda:clickEvent("*"))
dots.clicked.connect(lambda:clickEvent("."))
equal.clicked.connect(calculate)
backspace.clicked.connect(backspaceclick)

widget.setLayout(gridlayout)

mainwindow.setCentralWidget(widget)

mainwindow.show()

sys.exit(app.exec_())
