from toph.common import exceptions, prints, config
from toph.target import target
from simple_term_menu import TerminalMenu


def printMenu():
	try:
		menuOptionsConfig = config.getMenuOptions()
		menuOptions = TerminalMenu(menuOptionsConfig, title="Select one option:")
		selectionIndex = menuOptions.show()
		selectionMenu(selectionIndex)
	except ValueError:
		exceptions.printException(__name__)

def selectionMenu(selectionNumber):
	try:
		if selectionNumber == 0:
			target.onlyOneTargetMenu()
	except ValueError:
		exceptions.printException(__name__)

