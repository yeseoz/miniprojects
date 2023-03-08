# NaverApi 클래스 - OpenAPI 인터넷 통해서 데이터를 전달받음
from urllib.request import Request, urlopen
from urllib.parse import quote
import datetime # 현재시간 사용
import json # 결과는 json으로 받기

class NaverApi:
    # 생성자
    def __init__(self) -> None:
        print(f'[{datetime.datetime.now()}] Naver API 생성')

    # Naver API를 호출 (중요!!)
    def get_request_url(self,url):
        # 네이버 API 개인별 인증
        req = Request(url) # 리퀘스트 생성
        req.add_header('X-Naver-Client-Id', 'I8oWObnIX5fGBZjbxbsl') 
        req.add_header('X-Naver-Client-Secret', 'TZWVRkbuFu')

        try:
            res = urlopen(req) # 요청결과 바로 돌아옴
            if res.getcode() == 200: # response OK
                print(f'[{datetime.datetime.now()}] 네이버 API 요청 성공')
                return res.read().decode('utf-8')
            else:
                print(f'[{datetime.datetime.now()}] 네이버 API 요청 실패')
                return None
        except Exception as e:
            print(f'[{datetime.datetime.now()}] 예외 발생 : {e}')
            return None

    # 호출함수
    def get_naver_search(self, node, search, start, display):
        base_url = 'https://openapi.naver.com/v1/search'
        node_url = f'/{node}.json'
        params = f'?query={quote(search)}&start={start}&display={display}'

        url = base_url + node_url + params # 하나의 url로 합치기
        retData = self.get_request_url(url)

        if retData == None:
            return None
        else:
            return json.loads(retData) # json으로 return

    # json 데이터 --> list로 변환
    #def get_post_data(self, post, outputs) -> None:
        title = post['tilte']
        discription = post['discription']
        originallink = post['originallink']
        link = post[['link']]
        
        #'Tue, 07 Mar 2023 17:00:00 +0900'
        pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d, %b, %Y, %H:%M:%S +0900') # 문자로 된걸 날짜 타입으로 바꿈
        pubDate = pDate.strftimme('%Y-%m-%d %H:%M:%S') # 2023-03-07 17:04:00 변경

        # output에 옮기기
        outputs.append({'title':title, 'discription':discription,
                         'originallink':originallink, 'link':link,
                         'pubDate':pubDate})