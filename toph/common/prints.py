from os import system, name

def clearPrint():
    system('cls' if name == 'nt' else "printf '\033c'")