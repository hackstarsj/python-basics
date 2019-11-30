import sys
from PyQt5.QtWidgets import  QMainWindow,QApplication,QLineEdit,QPushButton,QTabWidget,QVBoxLayout,QWidget

app=QApplication(sys.argv)

mainWindow=QMainWindow()
mainWindow.setWindowTitle("My Tab Program")

qwidget=QWidget()
layout=QVBoxLayout(qwidget)

#creating tabs
tabs=QTabWidget()

#tab items
tab1=QWidget()
tab2=QWidget()

tabs.resize(200,300)
tabs.addTab(tab1,"Tab 1")
tabs.addTab(tab2,"Tab 2")

tablayout=QVBoxLayout(qwidget)
button1=QPushButton("Tab 1 Item")
editBox1=QLineEdit()
tablayout.addWidget(editBox1)
tablayout.addWidget(button1)
tab1.setLayout(tablayout)

tablayout2=QVBoxLayout(qwidget)
button2=QPushButton("Tab 2 Item")
editBox2=QLineEdit()
tablayout2.addWidget(editBox2)
tablayout2.addWidget(button2)
tab2.setLayout(tablayout2)

layout.addWidget(tabs)
qwidget.setLayout(layout)

mainWindow.setCentralWidget(qwidget)
mainWindow.show()

sys.exit(app.exec_())
