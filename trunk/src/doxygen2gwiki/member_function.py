from utils import getText

from templates.Function import Function

class DoxygenMemberFunction:
    def __init__(self, xml):
        try:
            self.refid = xml.attributes["refid"].value
        except KeyError:
            self.refid = xml.attributes["id"].value
        self.name = getText(xml.getElementsByTagName("name")[0].childNodes)

        l = [""]
        [x.getLines(l) for x in convertLine(xml.getElementsByTagName("briefdescription")[0], self)]
        self.brief = "".join(l).strip()

        l = [""]
        [x.getLines(l) for x in convertLine(xml.getElementsByTagName("detaileddescription")[0], self)]
        self.detailed = "".join(l).strip()

        self.type = getText(xml.getElementsByTagName("type")[0].childNodes)
        self.params = []
        for p in xml.getElementsByTagName("param"):
            type = getText(p.getElementsByTagName("type")[0].childNodes)
            declname = getText(p.getElementsByTagName("declname")[0].childNodes)
            self.params.append((type, declname))
        self.type = getText(xml.getElementsByTagName("type")[0].childNodes)

    def __get_sig(self):
        return self.type + " " + self.name + "(" + ", ".join(["%s %s" % x for x in self.params]) + ")"
    sig = property(__get_sig)

    def __get_doc(self):
        return unicode(Function(searchList={"f": self}))
    doc = property(__get_doc)

from text_elements import convertLine
