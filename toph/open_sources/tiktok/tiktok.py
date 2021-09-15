from toph.common import exceptions
from toph.open_sources.tiktok.client import tiktok_client

def checkByUserName(username):
    try:
        tiktok_client.getData(username)

    except ValueError:
        exceptions.printException(__name__)