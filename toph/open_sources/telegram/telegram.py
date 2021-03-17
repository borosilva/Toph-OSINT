from toph.common import exceptions
from toph.open_sources.telegram.client import telegram_client

def checkByUserName(username):
    try:
        telegram_client.getData(username)

    except ValueError:
        exceptions.printException(__name__)