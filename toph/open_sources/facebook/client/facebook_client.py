from toph.common import exceptions, prints, htmlClient, texts
from os import getenv

def getData(username):
    try:
        FACEBOOK_URL = getenv("FACEBOOK_URL")
        html = htmlClient.getHtml(FACEBOOK_URL, username)
        findedText = texts.findTagText(html, "title")

        url = FACEBOOK_URL + username
        
        if "No se pudo encontrar la página | Facebook" in findedText:
            prints.notFoundPrint("Facebook", username)
        else:
            prints.foundPrint("Facebook", url)

    except ValueError:
        exceptions.printException(__name__)