from toph.common import exceptions, validations, prints, config
from toph.menu import menu
from simple_term_menu import TerminalMenu
from toph.open_sources import email_rep

def onlyOneTargetMenu():
    try:
        targetOptionsConfig = config.getTargetOptions()
        targetOptions = TerminalMenu(
            targetOptionsConfig, title="Select one target type:")
        selectionIndex = targetOptions.show()

        if selectionIndex == 0:
            onlyOneTargetEmail()
        if selectionIndex == 1:
            onlyOneTargetUserName()
        if selectionIndex == 2:
            prints.clearPrint()
            menu.printMenu()
    except ValueError:
        exceptions.printException(__name__)

def onlyOneTargetEmail():
    try:
        email = str(input("Email: "))
        isValidEmail = validations.validateFormatEmail(email)
        if isValidEmail:
            email_rep.checkEmailRep(email)
        else:
            messageNotValid = " Email is not valid "
            print("\n", messageNotValid.center(40, '*'), "\n")
            onlyOneTargetMenu()
    except ValueError:
        exceptions.printException(__name__)

def onlyOneTargetUserName():
    try:
        prints.clearPrint()
        print("User name target WIP")
    except ValueError:
        exceptions.printException(__name__)
