from toph.common import exceptions, regex, prints
from toph.config import colors
from os import getenv
from bs4 import BeautifulSoup
from requests import get

def getData(username):
    try:
        #TODO descomentar cuando se solucione error 
        # TWITTER_URL = getenv("TWITTER_URL")

        # url = TWITTER_URL + username

        # html = get(url)
        # parsedXml = BeautifulSoup(html.content, "html.parser")

        # for text in parsedXml.findAll("h1"):
        #     print(text)
        #     text = regex.removeTags(str(text))
        #     print(text)
        #     if "Sorry" in text or "Lo sentimos," in text:
        #             prints.notFoundPrint("Twitter", username)
        #     else:
        #         prints.foundPrint("Twitter", username)

        prints.notFoundPrint("Twitter", "not available")

    except ValueError:
        exceptions.printException(__name__)
