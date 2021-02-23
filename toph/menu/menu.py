from toph.common import exceptions

def printMenu():
	print("")
	print("------------------------------------------------------------------------")
	print("--- 1. Only one target                                               ---")
	print("--- 0. Exit                                                          ---")
	print("------------------------------------------------------------------------")
	print("")
	try:
		selection = int(input("Select 1 or 0: "))
		return selection
	except ValueError:
		exceptions.printException(__name__)