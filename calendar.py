from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QCalendarWidget, QLabel, QTextEdit, QMessageBox
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
        self.jalaliDate = self.findChild(QLabel, "jalaiDate")

        # Clickable Our Needed Widgets
        self.calendar.selectionChanged.connect(self.meetingCheck)
        self.saveButton.clicked.connect(self.saveMeeting)

        # Define Variable For Selected Date
        self.date = ""

        # Show The App
        self.show()

    # Define Function For Checking Meeting for  Selected Date
    def meetingCheck(self):
        selectedDate = self.calendar.selectedDate()
        self.date = str(selectedDate.toString())
        try:
            with open(f"{self.date}.txt", "r") as file:
                file_content = file.read()
                self.textMeeting.setText(file_content)
        except FileNotFoundError:
            self.textMeeting.setText("No Meeting Attached")

        # Convert Gregorian to Jalali
        selectedDateForJalali = selectedDate.toPyDate()
        jalaliDate = JalaliDate.to_jalali(selectedDateForJalali.year,
                                          selectedDateForJalali.month,
                                          selectedDateForJalali.day
                                          )
        self.jalaliDate.setText(jalaliDate.strftime("%Y/%m/%d"))

    # Define Function For Save The Meeting
    def saveMeeting(self):
        try:
            if str(self.textMeeting.toPlainText()) == "No Meeting Attached"\
                    or str(self.textMeeting.toPlainText()) == "":
                self.warningMessage()
            else:
                with open(f"{self.date}.txt", "w") as file:
                    file.write(self.textMeeting.toPlainText())

        except Exception as e:
            print(f"The Error is: {e}")

    # Define Function for Warning Message
    def warningMessage(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Don't empty The Day")
        msg.setWindowTitle("Warning")
        msg.exec_()


# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
