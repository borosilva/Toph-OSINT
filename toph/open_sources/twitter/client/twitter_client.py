from toph.common import exceptions, regex, prints
from toph.config import colors
from os import getenv
from bs4 import BeautifulSoup
from requests import get

def getData(username):
    try:
        TWITTER_URL = getenv("TWITTER_URL")

        url = TWITTER_URL + username
        html = get(url).text
        soup = BeautifulSoup(html, "html.parser")
        for text in soup.findAll("h1"):
            text = regex.removeTags(str(text))
            print(text)
            if "Sorry" in text or "Lo sentimos," in text:
                    prints.notFoundPrint("Twitter", username)
            else:
                prints.foundPrint("Twitter", username)

    except ValueError:
        exceptions.printException(__name__)
