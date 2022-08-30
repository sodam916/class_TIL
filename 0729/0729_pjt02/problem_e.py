from unittest import result
import requests
from pprint import pprint


def credits(title):

    URL = 'https://api.themoviedb.org/3/search/movie'

    params = {
    'api_key' : '9da7ae64abaf7f23cd60ddbaebcfb205',
    'language' : 'ko-KR',
    'query' : f'{title}', 
    }
    
    response = requests.get(URL, params=params).json()
    movie_detail = response.get('results')

    if movie_detail == []:
        return None
    else :

        result = movie_detail[0].get('id')
    

    SURL = f'https://api.themoviedb.org/3/movie/{result}/credits'

    params = {
    'movie_id' : f'{result}',
    'api_key' : '9da7ae64abaf7f23cd60ddbaebcfb205',
    'language' : 'ko-KR',
    }
    

    response_credits = requests.get(SURL, params=params).json()
    cast_detail = response_credits.get('cast')
    castfile = []
    direct_file = []
    for castid in cast_detail:
        if castid.get('cast_id') < 10:
            castfile.append(castid.get('name'))
        elif castid.get('known_for_department') == 'Directing':
            direct_file.append(castid.get('name'))
    
    
    return ('cast : {}, directing : {}'.format(castfile,direct_file))

    
    

    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
