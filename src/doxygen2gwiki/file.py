from utils import getText, getDirectDescendents

from options import options
from member_function import DoxygenMemberFunction

from templates.FilePage import FilePage

class DoxygenFile:
    def __init__(self, xml):
        self.id = xml.attributes["id"].value
        self.name = getText(xml.getElementsByTagName("compoundname")[0].childNodes)
        self.brief = convertLine(getDirectDescendents(xml, "briefdescription")[0], self)
        self.detailed = convertLine(getDirectDescendents(xml, "detaileddescription")[0], self)

        l = [""]
        [x.getLines(l) for x in self.brief]
        registerFileBriefDescription(self.id, "".join(l).strip())

        funcs = getDirectDescendents(xml, "sectiondef")
        if len(funcs) > 0:
            self.functions = [DoxygenMemberFunction(x) for x in getDirectDescendents(funcs[0], "memberdef")]
        else:
            self.functions = []

        self.programlisting = ProgramListing(xml.getElementsByTagName("programlisting")[0], self)

    def createFiles(self):
        brief = [""]
        for b in self.brief:
            b.getLines(brief)
        detailed = [""]
        for b in self.detailed:
            b.getLines(detailed)
        return [("wiki", options.prefix + "_" + self.id, FilePage(searchList={"summary": "Documentation for the %s file" % (self.name, ), "labels": options.labels, "prefix": options.prefix, "filename": self.name, "briefdescription": "".join(brief).strip(), "detaileddescription": "".join(detailed).strip(), "functions": self.functions}))]

from text_elements import convertLine, ProgramListing
from filespage import registerFileBriefDescription
