import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class qtApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./studyThread/threadApp.ui',self)
        self.setWindowIcon(QIcon('./studyThread/settings.png'))
        self.setWindowTitle('NoThread App v0.1')
        self.pgbTask.setValue(0)

        self.btnStart.clicked.connect(self.btnStartClicked)

    def btnStartClicked(self):
        self.pgbTask.setRange(0, 999999)
        for i in range(0, 1000000):
            self.pgbTask.setValue(i)
            self.txbLog.append(f'노스레드 출력 > {i}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())