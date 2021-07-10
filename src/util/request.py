###################################
# Módulo responsável pela comunicação direta com a API
# https://developers.themoviedb.org/
###################################

import src.util.setting as setting
import requests

urlAPI = 'https://api.themoviedb.org/3'

def get_movie_request(movie):
    conf = setting.read_config()
    idioma = conf['language']
    tokenAPI = conf['token']
    response = requests.get(f'{urlAPI}/search/movie?api_key={tokenAPI}&query={movie}&language={idioma}')
    if response.status_code == 200:
        dados_movie = response.json()
        list = []
        for titulo in dados_movie['results']:
            list.append( {
                 'id': titulo['id'],
                'nome': titulo['original_title'],
            'descricao': titulo['overview']
            })
        return list
    else:
        print('Não encontrado')

def get_trending_request():
    list = []
    conf = setting.read_config()
    idioma = conf['language']
    tokenAPI = conf['token']
    response = requests.get(f'{urlAPI}/trending/movie/week?api_key={tokenAPI}&language={idioma}')
    if response.status_code != 200:
        print('Não encontrado')
    else:
        dados_movie = response.json()

        i = 0
        while i < 10:
            titulo = dados_movie['results'][i]
            list.append({
                'id': titulo['id'],
                'nome': titulo['original_title'],
                'descricao': titulo['overview']
            })
            i += 1

    return list

def get_details_request(id_movie):
    conf = setting.read_config()
    idioma = conf['language']
    tokenAPI = conf['token']
    response = requests.get(f'{urlAPI}/movie/{id_movie}?api_key={tokenAPI}&language={idioma}')
    if response.status_code != 200:
        print('Não encontrado')
        return {}
    else:
        dados_movie = response.json()
        genres = []
        for value in dados_movie['genres']:
            genres.append(value['name'])
        objMovie = {
            'original_title': dados_movie['original_title'],
            'title': dados_movie['title'],
            'genges': genres,
            'homepage': dados_movie['homepage'],
            'vote_average': dados_movie['vote_average'],
            'release_date': dados_movie['release_date']
        }
        return objMovie



if __name__ == '__main__':
    p = get_movie_request('House of Card')
    print(p)

