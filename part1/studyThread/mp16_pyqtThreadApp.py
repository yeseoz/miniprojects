# 스레드사용 앱
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time
MAX = 100000

class BackgroundWorker(QThread): # PyQt5 안에 스레드를 위한 클래스 존재
    procChanged = pyqtSignal(int) # 커스텀 시그널

    def __init__(self, count=0, parent=None) -> None:
        super().__init__()
        self.parent = parent
        self.working = False # 스레드 동작여부
        self.count = count

    def run(self): # thread.start() --> run() 대신 실행
        # self.parent.pgbTask.setRange(0, 100)
        # for i in range(0, 101):
        #     print(f'스레드 출력 > {i}')
        #     self.parent.pgbTask.setValue(i)
        #     self.parent.txbLog.append(f'스레드 출력 > {i}')
        while self.working:
            if self.count <= MAX:
                self.procChanged.emit(self.count) # emit 시그널을 내보낸다.
                self.count += 1 # 값 증가만 // 업무프로세스 동작하는 위치
                time.sleep(0.001) # 세밀하게 주면 GUI 처리를 제대로 못함
            else:
                self.working = False # 멈춤

class qtApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./studyThread/threadApp.ui',self)
        self.setWindowIcon(QIcon('./studyThread/settings.png'))
        self.setWindowTitle('Thread App v0.2')
        self.pgbTask.setValue(0)

        self.btnStart.clicked.connect(self.btnStartClicked)

        # 쓰레드 초기화
        self.worker = BackgroundWorker(parent=self, count=0)
        # 백그라운드 워커에 있는 시그널을 접근 하는 슬롯 함수
        self.worker.procChanged.connect(self.procUpdated)

        self.pgbTask.setRange(0,MAX)

    # @pyqtSlot(int) # pyqt에 들어가는 슬롯함수다
    def procUpdated(self, count):
        self.txbLog.append(f'스레드 출력 > {count}')
        self.pgbTask.setValue(count)
        print(f'스레드 출력 > {count}')

    # @pyqtSlot() # 데코레이션(사실 없어도 동작함)
    def btnStartClicked(self):
       self.worker.start() # 스레드 클래스 run() 실행
       self.worker.working = True
       self.worker.count = 0 


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())