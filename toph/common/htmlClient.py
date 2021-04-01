from toph.common import exceptions
from os import getenv
from bs4 import BeautifulSoup
from requests import get

def getHtml(url, username):
    try:
        PARAMS = dict(lang='en-US')
        
        urlComplete = url + username
        html = get(urlComplete, params=PARAMS).text
        parsedHtml = BeautifulSoup(html, "html.parser")
        return parsedHtml
    except ValueError:
        exceptions.printException(__name__)