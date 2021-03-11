from toph.common import exceptions, regex, prints
from toph.config import colors
from os import getenv
from bs4 import BeautifulSoup
from requests import get

def getData(username):
    try:
        FACEBOOK_URL = getenv("FACEBOOK_URL")
        PARAMS = dict(lang='en-US')
        
        url = FACEBOOK_URL + username
        html = get(url, params=PARAMS).text
        parsedHtml = BeautifulSoup(html, "html.parser")
        findedText = findTagText(parsedHtml)
        
        if "No se pudo encontrar la página | Facebook" in findedText:
            prints.notFoundPrint("Facebook", username)
        else:
            prints.foundPrint("Facebook", username, url)

    except ValueError:
        exceptions.printException(__name__)

def findTagText(parsedHtml):
    try:
        for text in parsedHtml.findAll("title"):
            text = regex.removeTags(str(text))
            return text
    except ValueError:
        exceptions.printException(__name__)