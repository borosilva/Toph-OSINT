from toph.common import exceptions
from os import getenv
from bs4 import BeautifulSoup
from requests import get

def getHtml(url, username):
    try:
        HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
        PARAMS = dict(lang='en-US')
        
        urlComplete = url + username
        html = get(urlComplete, params=PARAMS, headers=HEADERS).text
        parsedHtml = BeautifulSoup(html, "html.parser")
        return parsedHtml
    except ValueError:
        exceptions.printException(__name__)