import sys
from PyQt5.QtWidgets import QWidget,QApplication,QTableWidget,QTableWidgetItem,QVBoxLayout

def getSelectedItemData():
    for currentItem  in tableWidget.selectedItems():
        print("ROw : "+str(currentItem.row())+" Column : "+str(currentItem.column())+" "+currentItem.text())

app=QApplication(sys.argv)

qwidget=QWidget()

qwidget.setWindowTitle("Python GUI Table")
qwidget.resize(300,400)

layout=QVBoxLayout()

tableWidget=QTableWidget()
tableWidget.setColumnCount(3)
tableWidget.setRowCount(4)

#adding item in table
tableWidget.setHorizontalHeaderItem(0,QTableWidgetItem("Name"))
tableWidget.setHorizontalHeaderItem(1,QTableWidgetItem("Age"))
tableWidget.setHorizontalHeaderItem(2,QTableWidgetItem("Work"))
tableWidget.setItem(0,0,QTableWidgetItem("Rahul"))
tableWidget.setItem(0,1,QTableWidgetItem("27"))
tableWidget.setItem(0,2,QTableWidgetItem("Dev"))

tableWidget.setItem(1,0,QTableWidgetItem("Vishal"))
tableWidget.setItem(1,1,QTableWidgetItem("28"))
tableWidget.setItem(1,2,QTableWidgetItem("Dev"))

tableWidget.setItem(2,0,QTableWidgetItem("Aman"))
tableWidget.setItem(2,1,QTableWidgetItem("29"))
tableWidget.setItem(2,2,QTableWidgetItem("Dev"))

tableWidget.setItem(3,0,QTableWidgetItem("Ankit"))
tableWidget.setItem(3,1,QTableWidgetItem("30"))
tableWidget.setItem(3,2,QTableWidgetItem("Dev"))

tableWidget.doubleClicked.connect(getSelectedItemData)
layout.addWidget(tableWidget)
qwidget.setLayout(layout)
qwidget.show()

sys.exit(app.exec_())