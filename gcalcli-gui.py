#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys
from subprocess import call
from PyQt4.QtCore import pyqtSlot
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QFormLayout, QHBoxLayout, QFrame
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Task import Task

class TaskForm(QtGui.QWidget):

    def __init__(self):
        super(TaskForm, self).__init__()

        self.initUI()

    def initUI(self):
        self.form = QFormLayout()

        self.labelTitle = QtGui.QLabel(self)
        self.labelTitle.setText("Title:")

        self.textboxTitle = QtGui.QLineEdit(self)
        self.textboxTitle.textChanged.connect(self.toggle_ok_button)

        self.form.addRow(self.labelTitle, self.textboxTitle)

        self.labelDate = QtGui.QLabel(self)
        self.labelDate.setText("Date:") 

        self.cal = QtGui.QCalendarWidget(self)
        self.cal.setGridVisible(True)
        self.cal.clicked[QtCore.QDate].connect(self.showDate)
		
        self.form.addRow(self.labelDate, self.cal)

        self.lbl = QtGui.QLabel(self)
        date = self.cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.setAlignment(Qt.AlignCenter)

        self.form.addRow(self.lbl)

        self.labelTime= QtGui.QLabel(self)
        self.labelTime.setText("Time:") 

        self.textboxTime = QtGui.QTimeEdit(self)

        self.form.addRow(self.labelTime, self.textboxTime)

        self.labelLocation= QtGui.QLabel(self)
        self.labelLocation.setText("Location:") 

        self.textboxLocation = QtGui.QLineEdit(self)

        self.form.addRow(self.labelLocation, self.textboxLocation)

        self.labelDescription = QtGui.QLabel(self)
        self.labelDescription.setText("Description:") 

        self.plainTextDesc = QtGui.QPlainTextEdit(self)

        self.form.addRow(self.labelDescription, self.plainTextDesc)

        self.hbox = QHBoxLayout()

        self.labelDuration = QtGui.QLabel(self)
        self.labelDuration.setText("Duration:") 

        self.textboxDuration = QtGui.QLineEdit(self)
        self.textboxDuration.setValidator(QIntValidator(0,100))

        self.hbox.addWidget(self.textboxDuration)

        self.labelReminder = QtGui.QLabel(self)
        self.labelReminder.setText(" Reminder:") 

        self.textboxReminder = QtGui.QLineEdit(self)
        self.textboxReminder.setValidator(QIntValidator(0,100))

        self.hbox.addWidget(self.labelReminder)
        self.hbox.addWidget(self.textboxReminder)

        self.form.addRow(self.labelDuration,self.hbox)

        self.separator = QFrame()
        self.separator.setFrameShape(QFrame.HLine)
        self.separator.setFrameShadow(QFrame.Sunken)
        self.separator.setFixedHeight(20)

        self.form.addWidget(self.separator)

        self.buttons = QHBoxLayout()

        self.btnOk = QtGui.QPushButton('Ok', self)
        self.btnOk.clicked.connect(self.ok_click)
        self.buttons.addWidget(self.btnOk)

        self.btnCancel = QtGui.QPushButton('Cancel', self)
        self.buttons.addWidget(self.btnCancel)

        self.form.addItem(self.buttons)

        self.setGeometry(500, 50, 550, 530)
        self.setWindowTitle('Google calendar task')
        self.setWindowIcon(QtGui.QIcon('calendar.png'))

        self.setLayout(self.form)
        self.show()

    @pyqtSlot()
    def ok_click(self):
        gmail = "vidovic.miroslav.vm@gmail.com"
        title = self.textboxTitle.text()
        time = self.textboxTime.text()
        location = self.textboxLocation.text()
        duration = self.textboxDuration.text()
        reminder = self.textboxReminder.text()
        date = self.lbl.text()
        description = self.plainTextDesc.toPlainText()

        print(title, location, date, time, duration, description, reminder)
        task = Task(gmail, title, location, date, time, duration, description,
                reminder)

        task.add_to_calendar()

        sys.exit()

    def showDate(self, date):
        self.lbl.setText(date.toString("M/dd/yyyy"))

    # TODO: Fix the issue where the ok button is enabled on start
    def toggle_ok_button(self):
        text = self.textboxTitle.text()
        if text:
            self.btnOk.setEnabled(True)
        else:
            self.btnOk.setEnabled(False)

def main():

    app = QtGui.QApplication(sys.argv)
    ex = TaskForm()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
