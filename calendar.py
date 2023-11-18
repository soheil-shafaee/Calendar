from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QCalendarWidget, QLabel, QLineEdit, QTextEdit
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QIcon
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load The UI File
        uic.loadUi("calendar.ui", self)

        # Define Our Widgets
        self.plusButton = self.findChild(QPushButton, "plusButton")
        self.calendar = self.findChild(QCalendarWidget, "calendarWidget")
        self.toDo = self.findChild(QLabel, "textDoLabel")

        # Change Icon And Image Icon
        self.setWindowIcon(QIcon("icon/calendar.png"))
        self.plusButton.setIcon(QIcon("icon/plus.png"))

        # Show The App
        self.show()


# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
