import re

# for validating an Email 
regexEmail = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def validateFormatEmail(email):  
    if(re.search(regexEmail,email)):  
        return True
    else:  
        return False