# requests 사용 예시 2

import requests


URL = 'https://api.agify.io'

params = {
    'name': 'michael',
    'country_id': 'KR',
}

response = requests.get(URL, params=params).json()
#유연성을 위해 '?' 뒤에 올 리퀘스트(정보요청)를 딕셔너리 형태로 만들어서 보냄
print(response)
