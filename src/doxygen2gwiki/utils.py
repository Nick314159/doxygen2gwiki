def getText(nodelist):
    rc = ""
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc = rc + node.data
    return rc

def getDirectDescendents(node, tagname):
    return [n for n in node.getElementsByTagName(tagname) if n.parentNode is node]