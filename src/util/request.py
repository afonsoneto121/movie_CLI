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



if __name__ == '__main__':
    p = get_movie_request('House of Card')
    print(p)

