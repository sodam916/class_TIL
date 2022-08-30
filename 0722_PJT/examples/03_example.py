# open 및 json 모듈 사용예시

import json
from pprint import pprint
#



movie = open('sample.json', encoding='utf-8')
movie_detail = json.load(movie)


#pprint(type(movie_detail))
#type : dict
file = open('new_json', 'w', encoding='utf8')
json.dump(movie_detail, file)


pprint(movie_detail)
#문자열로 들어오는 정보

