from toph.common import exceptions
from toph.open_sources.about_me.client import about_me_client

def checkByUserName(username):
    try:
        about_me_client.getData(username)

    except ValueError:
        exceptions.printException(__name__)

def getUserNameEmail(email):
	email = email.split("@")
	username = email[0]
	return username.replace(".","")