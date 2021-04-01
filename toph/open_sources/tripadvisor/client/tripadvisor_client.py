from toph.common import exceptions, regex, prints
from toph.config import colors
from os import getenv
from bs4 import BeautifulSoup
from requests import get

def getData(username):
    try:
        TRIPADVISOR_URL = getenv("TRIPADVISOR_URL")
        PARAMS = dict(lang='en-US')
        
        url = TRIPADVISOR_URL + username
        html = get(url, params=PARAMS).text
        parsedHtml = BeautifulSoup(html, "html.parser")
        findedText = findTagText(parsedHtml)

        if "  404 Not Found - Tripadvisor " in findedText:
            prints.notFoundPrint("Tripadvisor", username)
        else:
            prints.foundPrint("Tripadvisor", url)

    except ValueError:
        exceptions.printException(__name__)

def findTagText(parsedHtml):
    try:
        for text in parsedHtml.findAll("title"):
            text = regex.removeTags(str(text))
            return text
    except ValueError:
        exceptions.printException(__name__)