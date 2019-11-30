import  sys
from PyQt5.QtWidgets import  QWidget,QMainWindow,QVBoxLayout,QHBoxLayout,QLineEdit,QPushButton,QApplication

app=QApplication(sys.argv)

mainWindow=QMainWindow()
mainWindow.setWindowTitle("Horizontal and Vertical Layout")
qwidget=QWidget()

#creating three button and three input box 1st line will be input 2nd line be button and so button and input is horizontal and this two group in vertical

button1=QPushButton("Button 1")
button2=QPushButton("Button 2")
button3=QPushButton("Button 3")

input_1=QLineEdit()
input_2=QLineEdit()
input_3=QLineEdit()

horizontal_layout_1=QHBoxLayout()
horizontal_layout_1.addWidget(input_1)
horizontal_layout_1.addWidget(input_2)
horizontal_layout_1.addWidget(input_3)

horizontal_layout_2=QHBoxLayout()
horizontal_layout_2.addWidget(button1)
horizontal_layout_2.addWidget(button2)
horizontal_layout_2.addWidget(button3)

#adding both horizontal layout into vetical layout
verticalLayout=QVBoxLayout(qwidget)
verticalLayout.addLayout(horizontal_layout_1)
verticalLayout.addLayout(horizontal_layout_2)

qwidget.setLayout(verticalLayout)

mainWindow.setCentralWidget(qwidget)
mainWindow.show()

sys.exit(app.exec_())