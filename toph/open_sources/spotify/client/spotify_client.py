from toph.common import exceptions, regex, prints
from toph.config import colors
from os import getenv
from bs4 import BeautifulSoup
from requests import get

def getData(username):
    try:
        SPOTIFY_URL = getenv("SPOTIFY_URL")
        PARAMS = dict(lang='en-US')
        
        url = SPOTIFY_URL + username
        html = get(url, params=PARAMS).text
        parsedHtml = BeautifulSoup(html, "html.parser")
        findedText = findTagText(parsedHtml)
        if findedText:
            if username in findedText:
                prints.foundPrint("Spotify", username, url)               
        else:
            prints.notFoundPrint("Spotify", username)
    except ValueError:
        exceptions.printException(__name__)

def findTagText(parsedHtml):
    try:
        for text in parsedHtml.findAll("h1"):
            text = regex.removeTags(str(text))
            return text
    except ValueError:
        exceptions.printException(__name__)