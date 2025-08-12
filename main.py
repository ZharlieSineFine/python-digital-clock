# Python PyQt5 Digital Clock from Bro Code Python Tutorial
import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt


class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Digital Clock')
        self.setGeometry(1000, 650, 500, 200)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        self.time_label.setFont(QFont('Arial'))
        self.time_label.setStyleSheet("font-size: 150px;"
                                      "color: rgb(56, 237, 53);"
                                      "background-color: black;")

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.time_label.setText(current_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
