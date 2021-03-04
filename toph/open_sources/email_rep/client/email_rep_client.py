from toph.common import exceptions
from json import loads
from requests import get
from requests.auth import HTTPBasicAuth
from os import getenv


def getData(email):
    try:
        EMAILREP_URL = getenv("EMAILREP_URL")
        EMAILREP_APIKEY = getenv("EMAILREP_APIKEY")

        url =  EMAILREP_URL + email
        params = dict(key=EMAILREP_APIKEY) 
        JSON = loads(get(url, params=params).text)
        return JSON
    except ValueError:
        exceptions.printException(__name__)