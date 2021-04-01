from toph.common import exceptions, prints, htmlClient, texts
from os import getenv

def getData(username):
    try:
        INSTAGRAM_URL = getenv("INSTAGRAM_URL")
        html = htmlClient.getHtml(INSTAGRAM_URL, username)
        findedText = texts.findTagText(html, "title")
        url = INSTAGRAM_URL + username

        if username in findedText:
            prints.foundPrint("Instagram", url)
        else:
            prints.notFoundPrint("Instagram", username)
    except ValueError:
        exceptions.printException(__name__)