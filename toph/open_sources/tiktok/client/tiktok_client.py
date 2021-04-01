from toph.common import exceptions, prints, htmlClient, texts
from os import getenv

def printData(username):
    try:
        TIKTOK_URL = getenv("TIKTOK_URL")
        html = htmlClient.getHtml(TIKTOK_URL, username)
        findedText = texts.findTagText(html, "title")
        url = TIKTOK_URL + username

        if len(findedText) > 6:
            prints.foundPrint("TikTok", url)
        else:
            prints.notFoundPrint("TikTok", username)
    except ValueError:
        exceptions.printException(__name__)

