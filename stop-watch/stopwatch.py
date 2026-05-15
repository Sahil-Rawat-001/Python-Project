# This is a stopwatch in python using PyQt5 library
import sys #sys helps Python interact with the system
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, Qt

# QTimer library : runs code repeatedly after fixed interval

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        
        # add title and set window size
        self.setWindowTitle("Stopwatch")
        self.resize(400,300)

        # add label to show text on screen
        self.time_label = QLabel(self)

        # setting layout (it is important to center the label)
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        # centering label
        self.time_label.setAlignment(Qt.AlignCenter)

        # setting stylesheet like fontsize and font weight
        self.time_label.setStyleSheet("font-weight: bold;"
                                      "font-size:140px;")
        
        # timer object
        self.timer = QTimer(self)

        self.timer.timeout.connect(self.update_display)
        self.timer.start(1000)

        # store seconds
        self.elapsed_seconds = 0

    def update_display(self):
        self.elapsed_seconds += 1

        seconds = self.elapsed_seconds % 60
        
        # // is floor division
        minutes = (self.elapsed_seconds // 60) % 60

        hours  = self.elapsed_seconds // 3600

        time_text = f"{hours:02}:{minutes:02}:{seconds:02}"


        self.time_label.setText(time_text)


if __name__ == "__main__":
    app = QApplication(sys.argv) # (sys.argv) It stores command line arguments.

    window = Stopwatch()
    window.show()

    sys.exit(app.exec_())
