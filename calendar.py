from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QCalendarWidget, QLabel, QLineEdit, QTextEdit
from PyQt5 import uic, QtCore
from PyQt5.QtGui import QIcon
from persiantools.jdatetime import JalaliDate
import sys

from add_meeting import AddMeeting


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load The UI File
        uic.loadUi("calendar.ui", self)

        # Define Our Widgets
        self.plusButton = self.findChild(QPushButton, "plusButton")
        self.calendar = self.findChild(QCalendarWidget, "calendarWidget")
        self.nameToDo = self.findChild(QLabel, "nameMeetingLabel")
        self.TextToDo = self.findChild(QLabel, "textMeetingLabel")

        # # Make Gregorian calendar To Jalali Calendar(Remember That)
        # self.calendar.setLocale(QtCore.QLocale.Persian)

        # Click The Button
        self.plusButton.clicked.connect(self.usePlus)

        # Change Icon And Image Icon
        self.setWindowIcon(QIcon("icon/calendar.png"))
        self.plusButton.setIcon(QIcon("icon/plus.png"))
        # Resize The Window
        self.setFixedSize(580, 527)

        # Selected Date
        self.date = ""

        # Show The App
        self.show()

    # Define Function To Use Second Window For Add Meeting
    def usePlus(self):
        self.window = AddMeeting(self.date)
        date_selected = self.calendar.selectedDate()
        self.date = str(date_selected.toString())


# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
