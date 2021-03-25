from toph.common import exceptions, validations, prints
from toph.config.menu import menuOptions
from toph.menu import menu
from simple_term_menu import TerminalMenu
from toph.open_sources import open_sources



def onlyOneTargetMenu():
    try:
        targetOptionsConfig = menuOptions.optionsTarget
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
            open_sources.searchOnAllOpenSourcesByEmail(email)
        else:
            messageNotValid = " Email is not valid "
            print("\n", messageNotValid.center(40, '*'), "\n")
            onlyOneTargetMenu()

    except ValueError:
        exceptions.printException(__name__)

def onlyOneTargetUserName():
    try:
        TITLE = " SEARCH BY USER NAME"
        username = str(input("User Name: "))
        
        prints.titlePrint(TITLE)
        open_sources.searchOnAllOpenSourcesByUsername(username)
    except ValueError:
        exceptions.printException(__name__)
