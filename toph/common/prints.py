from os import system, name
from toph.config import colors

def clearPrint():
    system('cls' if name == 'nt' else "printf '\033c'")

def titlePrint(source):
    print((colors.colors.header + "########################### {} ###########################" + colors.colors.normal).format(source))

def infoPrint(key, value):
    print((colors.colors.blue + colors.colors.bold + " {}: " + colors.colors.normal + "{}").format(key.upper(), value))

def foundPrint(source, url):
    print((colors.colors.green + "[FOUND] " + colors.colors.blue + colors.colors.bold + " {}: " + colors.colors.normal + "{}").format(source, url))

def notFoundPrint(source, url):
    print((colors.colors.alert + "[NOT FOUND] " + colors.colors.blue + colors.colors.bold + " {}: " + colors.colors.normal + "{}").format(source, url))