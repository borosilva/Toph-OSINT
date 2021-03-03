from toph.common import exceptions
from json import loads
from requests import get

def checkEmailRep(email):
    try:
        url = "https://emailrep.io/" + email
        JSON = loads(get(url).text)

        if JSON["status"] == 'fail':
            exceptions.printException(JSON["reason"])
        else: 
            print("|--[INFO][REPUTATION][>] " + JSON["reputation"])
            print("|--[INFO][SUSPICIUS][>] " + str(JSON["suspicious"]))
            print("|--[INFO][BLACK LIST][>] " + str(JSON["details"]["blacklisted"]))
            print("|--[INFO][MALICIUS ACTIVITY][>] " + str(JSON["details"]["malicious_activity"]))
            print("|--[INFO][SPAM][>] " + str(JSON["details"]["spam"]))
            print("|--[INFO][MALICIUS ACTIVITY][>] " + str(JSON["details"]["malicious_activity"]))
            
            DOMAIN = email.split("@")
            print("|--[INFO][DOMAIN][>] Analyzing the domain " + DOMAIN[1])
            print("|----[INFO][CHECK DOMAIN][>] " + str(JSON["details"]["domain_exists"]))
            print("|----[INFO][DOMAIN REPUTATION][>] " + str(JSON["details"]["domain_reputation"]))
            print("|----[INFO][NEW DOMAIN][>] " + str(JSON["details"]["new_domain"]))
            print("|------[INFO][DAYS SINCE DOMAIN CREATION][>] " + str(JSON["details"]["days_since_domain_creation"]))
            print("|------[INFO][FREE PROVIDER][>] " + str(JSON["details"]["free_provider"]))

    except ValueError:
        exceptions.printException(__name__)