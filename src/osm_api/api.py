import requests

HOST = 'https://www.openstreetmap.org'
API_VERSION = '0.6'


def get_url(type: str, osm_id: str) -> str:
    return HOST + '/api/' + API_VERSION + '/' + type + '/' + osm_id + ('/full/' if type != 'node' else '/')


def get_object(type: str, osm_id: str) -> requests.models.Response:
    res = requests.get(get_url(type=type, osm_id=osm_id))
    if res.status_code == 200:
        return res
    else:
        raise Exception()
