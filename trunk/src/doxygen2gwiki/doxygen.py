from xml.dom.minidom import parse

from options import options
from member_function import DoxygenMemberFunction
from file import DoxygenFile
from page import DoxygenPage
from utils import getText

class Doxygen:
    def __init__(self, xml):
        self.files = []
        self.processFile(xml)

    def processFile(self, xml):
        if xml.documentElement.tagName == "doxygenindex":
            pages = [node.attributes["refid"].value for node in xml.documentElement.getElementsByTagName("compound") if node.attributes["kind"].value == "page"]
            for f in pages:
                print "Processing", f + ".xml"
                self.processFile(parse(options.docs + f + ".xml"))
            files = [node.attributes["refid"].value for node in xml.documentElement.getElementsByTagName("compound") if node.attributes["kind"].value == "file"]
            for f in files:
                print "Processing", f + ".xml"
                self.processFile(parse(options.docs + f + ".xml"))
        elif xml.documentElement.tagName == "doxygen":
            compounds = xml.documentElement.getElementsByTagName("compounddef")
            for c in compounds:
                if c.attributes["kind"].value == "file":
                    self.files.append(DoxygenFile(c))
                elif c.attributes["kind"].value == "page":
                    self.files.append(DoxygenPage(c))
                else:
                    raise SystemError, "Unrecognised compound type. (%s)" % (c.attributes["kind"].value, )
        else:
            raise SystemError, "Unrecognised root file node. (%s)" % (xml.documentElement.tagName, )

    def createFiles(self):
        files = []
        for f in self.files:
            files += f.createFiles()
        return files
