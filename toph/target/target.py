from toph.common import exceptions, validations, prints
from toph.config.menu import menuOptions
from toph.menu import menu
from simple_term_menu import TerminalMenu
from toph.open_sources.email_rep import email_rep
from toph.open_sources.instagram import instagram
from toph.open_sources.facebook import facebook
from toph.open_sources.twitter import twitter
from toph.open_sources.youtube import youtube
from toph.open_sources.pinterest import pinterest
from toph.open_sources.flickr import flickr
from toph.open_sources.medium import medium
from toph.open_sources.github import github
from toph.open_sources.about_me import about_me
from toph.open_sources.spotify import spotify

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
            email_rep.checkEmailRep(email)
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
        instagram.checkByUserName(username)
        facebook.checkByUserName(username)
        twitter.checkByUserName(username)
        youtube.checkByUserName(username)
        pinterest.checkByUserName(username)
        flickr.checkByUserName(username)
        medium.checkByUserName(username)
        github.checkByUserName(username)
        about_me.checkByUserName(username)
        spotify.checkByUserName(username)
    except ValueError:
        exceptions.printException(__name__)
