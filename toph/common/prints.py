from os import system, name
from toph.config import colors

def clearPrint():
    system('cls' if name == 'nt' else "printf '\033c'")

def titlePrint(source):
    print((colors.colors.header + "########################### {} ###########################" + colors.colors.normal).format(source))

def infoPrint(key, value):
    print(("\r" + colors.colors.blue + colors.colors.bold + " {}: " + colors.colors.normal + "{}").format(key.upper(), value))

def foundPrint(source, url):
    print(("\r" + colors.colors.green + "[FOUND] " + colors.colors.blue + colors.colors.bold + " {}: " + colors.colors.normal +  " {} " + "\n").format(source, url))

def notFoundPrint(source, url):
    print(("\r" + colors.colors.alert + "[NOT FOUND] " + colors.colors.blue + colors.colors.bold + " {}: " + colors.colors.normal + " {} " + "\n").format(source, url))

def notAvailablePrint(source, url):
    print(("\r" + colors.colors.fail + "[NOT AVAILABLE] " + colors.colors.blue + colors.colors.bold + " {}: " + colors.colors.normal + " {} " + "\n").format(source, url))