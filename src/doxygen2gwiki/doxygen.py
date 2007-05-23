import os
from xml.dom.minidom import parseString

from options import options
from utils import getText
from fix_xml import fixXML

class Doxygen:
    def __init__(self):
        self.files = []
        self.staticfiles = []
        self.links = {}
        self.footer = {}
        if options.no_labels:
            self.labels = []
        elif options.labels == []:
            self.labels = ["Doxygen"]
        else:
            self.labels = options.labels

    def processFile(self, xml):
        if xml.documentElement.tagName == "doxygenindex":
            pages = [node.attributes["refid"].value for node in xml.documentElement.getElementsByTagName("compound") if node.attributes["kind"].value == "page"]
            for f in pages:
                if options.verbose:
                    print "Processing", f + ".xml"
                self.processFile(parseString(fixXML(open(options.docs + f + ".xml", "r").read())))
            files = [node.attributes["refid"].value for node in xml.documentElement.getElementsByTagName("compound") if node.attributes["kind"].value == "file"]
            for f in files:
                if options.verbose:
                    print "Processing", f + ".xml"
                self.processFile(parseString(fixXML(open(options.docs + f + ".xml", "r").read())))
            dirs = [node.attributes["refid"].value for node in xml.documentElement.getElementsByTagName("compound") if node.attributes["kind"].value == "dir"]
            for f in dirs:
                if options.verbose:
                    print "Processing", f + ".xml"
                self.processFile(parseString(fixXML(open(options.docs + f + ".xml", "r").read())))
            for c in xml.documentElement.getElementsByTagName("compound"):
                registerGlobals(c)
        elif xml.documentElement.tagName == "doxygen":
            compounds = xml.documentElement.getElementsByTagName("compounddef")
            for c in compounds:
                if c.attributes["kind"].value == "file":
                    self.footer["file"] = True
                    self.files.append(DoxygenFile(c))
                elif c.attributes["kind"].value == "page":
                    self.files.append(DoxygenPage(c))
                elif c.attributes["kind"].value == "dir":
                    registerDir(c)
                else:
                    raise SystemError, "Unrecognised compound type. (%s)" % (c.attributes["kind"].value, )
        else:
            raise SystemError, "Unrecognised root file node. (%s)" % (xml.documentElement.tagName, )

    def addLink(self, refid, linkto):
        self.links[refid] = linkto

    def createFiles(self):
        files = []
        for f in self.files:
            files += f.createFiles()
        if self.footer.has_key("file"):
            files += DoxygenFilesPage().createFiles()
        if self.footer.has_key("globals"):
            files += DoxygenGlobalsPage().createFiles()
        return files + self.staticfiles

    def getFooter(self):
        footer = "---\n|| [%s Main Page]" % (options.prefix, )
        if self.footer.has_key("file"):
            footer += " || [%s_files Files]" % (options.prefix, )
        footer += " ||\n"
        return footer

    def copyFile(self, type, _from, _to):
        if options.output + _to not in [x[1] for x in self.staticfiles]:
            open(options.output + _to, "wb").write(open(_from, "rb").read())
            self.staticfiles.append(("static", _to, None))

doxygen = Doxygen()

from page import DoxygenPage
from file import DoxygenFile
from filespage import registerDir, DoxygenFilesPage
from globalspage import registerGlobals, DoxygenGlobalsPage
from member_function import DoxygenMemberFunction
