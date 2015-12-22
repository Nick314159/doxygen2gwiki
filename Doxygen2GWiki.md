# Introduction #

Doxygen2GWiki is a tool which takes [Doxygen](http://www.doxygen.org) generated documentation and converts it into a Google Code's Wiki markup. It can also [control subversion](CommandLineParameters.md), adding and removing files from the repository as necessary.

# Running Doxygen2GWiki #

To run Doxygen2GWiki simply type...
```
doxygen2gwiki
```

This will look for Doxygen generated XML documentation in `doc/xml` and place the resulting code into `wiki/`.

The location of the various files can be controlled through the use of options...
```
doxygen2gwiki -d examples/doxygen/doc/xml -o examples/doxygen/wiki -p Example
```

This command will look for the XML documentation in `examples/doxygen/doc/xml` and will place the output into `examples/doxygen/wiki`. All filenames will be prefixed with `Example_` rather than the default `Doxygen_`.

# Examples #

As an example, the complete Doxygen user manual can be found [here](Doxygen.md). The equivalent HTML output is [here](http://www.stack.nl/~dimitri/doxygen/manual.html).

More examples can be found [here](ListOfExamples.md).

# Useful Pages #

Below is a list of pages you might find useful when learning how to use Doxygen2GWiki.

  * [Command Line Parameters](CommandLineParameters.md)
  * [Version History](History.md)