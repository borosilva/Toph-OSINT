from dotenv import load_dotenv
from toph.banner import banner
from toph.menu import menu

def run():
    load_dotenv()
    banner.printBanner()
    menu.printMenu()
