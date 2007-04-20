from optparse import OptionParser

parser = OptionParser()
parser.add_option("-d", "--docs", dest="docs", default="docs/xml/",
                  help="Get documentation from this directory. (Default: docs/xml/)")
parser.add_option("-o", "--output", dest="output", default="wiki/",
                  help="Place the generated wiki pages in this directory. (Default: wiki/)")
parser.add_option("-p", "--prefix", dest="prefix", default="Doxygen",
                  help="Use this prefix when generating wiki pages. (Default: Doxygen)")
parser.add_option("-s", "--skip-svn", dest="skip_svn", default=False, action="store_true",
                  help="Skip attempts to control subversion. (Default: Control Subversion)")
parser.add_option("-l", "--label", dest="labels", default=[], action="append",
                  help="Apply this label to all pages.")
parser.add_option("-n", "--no-labels", dest="no_labels", default=False, action="store_true",
                  help="Don't apply any labels to the pages. (Overrides any --label options)")

(options, args) = parser.parse_args()

if not options.docs.endswith("/"):
    options.docs = options.docs + "/"
if not options.output.endswith("/"):
    options.output = options.output + "/"
