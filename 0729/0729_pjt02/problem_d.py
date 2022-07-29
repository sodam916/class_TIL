import requests
from pprint import pprint


def recommendation(title):

    URL = 'https://api.themoviedb.org/3/search/movie'

    params = {
    'api_key' : '9da7ae64abaf7f23cd60ddbaebcfb205',
    'language' : 'ko-KR',
    'query' : f'{title}', 
    }

    response = requests.get(URL, params=params).json() #영화목록
    moviedict = response.get('results')
    
    if moviedict == []:
        return None
    
    
        
    movie_id = moviedict[0]['id']
                    
    
    RURL = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations'

    params = {
    'movie_id' : f'{movie_id}',
    'api_key' : '9da7ae64abaf7f23cd60ddbaebcfb205',
    'language' : 'ko-KR',
    }
    

    response_id = requests.get(RURL, params=params).json()

    
    tilist = response_id.get('results')

    
    
    for ti in tilist:
        final_list = []

        final_list.append(ti.get('title'))
    
        print(final_list)

        
        # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
