from toph.common import exceptions, prints, htmlClient, texts
from os import getenv

def getData(username):
    try:
        GITHUB_URL = getenv("GITHUB_URL")
        html = htmlClient.getHtml(GITHUB_URL, username)
        findedText = texts.findTagText(html, "title")
        url = GITHUB_URL + username

        if findedText:
            if "Not Found" in findedText:
                prints.notFoundPrint("GitHub", username)
            else:
                prints.foundPrint("GitHub", url)
        else:
            prints.notFoundPrint("GitHub", username)
    except ValueError:
        exceptions.printException(__name__)