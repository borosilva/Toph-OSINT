from toph.common import exceptions, prints, htmlClient, texts
from os import getenv

def getData(username):
    try:
        FLICKR_URL = getenv("FLICKR_URL")
        html = htmlClient.getHtml(FLICKR_URL, username)
        findedText = texts.findTagText(html, "title")

        url = FLICKR_URL + username

        if len(findedText) > 6:
            prints.foundPrint("Flickr", url)
        else:
            prints.notFoundPrint("Flickr", username)
    except ValueError:
        exceptions.printException(__name__)