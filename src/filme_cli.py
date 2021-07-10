import argparse
import src.main as main

def init():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', help='Entre com o titulo de um filme ou série',nargs='+',metavar='N' )
    parser.add_argument('-d', help='Ver Top 10 em destaque',action="store_true")
    parser.add_argument('--token', help='Ver Top 10 em destaque')


    args = parser.parse_args()
    if args.f:
        str = ' '.join(args.f)
        main.get_movie(str)
        pass
    elif args.d:
        main.get_trending()
    elif args.token:
        main.set_token(args.token)

