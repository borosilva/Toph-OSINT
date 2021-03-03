from json import load

def getMenuOptions():
    with open('toph/config/menu.json') as f:
        data = load(f)
        menuOptions = data['optionsMenu']
        
    return menuOptions

def getTargetOptions():
    with open('toph/config/menu.json') as f:
        data = load(f)
        targetOptions = data['optionsTarget']
        
    return targetOptions