from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QCalendarWidget, QLabel, QTextEdit
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from persiantools.jdatetime import JalaliDate
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load The UI File
        uic.loadUi("calendar.ui", self)
        # Change Icon And Image Icon
        self.setWindowIcon(QIcon("icon/calendar.png"))
        # Resize The Window
        self.setFixedSize(580, 576)

        # Define Our Widgets
        self.calendar = self.findChild(QCalendarWidget, "calendarWidget")
        self.textMeeting = self.findChild(QTextEdit, "meetingText")
        self.saveButton = self.findChild(QPushButton, "saveButton")

        # Clickable Our Needed Widgets
        self.calendar.selected.connect(self.meetingCheck)
        self.saveButton.clicked.connect(self.saveMeeting)

        # Show The App
        self.show()

    # Define Function For Checking Meeting for  Selected Date
    def meetingCheck(self):
        pass

    # Define Function For Save The Meeting
    def saveMeeting(self):
        pass


# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
