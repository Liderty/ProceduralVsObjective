# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Ui generated: PyQt5 UI code generator 5.14.2
# Authors: Mateusz Liber, Przysław Lyschik
# Data: May 2020
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.Qt import QLabel
import traceback, sys

from pyqtgraph import PlotWidget
import datetime
import random
import OOP


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(880, 430)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 240, 241, 41))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 40, 141, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 10, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.console = QtWidgets.QTextBrowser(self.centralwidget)
        self.console.setGeometry(QtCore.QRect(10, 330, 861, 91))
        self.console.setAutoFillBackground(False)
        self.console.setObjectName("console")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 310, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.plotArea = PlotWidget(self.centralwidget)
        self.plotArea.setGeometry(QtCore.QRect(550, 40, 321, 221))
        self.plotArea.setObjectName("plotArea")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 290, 861, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(550, 10, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(640, 260, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = VerticalLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(525, 30, 21, 190))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setScaledContents(False)
        self.label_7.setWordWrap(False)
        self.label_7.setOpenExternalLinks(False)
        self.label_7.setObjectName("label_7")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(260, 10, 21, 271))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(110, 60, 141, 171))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.additionalOperationsCheckBox0 = QtWidgets.QCheckBox(self.layoutWidget)
        self.additionalOperationsCheckBox0.setEnabled(False)
        self.additionalOperationsCheckBox0.setChecked(True)
        self.additionalOperationsCheckBox0.setObjectName("additionalOperationsCheckBox0")
        self.verticalLayout_3.addWidget(self.additionalOperationsCheckBox0)
        self.additionalOperationsCheckBox1 = QtWidgets.QCheckBox(self.layoutWidget)
        self.additionalOperationsCheckBox1.setObjectName("additionalOperationsCheckBox1")
        self.verticalLayout_3.addWidget(self.additionalOperationsCheckBox1)
        self.additionalOperationsCheckBox2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.additionalOperationsCheckBox2.setObjectName("additionalOperationsCheckBox2")
        self.verticalLayout_3.addWidget(self.additionalOperationsCheckBox2)
        self.additionalOperationsCheckBox3 = QtWidgets.QCheckBox(self.layoutWidget)
        self.additionalOperationsCheckBox3.setObjectName("additionalOperationsCheckBox3")
        self.verticalLayout_3.addWidget(self.additionalOperationsCheckBox3)
        self.additionalOperationsCheckBox4 = QtWidgets.QCheckBox(self.layoutWidget)
        self.additionalOperationsCheckBox4.setObjectName("additionalOperationsCheckBox4")
        self.verticalLayout_3.addWidget(self.additionalOperationsCheckBox4)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 60, 91, 171))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.operationsNumberField0 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.operationsNumberField0.setObjectName("operationsNumberField0")
        self.verticalLayout.addWidget(self.operationsNumberField0)
        self.operationsNumberField0.setMaxLength(9)
        self.operationsNumberField0.setText("15000")
        self.operationsNumberField1 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.operationsNumberField1.setObjectName("operationsNumberField1")
        self.verticalLayout.addWidget(self.operationsNumberField1)
        self.operationsNumberField1.setMaxLength(9)
        self.operationsNumberField1.setText("50000")
        self.operationsNumberField2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.operationsNumberField2.setObjectName("operationsNumberField2")
        self.verticalLayout.addWidget(self.operationsNumberField2)
        self.operationsNumberField2.setMaxLength(9)
        self.operationsNumberField2.setText("150000")
        self.operationsNumberField3 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.operationsNumberField3.setObjectName("operationsNumberField3")
        self.verticalLayout.addWidget(self.operationsNumberField3)
        self.operationsNumberField3.setMaxLength(9)
        self.operationsNumberField3.setText("300000")
        self.operationsNumberField4 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.operationsNumberField4.setObjectName("operationsNumberField4")
        self.operationsNumberField4.setMaxLength(9)
        self.operationsNumberField4.setText("1000000")
        self.verticalLayout.addWidget(self.operationsNumberField4)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(410, 40, 61, 16))
        self.label_10.setObjectName("label_10")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(290, 60, 221, 171))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.timeOutputField0_2 = QtWidgets.QLineEdit(self.widget)
        self.timeOutputField0_2.setEnabled(False)
        self.timeOutputField0_2.setText("")
        self.timeOutputField0_2.setObjectName("timeOutputField0_2")
        self.verticalLayout_4.addWidget(self.timeOutputField0_2)
        self.timeOutputField1_2 = QtWidgets.QLineEdit(self.widget)
        self.timeOutputField1_2.setEnabled(False)
        self.timeOutputField1_2.setObjectName("timeOutputField1_2")
        self.verticalLayout_4.addWidget(self.timeOutputField1_2)
        self.timeOutputField2_2 = QtWidgets.QLineEdit(self.widget)
        self.timeOutputField2_2.setEnabled(False)
        self.timeOutputField2_2.setObjectName("timeOutputField2_2")
        self.verticalLayout_4.addWidget(self.timeOutputField2_2)
        self.timeOutputField3_2 = QtWidgets.QLineEdit(self.widget)
        self.timeOutputField3_2.setEnabled(False)
        self.timeOutputField3_2.setObjectName("timeOutputField3_2")
        self.verticalLayout_4.addWidget(self.timeOutputField3_2)
        self.timeOutputField4_2 = QtWidgets.QLineEdit(self.widget)
        self.timeOutputField4_2.setEnabled(False)
        self.timeOutputField4_2.setObjectName("timeOutputField4_2")
        self.verticalLayout_4.addWidget(self.timeOutputField4_2)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.timeOutputField0 = QtWidgets.QLineEdit(self.widget)
        self.timeOutputField0.setEnabled(False)
        self.timeOutputField0.setText("")
        self.timeOutputField0.setObjectName("timeOutputField0")
        self.verticalLayout_2.addWidget(self.timeOutputField0)
        self.timeOutputField1 = QtWidgets.QLineEdit(self.widget)
        self.timeOutputField1.setEnabled(False)
        self.timeOutputField1.setObjectName("timeOutputField1")
        self.verticalLayout_2.addWidget(self.timeOutputField1)
        self.timeOutputField2 = QtWidgets.QLineEdit(self.widget)
        self.timeOutputField2.setEnabled(False)
        self.timeOutputField2.setObjectName("timeOutputField2")
        self.verticalLayout_2.addWidget(self.timeOutputField2)
        self.timeOutputField3 = QtWidgets.QLineEdit(self.widget)
        self.timeOutputField3.setEnabled(False)
        self.timeOutputField3.setObjectName("timeOutputField3")
        self.verticalLayout_2.addWidget(self.timeOutputField3)
        self.timeOutputField4 = QtWidgets.QLineEdit(self.widget)
        self.timeOutputField4.setEnabled(False)
        self.timeOutputField4.setObjectName("timeOutputField4")
        self.verticalLayout_2.addWidget(self.timeOutputField4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(290, 40, 101, 16))
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.threadpool = QThreadPool()

        self.timeOutputAccessTableObjective = [self.timeOutputField0, self.timeOutputField1, self.timeOutputField2, self.timeOutputField3, self.timeOutputField4]
        self.timeOutputAccessTableProcedural = [self.timeOutputField0_2, self.timeOutputField1_2, self.timeOutputField2_2, self.timeOutputField3_2, self.timeOutputField4_2]

        self.executionTimes = [[0], [0]]

        self.pushButton.clicked.connect(lambda : self.count())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Porównanie czasów operacji wykonanych proceduralnie i obiektowo (M. Liber, P. Lyschik, 2020)"))
        self.pushButton.setText(_translate("MainWindow", "Oblicz"))
        self.label.setText(_translate("MainWindow", "Ilość operacji"))
        self.label_2.setText(_translate("MainWindow", "Wybór operacji do wykonania"))
        self.label_3.setText(_translate("MainWindow", "Czasy wykonania (milisekundy)"))
        self.label_4.setText(_translate("MainWindow", "Konsola wynikowa"))
        self.label_5.setText(_translate("MainWindow", "Wykres czasu działania programu w zależności od podejścia"))
        self.label_6.setText(_translate("MainWindow", "Ilość operacji (tys)"))
        self.label_7.setText(_translate("MainWindow", "Czas wykonania (millis)"))
        self.additionalOperationsCheckBox0.setText(_translate("MainWindow", "Operacji"))
        self.additionalOperationsCheckBox1.setText(_translate("MainWindow", "Operacji dodatkowych"))
        self.additionalOperationsCheckBox2.setText(_translate("MainWindow", "Operacji dodatkowych"))
        self.additionalOperationsCheckBox3.setText(_translate("MainWindow", "Operacji dodatkowych"))
        self.additionalOperationsCheckBox4.setText(_translate("MainWindow", "Operacji dodatkowych"))
        self.label_8.setText(_translate("MainWindow", "Dane wejściowe"))
        self.label_10.setText(_translate("MainWindow", "Obiektowo"))
        self.label_9.setText(_translate("MainWindow", "Proceduralnie"))

    def disableUI(self):
        self.pushButton.setEnabled(False) #TODO: Not working jet

    def enableUI(self):
        self.pushButton.setEnabled(True) #TODO: Not working jet
        
    def clearTimeTables(self):
        for elementProcedural in self.timeOutputAccessTableProcedural:
            elementProcedural.setText("")

        for elementObjective in self.timeOutputAccessTableObjective:
            elementObjective.setText("")


    def clearChart(self):
        self.plotArea.clear()

    def clearTimes(self):
        self.executionTimes = [[0], [0]]

    def clearData(self):
        self.clearTimeTables()
        self.clearChart()
        self.clearTimes()

    def consolePrintLine(self, message):
        currentDateTime = datetime.datetime.now()
        currentDate = currentDateTime.strftime("%d/%m/%Y")
        currentTime = currentDateTime.strftime("%H:%M:%S")
        self.console.append("[" + str(currentDate) + " " + str(currentTime) + "] " + str(message))

    def printExecutionTime(self, operation_type, operations_number, execution_time):
            self.consolePrintLine(str(operation_type)+" wykonano "+str(operations_number)+" operacji w czasie "+str(execution_time)+" milisekund")

    def getData(self):
        dataTable = []
        dataTable.append(0)

        if(len(self.operationsNumberField0.text()) > 0):
            dataTable.append(int(self.operationsNumberField0.text()))

        if(len(self.operationsNumberField1.text()) > 0 and self.additionalOperationsCheckBox1.isChecked()):
            dataTable.append(int(self.operationsNumberField1.text()))

        if(len(self.operationsNumberField2.text()) > 0 and self.additionalOperationsCheckBox2.isChecked()):
            dataTable.append(int(self.operationsNumberField2.text()))

        if(len(self.operationsNumberField3.text()) > 0 and self.additionalOperationsCheckBox3.isChecked()):
            dataTable.append(int(self.operationsNumberField3.text()))

        if(len(self.operationsNumberField4.text()) > 0 and self.additionalOperationsCheckBox4.isChecked()):
            dataTable.append(int(self.operationsNumberField4.text()))

        return dataTable

    def count(self):
        """Counting how long opeartions last"""
        self.disableUI()
        self.clearData()
        self.consolePrintLine("Start opearcji")

        numberOfOperations = self.getData()

        for k in range(1, len(numberOfOperations)):
            self.multithreadExecute(numberOfOperations[k], operationProcedural)
            self.multithreadExecute(numberOfOperations[k], operationObjective)

        self.consolePrintLine("Koniec operacji")
        self.enableUI()

    def updateProcedural(self, result):
        self.executionTimes[0].append(result[0])
        self.printExecutionTime("Proceduralnie", result[1], self.executionTimes[0][-1])
        self.timeOutputAccessTableProcedural[len(self.executionTimes[0]) - 2].setText(str(result[0]))
        self.updatePlots()

    def updateObjective(self, result):
        self.executionTimes[1].append(result[0])
        self.printExecutionTime("Obiektowo", result[1], self.executionTimes[1][-1])
        self.timeOutputAccessTableObjective[len(self.executionTimes[1]) - 2].setText(str(result[0]))
        self.updatePlots()

    def updatePlots(self):
        self.plotArea.plot(self.reduceDataForChartByTousend(self.getData()[:len(self.executionTimes[0])]), self.executionTimes[0], pen=(0, 2), name='Proceduralnie')
        self.plotArea.plot(self.reduceDataForChartByTousend(self.getData()[:len(self.executionTimes[1])]), self.executionTimes[1], pen=(1, 2), name='Obiektowo')

    def reduceDataForChartByTousend(self, data):
        new_data = []
        
        for element in data:
            new_data.append(element/1000)

        return new_data

    def multithreadExecute(self, operations_number, opeartion_type):
        worker = Worker(opeartion_type, operations_number)
        
        if(opeartion_type == operationProcedural):
            worker.signals.result.connect(self.updateProcedural)
        else:
            worker.signals.result.connect(self.updateObjective)

        self.threadpool.start(worker)


def operationProcedural(size):
    import Procedural
    thisProdural = Procedural

    thisProdural.create_account('Foo', 'Bar', 4578220122)
    thisProdural.create_account('Foo', 'Baz', 2347885320)
    thisProdural.create_account('Foo', 'Baz', 1174559614)

    for _ in range(0, size):
        thisProdural.make_deposit(4578220122, 5)
        thisProdural.make_deposit(2347885320, 5)

    for _ in range(0, size):
        thisProdural.make_withdraw(4578220122, 1)
        thisProdural.make_withdraw(2347885320, 1)

    for _ in range(0, size):
        thisProdural.make_transfer(4578220122, 2347885320, 3)

    for _ in range(0, size):
        thisProdural.make_transfer(2347885320, 4578220122, 2)

    thisProdural.clear_accounts()


def operationObjective(size):
    owner_fixtures = [
    OOP.Owner('Foo', 'Bar'),
    OOP.Owner('Foo', 'Baz')
    ]

    account_fixtures = [
    OOP.BankAccount(owner_fixtures[0], 4578220122),
    OOP.BankAccount(owner_fixtures[1], 2347885320),
    OOP.BankAccount(owner_fixtures[1], 1174559614)
    ]

    foo_bar_baz_bank = OOP.Bank()

    foo_bar_baz_bank.add_account(account_fixtures[0])
    foo_bar_baz_bank.add_account(account_fixtures[1])
    foo_bar_baz_bank.add_account(account_fixtures[2])

    for _ in range(0, size):
        foo_bar_baz_bank.make_deposit(foo_bar_baz_bank.get_account(4578220122), 5)
        foo_bar_baz_bank.make_deposit(foo_bar_baz_bank.get_account(2347885320), 5)

    for _ in range(0, size):
        foo_bar_baz_bank.make_withdraw(foo_bar_baz_bank.get_account(4578220122), 1)
        foo_bar_baz_bank.make_withdraw(foo_bar_baz_bank.get_account(2347885320), 1)

    for _ in range(0, size):
        foo_bar_baz_bank.make_transfer(foo_bar_baz_bank.get_account(4578220122), foo_bar_baz_bank.get_account(2347885320), 3)

    for _ in range(0, size):
        foo_bar_baz_bank.make_transfer(foo_bar_baz_bank.get_account(2347885320), foo_bar_baz_bank.get_account(4578220122), 2)


class VerticalLabel(QLabel):
    def __init__(self, *args):
        QLabel.__init__(self, *args)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.translate(0, self.height())
        painter.rotate(-90)
        painter.drawText(0, self.width()/2, self.text())
        painter.end()


class Worker(QRunnable):

    def __init__(self, opeartion_type, operations_number):
        super(Worker, self).__init__()
        self.opeartion_type = opeartion_type
        self.operations_number = operations_number
        self.signals = WorkerSignals()

    def getNumberOfEachOperation(self, number_of_operations):
        return int(number_of_operations/4)

    def microsecondsToMiliseconds(self, time_micro):
        return int(time_micro/1000)

    @pyqtSlot()
    def run(self):
        try:
            each_operation_number = self.getNumberOfEachOperation(self.operations_number)

            startTime = datetime.datetime.now()
            self.opeartion_type(each_operation_number)
            endTime = datetime.datetime.now()

            result = (self.microsecondsToMiliseconds((endTime - startTime).microseconds), self.operations_number)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()


class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
