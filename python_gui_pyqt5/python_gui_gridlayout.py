import sys
from PyQt5.QtWidgets import QApplication,QPushButton,QLineEdit,QWidget,QMainWindow,QGridLayout,QVBoxLayout,QHBoxLayout

app=QApplication(sys.argv)

mainWindow=QMainWindow()
mainWindow.setWindowTitle("Calculator")

qwidget=QWidget()

verticalLayout=QVBoxLayout(qwidget)

horizontalLayout=QHBoxLayout()

editLine=QLineEdit()
horizontalLayout.addWidget(editLine)


gridLayout=QGridLayout()
gridLayout.setVerticalSpacing(0)
gridLayout.setHorizontalSpacing(0)
gridLayout.addWidget(QPushButton("1"),1,0)
gridLayout.addWidget(QPushButton("2"),1,1)
gridLayout.addWidget(QPushButton("3"),1,2)
gridLayout.addWidget(QPushButton("4"),2,0)
gridLayout.addWidget(QPushButton("5"),2,1)
gridLayout.addWidget(QPushButton("6"),2,2)
gridLayout.addWidget(QPushButton("7"),3,0)
gridLayout.addWidget(QPushButton("8"),3,1)
gridLayout.addWidget(QPushButton("9"),3,2)

gridLayout2=QGridLayout()
gridLayout.setVerticalSpacing(0)
gridLayout.setHorizontalSpacing(0)
gridLayout.addWidget(QPushButton("+"),0,0)
gridLayout.addWidget(QPushButton("-"),0,1)
gridLayout.addWidget(QPushButton("/"),0,2)
gridLayout.addWidget(QPushButton("*"),0,3)


verticalLayout.addLayout(horizontalLayout)
verticalLayout.addLayout(gridLayout2)
verticalLayout.addLayout(gridLayout)


qwidget.setLayout(verticalLayout)
mainWindow.setCentralWidget(qwidget)
mainWindow.show()

sys.exit(app.exec_())
