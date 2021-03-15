from toph.common import exceptions, regex, prints
from toph.config import colors
from os import getenv
from bs4 import BeautifulSoup
from requests import get

def getData(username):
    try:
        FLICKR_URL = getenv("FLICKR_URL")
        PARAMS = dict(lang='en-US')

        url = FLICKR_URL + username
        html = get(url, params=PARAMS).text
        parsedHtml = BeautifulSoup(html, "html.parser")
        findedText = findTagText(parsedHtml)

        if len(findedText) > 6:
            prints.foundPrint("Flickr", username, url)
        else:
            prints.notFoundPrint("Flickr", username)
    except ValueError:
        exceptions.printException(__name__)

def findTagText(parsedHtml):
    try:
        for text in parsedHtml.findAll("title"):
            text = regex.removeTags(str(text))
            return text
    except ValueError:
        exceptions.printException(__name__)