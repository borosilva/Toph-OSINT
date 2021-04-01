from toph.common import exceptions, prints, htmlClient, texts
from os import getenv

def getData(username):
    try:
        SPOTIFY_URL = getenv("SPOTIFY_URL")
        html = htmlClient.getHtml(SPOTIFY_URL, username)
        findedText = texts.findTagText(html, "h1")
        url = SPOTIFY_URL + username

        if findedText:
            if username in findedText:
                prints.foundPrint("Spotify", url)               
        else:
            prints.notFoundPrint("Spotify", username)
    except ValueError:
        exceptions.printException(__name__)