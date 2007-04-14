from utils import getText

from options import options
from member_function import DoxygenMemberFunction

class DoxygenFile:
    def __init__(self, xml):
        self.id = xml.attributes["id"].value
        self.brief = getText(xml.getElementsByTagName("briefdescription")[0].childNodes)
        self.detailed = getText(xml.getElementsByTagName("detaileddescription")[0].childNodes)

        self.programlisting = []
        for line in xml.getElementsByTagName("programlisting")[0].getElementsByTagName("codeline"):
            self.programlisting.append(self.convertLine(line))
        self.programlisting = "\n".join(self.programlisting)

    def convertLine(self, node):
        text = []
        child = node.firstChild
        while child is not None:
            text.append(self.convertText(child))

            child = child.nextSibling
        return "".join(text)

    def convertText(self, node):
        if node.nodeType == node.TEXT_NODE:
            return node.data
        elif node.tagName == "highlight":
            return "*" + self.convertLine(node) + "*"
        elif node.tagName == "sp":
            return " "
        else:
            print "Unknown node type, " + node.tagName
            return " *Parsing error* "

    def createFiles(self):
        return [(options.prefix + "_" + self.id, self.programlisting)]
