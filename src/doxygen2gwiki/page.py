from utils import getText

from options import options
from member_function import DoxygenMemberFunction

class DoxygenPage:
    def __init__(self, xml):
        self.id = xml.attributes["id"].value

        try:
            title = xml.getElementsByTagName("title")[0]
        except IndexError:
            self.title = ""
        else:
            self.title = getText(title.childNodes)

        self.detailed = self.convertLine(xml.getElementsByTagName("detaileddescription")[0])

    def convertLine(self, node):
        text = []
        child = node.firstChild
        while child is not None:
            text.append(self.convertText(child))

            child = child.nextSibling
        return "".join(text)

    def convertText(self, node):
        if node.nodeType == node.TEXT_NODE:
            return node.data.strip()
        elif node.tagName == "highlight" or node.tagName == "bold":
            return "*" + self.convertLine(node) + "*"
        elif node.tagName == "emphasis":
            return "'" + self.convertLine(node) + "'"
        elif node.tagName == "sp":
            return " "
        elif node.tagName == "para":
            line = self.convertLine(node)
            if line.endswith("\n\n"):
                return line
            elif line.endswith("\n"):
                return line + "\n"
            else:
                return line + "\n\n"
        elif node.tagName == "computeroutput":
            return "{{{" + self.convertLine(node) + "}}}"
        elif node.tagName == "center":
            return self.convertLine(node)
        elif node.tagName == "heading":
            return "=" * int(node.attributes["level"].value) + " " + self.convertLine(node) + " " + "=" * int(node.attributes["level"].value)
        elif node.tagName == "htmlonly" or node.tagName == "latexonly":
            return ""
        elif node.tagName == "orderedlist":
            text = []
            child = node.firstChild
            while child is not None:
                if child.nodeType == child.TEXT_NODE:
                    pass
                elif child.tagName == "listitem":
                    text.append(" # " + self.convertLine(child))
                else:
                    print "Unknown node type in ordered list, " + child.tagName
                    text.append(" *Parsing error* ")

                child = child.nextSibling
            return "\n" + "".join(text)
        elif node.tagName == "itemizedlist":
            text = []
            child = node.firstChild
            while child is not None:
                if child.nodeType == child.TEXT_NODE:
                    pass
                elif child.tagName == "listitem":
                    text.append(" * " + self.convertLine(child))
                else:
                    print "Unknown node type in itemized list, " + child.tagName
                    text.append(" *Parsing error* ")

                child = child.nextSibling
            return "\n" + "".join(text)
        elif node.tagName == "sect1":
            return ""
        elif node.tagName == "formula":
            return "`" + self.convertLine(node) + "`"
        elif node.tagName == "ref":
            return " [" + node.attributes["refid"].value + "] "
        elif node.tagName == "ulink":
            return " [" + node.attributes["url"].value + " " + self.convertLine(node) + "] "
        elif node.tagName == "linebreak":
            return "\n"
        elif node.tagName == "copy":
            return "&copy;"
        elif node.tagName == "indexentry":
            return ""
        elif node.tagName == "umlaut":
            return "&%suml;" % (node.attributes["char"].value, )
        else:
            print "Unknown node type, " + node.tagName
            return " *Parsing error* "

    def createFiles(self):
        if self.id == "indexpage":
            id = options.prefix
        else:
            id = options.prefix + "_" + self.id
        return [(id, "= %s =\n\n%s" % (self.title, self.detailed))]
