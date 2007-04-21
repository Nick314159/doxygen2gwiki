from utils import getText

from options import options
from member_function import DoxygenMemberFunction

class DoxygenFile:
    def __init__(self, xml):
        self.id = xml.attributes["id"].value
        self.brief = getText(xml.getElementsByTagName("briefdescription")[0].childNodes)
        self.detailed = getText(xml.getElementsByTagName("detaileddescription")[0].childNodes)

        self.programlisting = ProgramListing(xml.getElementsByTagName("programlisting")[0], self)

    def createFiles(self):
        lines = [""]
        self.programlisting.getLines(lines)
        return [("wiki", options.prefix + "_" + self.id, "".join(lines))]

from text_elements import ProgramListing
