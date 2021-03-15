from toph.common import exceptions, regex, prints
from toph.config import colors
from os import getenv
from bs4 import BeautifulSoup
from requests import get

def getData(username):
    try:
        # Problem with selenium on mac
        # TODO 
        # TWITTER_URL = getenv("TWITTER_URL")
        # PARAMS = dict(lang='en-US')

        # url = TWITTER_URL + username
        # html = get(url, params=PARAMS).text
        # parsedHtml = BeautifulSoup(html, "html.parser")
        # findedText = findTagText(parsedHtml)
        # print(findedText)
        # if username in findedText:
        #     prints.foundPrint("Twitter", username, url)
        # else:
        #     prints.notFoundPrint("Twitter", username)
        prints.notFoundPrint("Twitter", username)
    except ValueError:
        exceptions.printException(__name__)

def findTagText(parsedHtml):
    try:
        for text in parsedHtml.findAll("title"):
            print(text)
            text = regex.removeTags(str(text))
            return text
    except ValueError:
        exceptions.printException(__name__)