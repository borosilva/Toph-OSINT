from toph.common import exceptions, prints
from toph.open_sources.email_rep.client import email_rep_client
from prettytable import PrettyTable

def checkEmailRep(email):
    try:
        TITLE = "EMAIL REP"

        dataJson = email_rep_client.getData(email)
        DOMAIN = email.split("@")
        x = PrettyTable()

        prints.titlePrint(TITLE)
        x.field_names = ["Info", "Results"]
        x.add_row(["Reputation", str(dataJson["reputation"])])
        x.add_row(["Suspicious", str(dataJson["suspicious"])])
        x.add_row(["Black listed", str(dataJson["details"]["blacklisted"])])
        x.add_row(["Malicious Activity", str(dataJson["details"]["malicious_activity"])])
        x.add_row(["Domain", str(DOMAIN[1])])
        x.add_row(["Domain Exists", str(dataJson["details"]["domain_exists"])])
        x.add_row(["First Seen", str(dataJson["details"]["first_seen"])])
        x.add_row(["Profiles", str(dataJson["details"]["profiles"])])
        print(x)
        
    except ValueError:
        exceptions.printException(__name__)