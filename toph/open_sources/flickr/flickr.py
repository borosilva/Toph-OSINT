from toph.common import exceptions
from toph.open_sources.flickr.client import flickr_client

def checkByUserName(username):
    try:
        flickr_client.getData(username)

    except ValueError:
        exceptions.printException(__name__)