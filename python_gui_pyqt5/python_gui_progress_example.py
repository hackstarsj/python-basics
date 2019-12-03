import  sys
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow,QProgressBar,QPushButton,QVBoxLayout,QHBoxLayout

app=QApplication(sys.argv)

def increaseValue():
    progress.setValue(progress.value()+10)

def decreaseValue():
    progress.setValue(progress.value()-10)

mainWindow=QMainWindow()
mainWindow.setWindowTitle("Progress")
mainWindow.resize(500,400)
widget=QWidget()

vertical_layout=QVBoxLayout()
horizontal_Layout=QHBoxLayout()

increase_progress=QPushButton("Increase")
increase_progress.clicked.connect(increaseValue)

decrease_progress=QPushButton("Decrease")
decrease_progress.clicked.connect(decreaseValue)

horizontal_Layout.addWidget(increase_progress)
horizontal_Layout.addWidget(decrease_progress)

progress=QProgressBar()
progress.setGeometry(30,300,10,10)

vertical_layout.addWidget(progress)
vertical_layout.addLayout(horizontal_Layout)

widget.setLayout(vertical_layout)
mainWindow.setCentralWidget(widget)

mainWindow.show()

sys.exit(app.exec_())