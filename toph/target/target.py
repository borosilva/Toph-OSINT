from toph.common import exceptions, validations, prints, config
from toph.menu import menu
from simple_term_menu import TerminalMenu
from mechanize import Browser, _http

br = Browser()
br.set_handle_equiv( True ) 
br.set_handle_gzip( True ) 
br.set_handle_redirect( True ) 
br.set_handle_referer( True ) 
br.set_handle_robots( False ) 
br.set_handle_refresh( _http.HTTPRefreshProcessor(), max_time = 1 ) 
br.addheaders = [ ( 'User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1' ) ] 



def onlyOneTargetMenu():
    try:
        targetOptionsConfig = config.getTargetOptions()
        targetOptions = TerminalMenu(targetOptionsConfig, title="Select one target type:")
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
            print(email)
            checkPastebin(email)
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

def checkPastebin(email):
	url = "http://pastebin.com/search?q=" + email.replace(" ", "+")
	print("|--[INFO][PASTEBIN][SEARCH][>] " + url + "...")
	html = br.open(url).read()
	soup = BeautifulSoup(html, "html.parser")
	for div in soup.findAll("div", {"class", "gsc-thumbnail-inside"}):
		print("|--[INFO][PASTEBIN][URL][>]" + str(div))