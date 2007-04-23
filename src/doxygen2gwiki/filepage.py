from utils import getText

from options import options

from templates.FilePage import FilePage

descriptions = {}
files = []

def registerDir(xml):
    dirname = getText(xml.getElementsByTagName("compoundname")[0].childNodes)
    for f in xml.getElementsByTagName("innerfile"):
        files.append((dirname, f.attributes["refid"].value, getText(f.childNodes)))

def registerFileBriefDescription(file, desc):
    descriptions[file] = desc

class DoxygenFilePage:
    def __init__(self):
        pass

    def createFiles(self):
        return [("wiki", options.prefix + "_files", FilePage(searchList={"summary": "A List of files with brief descriptions.", "labels": options.labels, "prefix": options.prefix, "files": files, "descriptions": descriptions}))]

from utils import getText
