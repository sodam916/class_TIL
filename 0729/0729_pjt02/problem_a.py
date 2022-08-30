import requests

URL = 'https://api.themoviedb.org/3/movie/popular'

params = {
'api_key' : '9da7ae64abaf7f23cd60ddbaebcfb205',
'language' : 'ko-KR'
}

response = requests.get(URL, params=params).json()





def popular_count():

    URL = 'https://api.themoviedb.org/3/movie/popular'

    params = {
    'api_key' : '9da7ae64abaf7f23cd60ddbaebcfb205',
    'language' : 'ko-KR'
    }

    response = requests.get(URL, params=params).json()



    moviedict = response.get('results')
    
    return len(moviedict)

    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
