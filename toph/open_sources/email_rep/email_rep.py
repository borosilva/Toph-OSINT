from toph.common import exceptions, prints
from toph.open_sources.email_rep.client import email_rep_client

def checkEmailRep(email):
    try:
        TITLE = "EMAIL REP"

        dataJson = email_rep_client.getData(email)
        DOMAIN = email.split("@")

        prints.titlePrint(TITLE)
        prints.infoPrint("Reputation", str(dataJson["reputation"]))
        prints.infoPrint("Suspicious", str(dataJson["suspicious"]))
        prints.infoPrint("Black listed", str(dataJson["details"]["blacklisted"]))
        prints.infoPrint("Malicious Activity", str(dataJson["details"]["malicious_activity"]))
        prints.infoPrint("Domain", str(DOMAIN[1]))
        prints.infoPrint("Domain Exists", str(dataJson["details"]["domain_exists"]))
        prints.infoPrint("First Seen", str(dataJson["details"]["first_seen"]))
        prints.infoPrint("Profiles", str(dataJson["details"]["profiles"]))
        
    except ValueError:
        exceptions.printException(__name__)