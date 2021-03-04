from toph.common import exceptions
from toph.open_sources.email_rep.client import email_rep_client
import numpy as np
import pandas as pd

def checkEmailRep(email):
    try:
        dataJson = email_rep_client.getData(email)
        DOMAIN = email.split("@")
        s = pd.Series(
                [
                    str(dataJson["reputation"]), 
                    str(dataJson["suspicious"]),
                    str(dataJson["details"]["blacklisted"]),
                    str(dataJson["details"]["malicious_activity"]),
                    str(DOMAIN[1]),
                    str(dataJson["details"]["domain_exists"]),
                    str(dataJson["details"]["first_seen"]),
                    str(dataJson["details"]["profiles"])
                ], 
                index=[
                    "Reputation:", 
                    "Suspicious:",
                    "Black listed:",
                    "Malicious Activity:",
                    "Domain:",
                    "Domain Exists:",
                    "First Seen:",
                    "Profiles:"
                ]
            )

        print("\n",s)
    except ValueError:
        exceptions.printException(__name__)