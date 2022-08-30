import json
from pprint import pprint

def movie_info(movie, genres):
    movie_detail = {
        '번호': movie.get('id'),
        '제목': movie.get('title'),
        '포스터': movie.get('poster_path'),
        '평점': movie.get('vote_average'),
        '줄거리': movie.get('overview'),
        '장르번호': movie.get('genre_ids')
    },



#genre = open('genres.json', encodint = 'utf-8')
#genre_ids = json.load(genre)

#print(genre_ids)

#    genre_names = {
#        for names in genres_list:
#            print(names.get('id'))


    # 여기에 코드를 작성합니다.  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))



