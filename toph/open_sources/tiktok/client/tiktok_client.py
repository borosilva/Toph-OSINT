from toph.common import exceptions, prints, htmlClient, texts
from os import getenv

def getData(username):
    try:
        TIKTOK_URL = getenv("TIKTOK_URL")
        html = htmlClient.getHtml(TIKTOK_URL, username)
        url = TIKTOK_URL + username
        findedMeta = html.find_all("meta", {"property": "og:title"})

        if len(findedMeta) > 0:
            contentAttr = str(findedMeta[0])
            findedContentAttr = contentAttr.find(username)
            if findedContentAttr > 0:
                prints.foundPrint("TikTok ", url)
            else:
                prints.notFoundPrint("TikTok", username)

    except ValueError:
        exceptions.printException(__name__)