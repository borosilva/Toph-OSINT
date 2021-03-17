from toph.common import exceptions, regex, prints
from toph.config import colors
from os import getenv
from bs4 import BeautifulSoup
from requests import get

def getData(username):
    try:
        TELEGRAM_URL = getenv("TELEGRAM_URL")
        PARAMS = dict(lang='en-US')
        
        url = TELEGRAM_URL + username
        html = get(url, params=PARAMS).text
        parsedHtml = BeautifulSoup(html, "html.parser")
        findedClass = parsedHtml.find_all("div", {"class": "tgme_page_post"})
        removedTag = regex.removeTags(str(findedClass))

        if len(removedTag) > 0:
            prints.foundPrint("Telegram",username,url)
        else:
            prints.notFoundPrint("Telegram", username)

    except ValueError:
        exceptions.printException(__name__)