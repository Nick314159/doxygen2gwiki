from utils import getText

class DoxygenMemberFunction:
    def __init__(self, xml):
        self.refid = xml.attributes["refid"].value
        self.name = getText(xml.getElementsByTagName("name")[0].childNodes)
