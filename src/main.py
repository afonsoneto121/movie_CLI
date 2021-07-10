###################################
# Módulo responsável por formatar os dados recebidos
# pelo terminal e imprimir a resposta
###################################
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

def get_details(id_movie):
    result = rq.get_details_request(id_movie)
    if result:
        str_genges = ', '.join(result['genges'])
        print(f'''
Título Original: {result['original_title']}  
Título: {result['title']}
Gênero:  {str_genges}   
Pagina Inicial: {result['homepage']}    
Média de Votos: {result['vote_average']}  
Data de Lançamento: {result['release_date']}       
''')
    else:
        print('Não encontrado')
