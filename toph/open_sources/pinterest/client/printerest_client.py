from toph.common import exceptions, prints, htmlClient, texts, regex
from os import getenv
from json import loads
from types import SimpleNamespace

def getData(username):
    try:
        PINTEREST_URL = getenv("PINTEREST_URL")
        html = htmlClient.getHtml(PINTEREST_URL, username)

        findedId = html.find(id='initial-state')
        removedTag = regex.removeTags(str(findedId))
        convertedObject = convertToObject(removedTag)
        url = PINTEREST_URL + username

        if convertedObject.resourceResponses[0].response.code == 0:
            prints.foundPrint("Pinterest",url)
        else:
            prints.notFoundPrint("Pinterest", username)

    except ValueError:
        exceptions.printException(__name__)

def convertToObject(jsonValue):
    convertedObject = loads(jsonValue, object_hook=lambda d: SimpleNamespace(**d))
    return convertedObject