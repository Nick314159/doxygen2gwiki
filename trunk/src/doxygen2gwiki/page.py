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

    #def convertText(self, node):
        #if node.nodeType == node.TEXT_NODE:
            #return node.data
        #elif node.tagName == "highlight" or node.tagName == "bold":
            #return "*" + self.convertLine(node) + "*"
        #elif node.tagName == "emphasis":
            #return "'" + self.convertLine(node) + "'"
        #elif node.tagName == "title":
            #return "= " + self.convertLine(node) + " ="
        #elif node.tagName == "verbatim":
            #return "{{{\n" + self.convertLine(node) + "\n}}}"
        #elif node.tagName == "sp":
            #return " "
        #elif node.tagName == "para":
            #line = self.convertLine(node)
            #if line.endswith("\n\n"):
                #return line
            #elif line.endswith("\n"):
                #return line + "\n"
            #else:
                #return line + "\n\n"
        #elif node.tagName == "computeroutput":
            #return "`" + self.convertLine(node) + "`"
        #elif node.tagName == "center":
            #return self.convertLine(node)
        #elif node.tagName == "heading":
            #return "=" * int(node.attributes["level"].value) + " " + self.convertLine(node) + " " + "=" * int(node.attributes["level"].value)
        #elif node.tagName == "htmlonly" or node.tagName == "latexonly":
            #return ""
        #elif node.tagName == "orderedlist":
            #text = []
            #child = node.firstChild
            #while child is not None:
                #if child.nodeType == child.TEXT_NODE:
                    #pass
                #elif child.tagName == "listitem":
                    #text.append(" # " + self.convertLine(child).strip() + "\n")
                #else:
                    #print "Unknown node type in ordered list, " + child.tagName
                    #text.append(" *Parsing error* ")

                #child = child.nextSibling
            #return "\n" + "".join(text)
        #elif node.tagName == "itemizedlist":
            #text = []
            #child = node.firstChild
            #while child is not None:
                #if child.nodeType == child.TEXT_NODE:
                    #pass
                #elif child.tagName == "listitem":
                    #text.append(" * " + self.convertLine(child).strip() + "\n")
                #else:
                    #print "Unknown node type in itemized list, " + child.tagName
                    #text.append(" *Parsing error* ")

                #child = child.nextSibling
            #return "\n" + "".join(text)
        #elif node.tagName == "sect1":
            #return self.convertLine(node)
        #elif node.tagName == "formula":
            #return "`" + self.convertLine(node) + "`"
        #elif node.tagName == "ref":
            #return " [" + options.prefix + "_" + node.attributes["refid"].value + " " + self.convertLine(node) + "] "
        #elif node.tagName == "ulink":
            #return " [" + node.attributes["url"].value + " " + self.convertLine(node) + "] "
        #elif node.tagName == "linebreak":
            #return "\n"
        #elif node.tagName == "copy":
            #return "&copy;"
        #elif node.tagName == "indexentry":
            #return ""
        #elif node.tagName == "umlaut":
            #return "&%suml;" % (node.attributes["char"].value, )
        #else:
            #print "Unknown node type, " + node.tagName
            #return " *Parsing error* "

    def createFiles(self):
        lines = [""]
        for d in self.detailed:
            d.getLines(lines)
        return [(self.pagename, "= %s =\n\n%s" % (self.title, "".join(lines)))]

from text_elements import convertLine
from doxygen import doxygen
