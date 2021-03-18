from toph.common import exceptions
from toph.open_sources.tripadvisor.client import tripadvisor_client

def checkByUserName(username):
    try:
        tripadvisor_client.getData(username)

    except ValueError:
        exceptions.printException(__name__)

def getUserNameEmail(email):
	email = email.split("@")
	username = email[0]
	return username.replace(".","")