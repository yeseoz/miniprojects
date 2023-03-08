# QT Designer 디자인 사용
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from NaverApi import *
from urllib.request import urlopen
import webbrowser # 웹브라우저 모듈


class qtApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./studyPyQt/naverApiMovie.ui',self)
        self.setWindowIcon(QIcon('./studyPyQt/newsPaper.png'))

        # 검색 버튼 클릭 시그널 / 슬롯 함수
        self.btnSearch.clicked.connect(self.btnSearchClicked)
        # 텍스트 박스 검색어 입력후 엔터를 피면 처리
        self.txtSearch.returnPressed.connect(self.txtSearchReturned)
        self.tblResult.doubleClicked.connect(self.tblResultDoubleClicked)

    def btnSearchClicked(self):
        search = self.txtSearch.text()

        if search == '':
            QMessageBox.critical(self, '경고', '영화명을 입력하세요!')
            return
        else:
            api = NaverApi() # NaverApi 클래스 객체 생성
            node = 'movie' # movie로 변경하면 영화검색
            display = 100 # 100개만 출력

            result = api.get_naver_search(node, search, 1, display)
            print(result)
            # 테이블 위젯에 출력가능
            items = result['items'] # json결좌 중 items부분만 잘라서 때겠다.   
            #print(len(items))   
            self.makeTable(items) # 테이블위젯에 데이터들을 할당함수      

    # 테이블 위젯에 데이터 표시 -- 네이버 영화 결과에 맞춰 변경
    def makeTable(self, items) -> None:
        self.tblResult.setSelectionMode(QAbstractItemView.SingleSelection) # 단일 선택
        self.tblResult.setColumnCount(7) # 테이블 행을 세주는 것
        self.tblResult.setRowCount(len(items)) # 밑으로 몇개의 행을 만들어 줄것인지
        self.tblResult.setHorizontalHeaderLabels(['영화 제목', '개봉년도', '감독', '배우진', '평점', '링크', '포스터'])
        self.tblResult.setColumnWidth(0, 150)
        self.tblResult.setColumnWidth(1, 60) # 개봉년도
        self.tblResult.setColumnWidth(4, 50) # 개봉년도
        self.tblResult.setEditTriggers(QAbstractItemView.NoEditTriggers) # 컬럼 데이터 수정 금지 못하도록
        


        for i, post in enumerate(items): # 0, 영화 타이틀
            title = self.replaceHtmlTag(post['title'])
            pubDate = post['pubDate']
            director = post['director']
            actor = post['actor']
            userRating = post['userRating']
            link = post['link']
            #image = QImage(requests.get(post['image'], streagm=True))
            # imgData = urlopen(post['image']).read()
            # image = QPixmap()
            # if imgData != None:
            #     image.loadFromData(imgData)
                
            #     imgLabel = QLabel()
            #     imgLabel.setPixmap(image)
            #     imgLabel.setGeometry(0, 0, 60, 100)
            #     imgLabel.resize(60, 100)

            # setItem(행, 열, 넣을데이터)
            #self.tblResult.setItem(i, 0, QTableWidgetItem(str(num)))
            self.tblResult.setItem(i, 0, QTableWidgetItem(title))
            self.tblResult.setItem(i, 1, QTableWidgetItem(pubDate))
            self.tblResult.setItem(i, 2, QTableWidgetItem(director))
            self.tblResult.setItem(i, 3, QTableWidgetItem(actor))
            self.tblResult.setItem(i, 4, QTableWidgetItem(userRating))
            self.tblResult.setItem(i, 5, QTableWidgetItem(link))
            # if imgData != None:
            #     self.tblResult.setItem(i, 6, imgLabel)

    def txtSearchReturned(self):
           self.btnSearchClicked()
            
    def tblResultDoubleClicked(self):
        #row = self.tblResult.currentIndex().row()
        #column = self.tblResult.currentIndex().column()
        #print(row, column)
        selected = self.tblResult.currentRow()
        url = self.tblResult.item(selected, 5).text() # url 링크 컬럼 변경
        webbrowser.open(url) # 뉴스기사 웹사이트 오픈

    def replaceHtmlTag(self, sentence) -> str:
        result = sentence.replace('&lt;', '<') # lesser than 작다 
        result= result.replace('&gt;', '>') # greater than 크다
        result = result.replace('<b>', '') # 화면에 bold를 표시할 방법이 없어서
        result = result.replace('</b>', '')
        result = result.replace('&apos;', "'") # apostopy 홑따옴표
        result = result.replace('&quot;', '"') # quotation mark 쌍따옴표
        # 변환 안된 특수문자가 나타나면 여기 추가
        return result

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())