from toph.common import exceptions, prints, htmlClient, regex
from os import getenv

def getData(username):
    try:
        TELEGRAM_URL = getenv("TELEGRAM_URL")
        html = htmlClient.getHtml(TELEGRAM_URL, username)
        url = TELEGRAM_URL + username
        findedClass = html.find_all("div", {"class": "tgme_page_extra"})
        removedTag = regex.removeTags(str(findedClass))

        if len(removedTag) > 2:
            prints.foundPrint("Telegram",url)
        else:
            prints.notFoundPrint("Telegram", username)

    except ValueError:
        exceptions.printException(__name__)