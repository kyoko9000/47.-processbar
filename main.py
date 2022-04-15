import os
import sys
# pip install pyqt5
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.uic.progressBar.setValue(0)
        self.uic.pushButton.clicked.connect(self.program)
        self.uic.pushButton_2.clicked.connect(self.restart_program)
        self.a = 0

    def restart_program(self):
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def program(self):
        timer = QTimer(self)
        timer.timeout.connect(self.process)
        timer.start(100)

    def process(self):
        self.a += 5
        self.uic.progressBar.setValue(self.a)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
