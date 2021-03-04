from toph.common import exceptions
from toph.config.menu import menuOptions
from toph.target import target
from simple_term_menu import TerminalMenu


def printMenu():
	try:
		menuOptionsConfig = menuOptions.optionsMenu
		menuOptionsTermnial = TerminalMenu(menuOptionsConfig, title="Select one option:")
		selectionIndex = menuOptionsTermnial.show()
		selectionMenu(selectionIndex)
	except ValueError:
		exceptions.printException(__name__)

def selectionMenu(selectionNumber):
	try:
		if selectionNumber == 0:
			target.onlyOneTargetMenu()
	except ValueError:
		exceptions.printException(__name__)

