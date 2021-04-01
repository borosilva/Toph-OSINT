from toph.common import exceptions, regex

def findTagText(parsedHtml, htmlTagName):
    try:
        for text in parsedHtml.findAll(htmlTagName):
            text = regex.removeTags(str(text))
            return text
    except ValueError:
        exceptions.printException(__name__)