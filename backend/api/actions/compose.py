from .. import schemas
import os
from urllib.parse import urlparse
import wget
import pathlib

def add_compose(name):
    try:
    # Opens the JSON and iterate over the content. 
        compose_name = compose.name
        compose_url = compose.url

        compose_path = urlparse(compose_url).path
        ext = os.path.splitext(compose_path)[1]

        if os.path.exists('/config/'+compose_name+"/docker-compose.yml"):
            print('file exists, overwritting')
            os.remove('/config/'+compose_name+"/docker-compose.yml")

        if ext in ('.yml', 'yaml'):
            compose_path = wget.download(compose_url, out='/config/compose/'+compose_name+'/docker-compose.yml')
        else:
            print('Not a valid extension: ' + ext)
            raise

    except (OSError, TypeError, ValueError) as err:
        # Optional handle KeyError here too.
        print('data request failed', err)
        raise

    return get_compose(name=compose.name)

def write_compose(compose):
    print(compose)
    pathlib.Path("config/compose/"+compose.name).mkdir(parents=True)
    f = open('config/compose/'+compose.name+'/docker-compose.yml', "a")
    f.write(compose.content)
    f.close()

    return get_compose(name=compose.name)

def get_compose(name):
    if os.path.isdir("/config/compose/"+name):
        path = '/config/compose'+name+'/docker-compose.yml'
        compose = open(path, 'r')
        response = {'name': name, 'path': path, 'compose': compose}