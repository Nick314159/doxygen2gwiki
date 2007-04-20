from utils import getText

from options import options
from member_function import DoxygenMemberFunction

class DoxygenPage:
    def __init__(self, xml):
        self.id = xml.attributes["id"].value
        if self.id == "indexpage":
            self.pagename = options.prefix
        else:
            self.pagename = options.prefix + "_" + self.id

        doxygen.addLink(self.id, self.pagename)

        try:
            title = xml.getElementsByTagName("title")[0]
        except IndexError:
            self.title = ""
        else:
            self.title = getText(title.childNodes)

        self.detailed = convertLine(xml.getElementsByTagName("detaileddescription")[0], self)

    def createFiles(self):
        lines = [""]
        for d in self.detailed:
            d.getLines(lines)
        return [(self.pagename, "= %s =\n\n%s" % (self.title, "".join(lines)))]

from text_elements import convertLine
from doxygen import doxygen