from utils import getText

from options import options
from member_function import DoxygenMemberFunction

class DoxygenFile:
    def __init__(self, xml):
        self.id = xml.attributes["id"].value
        self.brief = convertLine(xml.getElementsByTagName("briefdescription")[0], self)
        self.detailed = getText(xml.getElementsByTagName("detaileddescription")[0].childNodes)

        l = [""]
        [x.getLines(l) for x in self.brief]
        registerFileBriefDescription(self.id, "".join(l).strip())

        self.programlisting = ProgramListing(xml.getElementsByTagName("programlisting")[0], self)

    def createFiles(self):
        lines = [""]
        self.programlisting.getLines(lines)
        return [("wiki", options.prefix + "_" + self.id, "".join(lines))]

from text_elements import convertLine, ProgramListing
from filepage import registerFileBriefDescription