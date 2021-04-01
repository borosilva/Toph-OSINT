from toph.common import exceptions, prints, htmlClient, texts
from os import getenv

def getData(username):
    try:
        ABOUTME_URL = getenv("ABOUTME_URL")
        
        html = htmlClient.getHtml(ABOUTME_URL, username)
        findedText = texts.findTagText(html, "title")

        url = ABOUTME_URL + username

        if len(findedText) >8:
            prints.foundPrint("About.me", url)
        else:
            prints.notFoundPrint("About.me", username)
    except ValueError:
        exceptions.printException(__name__)