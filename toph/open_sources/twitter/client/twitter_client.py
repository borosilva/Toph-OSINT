from toph.common import exceptions, regex, prints
from toph.config import colors
from os import getenv
from bs4 import BeautifulSoup
from requests import get
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def getData(username):
    try:
        TWITTER_URL = getenv("TWITTER_URL")
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        PATH = "/Users/vn5139c/Desktop/chromedriver"
        driver = webdriver.Chrome(PATH, options = options)

        url = TWITTER_URL + username
        driver.get(url)
        html = driver.page_source
        print(html)
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
