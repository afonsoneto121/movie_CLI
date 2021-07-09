import src.util.setting as config
import src.util.request as rq
def get_movie(movie):
    result = rq.get_movie_request(movie)
    if len(result):
        for titulo in result:
            print(f'''
Id: {titulo['id']}
Nome: {titulo['nome']}
Descrição: {titulo['descricao']}
            ''')
    else:
        print('Não encontrado')

def get_trending():
    result = rq.get_trending_request()
    if len(result):
        for titulo in result:
            print(f'''
Id: {titulo['id']}
Nome: {titulo['nome']}
Descrição: {titulo['descricao']}
            ''')
    else:
        print('Não encontrado')

def set_token(value):
    configuracoes = {
        'token': value,
        'language':'pt-BR'
    }
    config.new_config(configuracoes)