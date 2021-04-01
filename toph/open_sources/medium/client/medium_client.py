from toph.common import exceptions, prints, htmlClient, texts
from os import getenv

def getData(username):
    try:
        MEDIUM_URL = getenv("MEDIUM_URL")
        html = htmlClient.getHtml(MEDIUM_URL, username)
        findedText = texts.findTagText(html, "title")
        url = MEDIUM_URL + username

        if len(findedText) > 6:
            prints.foundPrint("Medium", url)
        else:
            prints.notFoundPrint("Medium", username)
    except ValueError:
        exceptions.printException(__name__)