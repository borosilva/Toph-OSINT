from toph.common import exceptions
from toph.open_sources.spotify.client import spotify_client

def checkByUserName(username):
    try:
        spotify_client.getData(username)

    except ValueError:
        exceptions.printException(__name__)