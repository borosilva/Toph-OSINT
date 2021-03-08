from toph.common import exceptions
from toph.open_sources.twitter.client import twitter_client

def checkTwitterByEmail(email):
    try:
        username = getUserNameEmail(email)
        twitter_client.getData(username)

    except ValueError:
        exceptions.printException(__name__)

def checkTwitterByUserName(username):
    try:
        twitter_client.getData(username)

    except ValueError:
        exceptions.printException(__name__)

def getUserNameEmail(email):
	email = email.split("@")
	username = email[0]
	return username.replace(".","")