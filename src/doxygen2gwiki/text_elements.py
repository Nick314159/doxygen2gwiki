from utils import getText

def convertLine(node, parent):
    text = []
    child = node.firstChild
    while child is not None:
        if child.nodeType == child.TEXT_NODE:
            text.append(Text(child, parent))
        else:
            try:
                e = elements[child.tagName]
            except KeyError:
                print "Unrecognized element,", child.tagName
                t = Text(None, parent)
                t.text = getText(child.childNodes).strip()
                text.append(t)
            else:
                text.append(e(child, parent))

        child = child.nextSibling
    return text

class Text:
    def __init__(self, xml, parent):
        self.parent = parent
        if xml is not None:
            self.text = xml.data.strip("\n")

    def getLines(self, lines):
        if len(lines[-1]) > 0 and lines[-1][-1] == "\n":
            lines.append(self.text.lstrip())
        else:
            lines[-1] = lines[-1] + self.text

class Highlight:
    def __init__(self, xml, parent):
        self.parent = parent
        self.text = convertLine(xml, self)

    def getLines(self, lines):
        l = [""]
        [x.getLines(l) for x in self.text]
        text = "*" + "".join(l) + "*"
        if len(lines[-1]) > 0 and lines[-1][-1] == "\n":
            lines.append(text)
        else:
            lines[-1] = lines[-1] + text

class Emphasis:
    def __init__(self, xml, parent):
        self.parent = parent
        self.text = convertLine(xml, self)

    def getLines(self, lines):
        l = [""]
        [x.getLines(l) for x in self.text]
        text = "_" + "".join(l) + "_"
        if len(lines[-1]) > 0 and lines[-1][-1] == "\n":
            lines.append(text)
        else:
            lines[-1] = lines[-1] + text

class SuperScript:
    def __init__(self, xml, parent):
        self.parent = parent
        self.text = convertLine(xml, self)

    def getLines(self, lines):
        l = [""]
        [x.getLines(l) for x in self.text]
        text = "^" + "".join(l) + "^"
        if len(lines[-1]) > 0 and lines[-1][-1] == "\n":
            lines.append(text)
        else:
            lines[-1] = lines[-1] + text

class SubScript:
    def __init__(self, xml, parent):
        self.parent = parent
        self.text = convertLine(xml, self)

    def getLines(self, lines):
        l = [""]
        [x.getLines(l) for x in self.text]
        text = ",," + "".join(l) + ",,"
        if len(lines[-1]) > 0 and lines[-1][-1] == "\n":
            lines.append(text)
        else:
            lines[-1] = lines[-1] + text

class Para:
    def __init__(self, xml, parent):
        self.parent = parent
        self.text = convertLine(xml, self)

    def getLines(self, lines):
        if not lines[-1] == "\n":
            lines[-1] = lines[-1] + "\n"
        [x.getLines(lines) for x in self.text]
        if not lines[-1] == "\n":
            lines[-1] = lines[-1] + "\n"
        lines.append("\n")

class LineBreak:
    def __init__(self, xml, parent):
        self.parent = parent

    def getLines(self, lines):
        if len(lines[-1]) == 0:
            lines[-1] = "\n"
        elif not lines[-1].endswith("\n"):
            lines[-1] = lines[-1] + "\n"

class Sect1:
    def __init__(self, xml, parent):
        self.parent = parent
        while parent is not None and not hasattr(parent, "pagename"):
            parent = parent.parent
        if parent is not None:
            doxygen.addLink(xml.attributes["id"].value, parent.pagename)
        else:
            doxygen.addLink(xml.attributes["id"].value, None)
        self.text = convertLine(xml, self)

    def getLines(self, lines):
        [x.getLines(lines) for x in self.text]

class Ignore:
    def __init__(self, xml, parent):
        self.parent = parent

    def getLines(self, lines):
        pass

class Verbatim:
    def __init__(self, xml, parent):
        self.parent = parent
        self.text = convertLine(xml, self)

    def getLines(self, lines):
        if len(lines[-1]) == 0 or lines[-1][-1] != "\n":
            lines[-1] = lines[-1] + "\n"
        lines.append("{{{\n")
        for x in self.text:
            assert isinstance(x, Text)
            lines.append(x.text)
        if len(lines[-1]) == 0 or lines[-1][-1] != "\n":
            lines[-1] = lines[-1] + "\n"
        lines.append("}}}\n")

class ComputerOutput:
    def __init__(self, xml, parent):
        self.parent = parent
        self.text = convertLine(xml, self)

    def getLines(self, lines):
        l = [""]
        [x.getLines(l) for x in self.text]
        text = "`" + "".join(l) + "`"
        if len(lines[-1]) > 0 and lines[-1][-1] == "\n":
            lines.append(text)
        else:
            lines[-1] = lines[-1] + text

class Heading:
    def __init__(self, xml, parent):
        self.parent = parent
        self.text = convertLine(xml, self)

    def getLines(self, lines):
        l = [""]
        [x.getLines(l) for x in self.text]
        text = "= " + "".join(l) + " =\n"
        lines.append(text)

class ULink:
    def __init__(self, xml, parent):
        self.parent = parent
        self.url = xml.attributes["url"].value
        self.text = convertLine(xml, self)

    def getLines(self, lines):
        l = [""]
        [x.getLines(l) for x in self.text]
        text = "[" + self.url + " " + "".join(l) + "]"
        if len(lines[-1]) > 0 and lines[-1][-1] == "\n":
            lines.append(text)
        else:
            lines[-1] = lines[-1] + text

class Ref:
    def __init__(self, xml, parent):
        self.parent = parent
        self.ref = xml.attributes["refid"].value
        self.text = convertLine(xml, self)

    def getLines(self, lines):
        try:
            ref = doxygen.links[self.ref]
        except KeyError:
            ref = None
        l = [""]
        [x.getLines(l) for x in self.text]
        if ref:
            text = "[" + ref + " " + "".join(l) + "]"
        else:
            text = "".join(l)
        if len(lines[-1]) > 0 and lines[-1][-1] == "\n":
            lines.append(text)
        else:
            lines[-1] = lines[-1] + text

class ItemizedList:
    def __init__(self, xml, parent):
        self.parent = parent
        self.listitems = []
        child = xml.firstChild
        while child is not None:
            if child.nodeType == child.TEXT_NODE:
                pass
            elif child.tagName == "listitem":
                self.listitems.append(convertLine(child, self))
            else:
                print "Unknown node type in itemized list, " + child.tagName

            child = child.nextSibling

    def getLines(self, lines):
        if not lines[-1] == "\n":
            lines[-1] = lines[-1] + "\n"
        text = []
        for item in self.listitems:
            l = [""]
            [i.getLines(l) for i in item]
            text.append(" * " + "".join(l).strip() + "\n")
        lines.extend(text)

class OrderedList:
    def __init__(self, xml, parent):
        self.parent = parent
        self.listitems = []
        child = xml.firstChild
        while child is not None:
            if child.nodeType == child.TEXT_NODE:
                pass
            elif child.tagName == "listitem":
                self.listitems.append(convertLine(child, self))
            else:
                print "Unknown node type in itemized list, " + child.tagName

            child = child.nextSibling

    def getLines(self, lines):
        if not lines[-1] == "\n":
            lines[-1] = lines[-1] + "\n"
        text = []
        fake = False
        for item in self.listitems:
            l = [""]
            [i.getLines(l) for i in item]
            text.append(l)
            if len(l) > 1:
                fake = True

        if fake:
            for i in range(len(text)):
                lines.append(" %i. " % (i+1) + "".join(text[i]).strip() + "\n")
        else:
            lines.extend(["# " + "".join(l).strip() + "\n" for l in text])

class TocList:
    def __init__(self, xml, parent):
        self.parent = parent
        self.items = convertLine(xml, self)

    def getLines(self, lines):
        [x.getLines(lines) for x in self.items]

class TocItem:
    def __init__(self, xml, parent):
        self.parent = parent
        self.ref = xml.attributes["id"].value
        self.text = convertLine(xml, self)

    def getLines(self, lines):
        try:
            ref = doxygen.links[self.ref]
        except KeyError:
            ref = None
        l = [""]
        [x.getLines(l) for x in self.text]
        if ref:
            text = "[" + ref + " " + "".join(l) + "]"
        else:
            text = "".join(l)
        if len(lines[-1]) > 0 and lines[-1][-1] == "\n":
            lines.append(text[1:])
        else:
            lines[-1] = lines[-1] + text

class ProgramListing:
    def __init__(self, xml, parent):
        self.parent = parent
        self.code = [convertLine(x, self) for x in xml.getElementsByTagName("codeline")]

    def getLines(self, lines):
        if len(lines[-1]) == 0 or lines[-1][-1] != "\n":
            lines[-1] = lines[-1] + "\n"
        for l in self.code:
            [x.getLines(lines) for x in l]
            if len(lines[-1]) == 0 or lines[-1][-1] != "\n":
                lines[-1] = lines[-1] + "\n"
        if len(lines[-1]) == 0 or lines[-1][-1] != "\n":
            lines[-1] = lines[-1] + "\n"
        lines.append("\n")

class Space:
    def __init__(self, xml, parent):
        self.parent = parent

    def getLines(self, lines):
        lines[-1] = lines[-1] + " "

elements = {
    "highlight": Highlight,
    "bold": Highlight,
    "emphasis": Emphasis,
    "para": Para,
    "sect1": Sect1,
    "htmlonly": Ignore,
    "latexonly": Ignore,
    "hruler": Ignore,
    "indexentry": Ignore,
    "verbatim": Verbatim,
    "computeroutput": ComputerOutput,
    "heading": Heading,
    "title": Heading,
    "ulink": ULink,
    "ref": Ref,
    "toclist": TocList,
    "tocitem": TocItem,
    "itemizedlist": ItemizedList,
    "orderedlist": OrderedList,
    "simplesect": Para,
    "linebreak": LineBreak,
    "programlisting": ProgramListing,
    "superscript": SuperScript,
    "subscript": SubScript,
    "sp": Space
}

from doxygen import doxygen
