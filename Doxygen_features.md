  * Requires very little overhead from the writer of the documentation. Plain text will do, but for more fancy or structured output HTML tags and/or some of doxygen's special commands can be used.
  * Supports C/C++, Java, (Corba and Microsoft) Java, Python, IDL, C#, Objective-C and to some extent D and PHP sources.
  * Supports documentation of files, namespaces, packages, classes, structs, unions, templates, variables, functions, typedefs, enums and defines.
  * JavaDoc (1.1), Qt-Doc, and ECMA-334 (C# spec.) compatible.
  * Automatically generates class and collaboration diagrams in HTML (as clickable image maps) and ![http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png](http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png)  (as Encapsulated PostScript images).
  * Uses the dot tool of the Graphviz tool kit to generate include dependency graphs, collaboration diagrams, and graphical class hierarchy graphs.
  * Flexible comment placement: Allows you to put documentation in the header file (before the declaration of an entity), source file (before the definition of an entity) or in a separate file.
  * Generates a list of all members of a class (including any inherited members) along with their protection level.
  * Outputs documentation in on-line format (HTML and UNIX man page) and off-line format (![http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png](http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png)  and RTF) simultaneously (any of these can be disabled if desired). All formats are optimized for ease of reading.
Furthermore, compressed HTML can be generated from HTML output using Microsoft's HTML Help Workshop (Windows only) and PDF can be generated from the ![http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png](http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png)  output.
  * Includes a full C preprocessor to allow proper parsing of conditional code fragments and to allow expansion of all or part of macros definitions.
  * Automatically detects public, protected and private sections, as well as the Qt specific signal and slots sections. Extraction of private class members is optional.
  * Automatically generates references to documented classes, files, namespaces and members. Documentation of global functions, globals variables, typedefs, defines and enumerations is also supported.
  * References to base/super classes and inherited/overridden members are generated automatically.
  * Includes a fast, rank based search engine to search for strings or words in the class and member documentation.
  * You can type normal HTML tags in your documentation. Doxygen will convert them to their equivalent ![http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png](http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png) , RTF, and man-page counterparts automatically.
  * Allows references to documentation generated for other projects (or another part of the same project) in a location independent way.
  * Allows inclusion of source code examples that are automatically cross-referenced with the documentation.
  * Inclusion of undocumented classes is also supported, allowing to quickly learn the structure and interfaces of a (large) piece of code without looking into the implementation details.
  * Allows automatic cross-referencing of (documented) entities with their definition in the source code.
  * All source code fragments are syntax highlighted for ease of reading.
  * Allows inclusion of function/member/class definitions in the documentation.
  * All options are read from an easy to edit and (optionally) annotated configuration file.
  * Documentation and search engine can be transferred to another location or machine without regenerating the documentation.
  * Can cope with large projects easily.


Although doxygen can be used in any C or C++ project, initially it was specifically designed to be used for projects that make use of Troll Tech's [Qt toolkit](http://www.trolltech.com/products/qt.html). I have tried to make doxygen `Qt-compatible'. That is: Doxygen can read the documentation contained in the Qt source code and create a class browser that looks very similar to the one that is generated by Troll Tech. Doxygen understands the C++ extensions used by Qt such as signals and slots.

Doxygen can also automatically generate links to existing documentation that was generated with Doxygen or with Qt's non-public class browser generator. For a Qt based project this means that whenever you refer to members or classes belonging to the Qt toolkit, a link will be generated to the Qt documentation. This is done independent of where this documentation is located!


---
| [Main Page](Doxygen.md) | [Files](Doxygen_files.md) |
|:------------------------|:--------------------------|