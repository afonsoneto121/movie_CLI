###################################
# Módulo responsável pro receber as solicitações diretas do usuário
###################################


import argparse
import src.main as main

def init():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', help='Entre com o titulo de um filme ou série',nargs='+')
    parser.add_argument('-s', help='Ver Detalhes do filme pelo Id')
    parser.add_argument('-d', help='Ver Top 10 em destaque',action="store_true")
    parser.add_argument('--token', help='Ver Top 10 em destaque')


    args = parser.parse_args()
    if args.f:
        str = ' '.join(args.f)
        main.get_movie(str)
        pass
    elif args.d:
        main.get_trending()
    elif args.s:
        main.get_details(args.s)
    elif args.token:
        main.set_token(args.token)

