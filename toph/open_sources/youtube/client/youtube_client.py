from toph.common import exceptions, regex, prints
from toph.config import colors
from os import getenv
from bs4 import BeautifulSoup
from requests import get

def getData(username):
    try:
        YOUTUBE_URL = getenv("YOUTUBE_URL")
        PARAMS = dict(lang='en-US')

        url = YOUTUBE_URL + username
        html = get(url, params=PARAMS).text
        parsedHtml = BeautifulSoup(html, "html.parser")
        findedText = findTagText(parsedHtml)

        if "404 Not Found" in findedText:
            prints.notFoundPrint("YouTube", username)
        else:
            prints.foundPrint("YouTube", url)
    except ValueError:
        exceptions.printException(__name__)

def findTagText(parsedHtml):
    try:
        for text in parsedHtml.findAll("title"):
            text = regex.removeTags(str(text))
            return text
    except ValueError:
        exceptions.printException(__name__)