from toph.common import exceptions
from toph.open_sources.medium.client import medium_client

def checkByUserName(username):
    try:
        medium_client.getData(username)

    except ValueError:
        exceptions.printException(__name__)