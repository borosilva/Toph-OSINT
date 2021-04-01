from toph.common import exceptions, regex, prints
from toph.config import colors
from os import getenv
from bs4 import BeautifulSoup
from requests import get

def getData(username):
    try:
        GITHUB_URL = getenv("GITHUB_URL")
        PARAMS = dict(lang='en-US')
        
        url = GITHUB_URL + username
        html = get(url, params=PARAMS).text
        parsedHtml = BeautifulSoup(html, "html.parser")
        if "Not Found" in parsedHtml:
            prints.notFoundPrint("GitHub", username)
        else:
            prints.foundPrint("GitHub", url)
    except ValueError:
        exceptions.printException(__name__)

def findTagText(parsedHtml):
    try:
        for text in parsedHtml.findAll("title"):
            text = regex.removeTags(str(text))
            return text
    except ValueError:
        exceptions.printException(__name__)