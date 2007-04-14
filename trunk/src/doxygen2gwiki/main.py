#!/usr/bin/python

import os
import sys
from xml.dom.minidom import parse

from options import options
from doxygen import Doxygen

def getPreviousFiles():
    try:
        return [x.strip() for x in open("%s%s.status" % (options.output, options.prefix), "r").readlines()]
    except IOError:
        return None

def addRemovePages(oldfiles, newfiles):
    if oldfiles is None:
        open("%s%s.status" % (options.output, options.prefix), "w").write("\n".join(newfiles))
        if not options.skip_svn:
            for f in newfiles:
                os.system("svn add %s%s" % (options.output, f))
            os.system("svn add %s%s.status" % (options.output, options.prefix))
        return
    for f in newfiles:
        try:
            index = oldfiles.index(f)
        except ValueError:
            # New file
            if not options.skip_svn:
                os.system("svn add %s%s" % (options.output, f))
        else:
            del oldfiles[index]
    if options.skip_svn:
        for f in oldfiles:
            os.unlink(options.output + f)
    else:
        for f in oldfiles:
            os.system("svn del %s%s" % (options.output, f))
    open("%s%s.status" % (options.output, options.prefix), "w").write("\n".join(newfiles))

def main():
    d = Doxygen(parse(options.docs + "index.xml"))

    oldfiles = getPreviousFiles()
    files = []

    for file, code in d.createFiles():
        file = file + ".wiki"
        files.append(file)

        open(options.output + file, "w").write(code)

    addRemovePages(oldfiles, files)
