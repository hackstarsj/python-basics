import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QMessageBox

app=QApplication(sys.argv)

qwidget=QWidget()
qwidget.setWindowTitle("My First Dialog Box")

button_reply_from_user=QMessageBox.question(qwidget,"PyQt5 Dialog","Do You Like This Program ?",QMessageBox.Yes | QMessageBox.No,QMessageBox.No)

if button_reply_from_user==QMessageBox.Yes:
    print("Thanks for Liking")
else:
    print("Don't Worry We Do More Better")

#if you don't want to show window
#qwidget.show()

sys.exit(app.exec_())