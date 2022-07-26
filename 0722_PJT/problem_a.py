import json
from pprint import pprint


def movie_info(movie):
    new_movie = {
        '번호': movie.get('id'),
        '제목': movie.get('title'),
        '포스터': movie.get('poster_path'),
        '평점': movie.get('vote_average'),
        '줄거리': movie.get('overview'),
        '장르번호': movie.get('genre_ids')
    }
    return new_movie

    # 여기에 코드를 작성합니다.    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))
