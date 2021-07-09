import json


def new_config(name):
    with open('config.json','w') as fp:
        json.dump(name,fp)

def read_config():
    with open('config.json','r') as fp:
        config = json.load(fp)
    return config

def set_languange(language):
    data ={}
    with open('config.json','r') as fp:
        data = json.load(fp)
        data['language'] = language
    with open('config.json', 'w') as fp:
        json.dump(data,language)