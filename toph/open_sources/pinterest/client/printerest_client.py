from toph.common import exceptions, regex, prints
from toph.config import colors
from os import getenv
from bs4 import BeautifulSoup
from requests import get
from json import loads
from types import SimpleNamespace

def getData(username):
    try:
        PINTEREST_URL = getenv("PINTEREST_URL")
        PARAMS = dict(lang='en-US')

        url = PINTEREST_URL + username
        html = get(url, params=PARAMS).text
        parsedHtml = BeautifulSoup(html, "html.parser")
        findedId = parsedHtml.find(id='initial-state')
        removedTag = regex.removeTags(str(findedId))
        convertedObject = convertToObject(removedTag)

        if convertedObject.resourceResponses[0].response.code == 0:
            prints.foundPrint("Pinterest",url)
        else:
            prints.notFoundPrint("Pinterest", username)

    except ValueError:
        exceptions.printException(__name__)

def convertToObject(jsonValue):
    convertedObject = loads(jsonValue, object_hook=lambda d: SimpleNamespace(**d))
    return convertedObject