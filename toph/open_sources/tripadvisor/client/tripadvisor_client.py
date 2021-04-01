from toph.common import exceptions, prints, htmlClient, texts
from os import getenv

def getData(username):
    try:
        TRIPADVISOR_URL = getenv("TRIPADVISOR_URL")
        html = htmlClient.getHtml(TRIPADVISOR_URL, username)
        findedText = texts.findTagText(html, "title")
        url = TRIPADVISOR_URL + username

        if "  404 Not Found - Tripadvisor " in findedText:
            prints.notFoundPrint("Tripadvisor", username)
        else:
            prints.foundPrint("Tripadvisor", url)

    except ValueError:
        exceptions.printException(__name__)