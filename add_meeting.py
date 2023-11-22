from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QTextEdit, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5 import uic
import sys


class AddMeeting(QMainWindow):
    def __init__(self, date):
        super(AddMeeting, self).__init__()

        # Load The UI File
        uic.loadUi("add_meeting.ui", self)
        # Define Our Widget
        self.dateLabel = self.findChild(QLabel, "dateLabel")
        self.meetingName = self.findChild(QLineEdit, "nameLineEdit")
        self.meetingText = self.findChild(QTextEdit, "textLineEdit")
        self.saveButton = self.findChild(QPushButton, "saveButton")
        # Resize The Window
        self.setFixedSize(456, 411)
        # Change The Icon Of Window
        self.setWindowIcon(QIcon("icon/calendar.png"))

        # The Selected Date
        self.date = date
        self.dateLabel.setText(self.date)

        # Show The App
        self.show()


# Initialize The App
if __name__ == "__main__":
    app = QApplication(sys.argv)
    second_window = AddMeeting("some date")
    second_window.show()
    app.exec_()
