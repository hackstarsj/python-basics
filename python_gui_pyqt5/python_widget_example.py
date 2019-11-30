import sys
from PyQt5.QtWidgets import QApplication,QWidget

#creating window first

#first creating QApplication
app=QApplication(sys.argv)
qwidget=QWidget()
qwidget.setWindowTitle("My First Window")
qwidget.show();
sys.exit(app.exec_())