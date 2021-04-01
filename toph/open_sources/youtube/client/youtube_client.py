from toph.common import exceptions, prints, htmlClient, texts
from os import getenv

def getData(username):
    try:
        YOUTUBE_URL = getenv("YOUTUBE_URL")
        html = htmlClient.getHtml(YOUTUBE_URL, username)
        findedText = texts.findTagText(html, "title")
        url = YOUTUBE_URL + username

        if "404 Not Found" in findedText:
            prints.notFoundPrint("YouTube", username)
        else:
            prints.foundPrint("YouTube", url)
    except ValueError:
        exceptions.printException(__name__)