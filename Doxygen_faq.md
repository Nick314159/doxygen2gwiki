  1. **How to get information on the index page in HTML?**

You should use the \mainpage command inside a comment block like this:
```
/*! \mainpage My Personal Index Page
 *
 * \section intro_sec Introduction
 *
 * This is the introduction.
 *
 * \section install_sec Installation
 *
 * \subsection step1 Step 1: Opening the box
 *  
 * etc...
 */
```
> 2. **Help, some/all of the members of my class / file / namespace are not documented?**

Check the following:
  1. Is your class / file / namespace documented? If not, it will not be extracted from the sources unless `EXTRACT_ALL` is set to `YES` in the config file.
> 2. Are the members private? If so, you must set `EXTRACT_PRIVATE` to `YES` to make them appear in the documentation.
> 3. Is there a function macro in your class that does not end with a semicolon (e.g. MY\_MACRO())? If so then you have to instruct doxygen's preprocessor to remove it.

This typically boils down to the following settings in the config file:

```
ENABLE_PREPROCESSING   = YES
MACRO_EXPANSION        = YES
EXPAND_ONLY_PREDEF     = YES
PREDEFINED             = MY_MACRO()=
      
```


Please read the [preprocessing](Doxygen_preprocessing.md)  section of the manual for more information.
> 3. **When I set EXTRACT\_ALL to NO none of my functions are shown in the documentation.**

In order for global functions, variables, enums, typedefs, and defines to be documented you should document the file in which these commands are located using a comment block containing a \file (or @file) command.

Alternatively, you can put all members in a group (or module) using the \ingroup command and then document the group using a comment block containing the \defgroup command.

For member functions or functions that are part of a namespace you should document either the class or namespace.
> 4. **How can I make doxygen ignore some code fragment?**

The new and easiest way is to add one comment block with a [\cond](Doxygen_commands.md)  command at the start and one comment block with a [\endcond](Doxygen_commands.md)  command at the end of the piece of code that should be ignored. This should be within the same file of course.

But you can also use Doxygen's preprocessor for this: If you put
```
#ifndef DOXYGEN_SHOULD_SKIP_THIS

 /* code that must be skipped by Doxygen */

#endif /* DOXYGEN_SHOULD_SKIP_THIS */
```
around the blocks that should be hidden and put:
```
  PREDEFINED = DOXYGEN_SHOULD_SKIP_THIS
```
in the config file then all blocks should be skipped by Doxygen as long as `PREPROCESSING = YES`.
> 5. **How can I change what is after the `#include` in the class documentation?**

In most cases you can use STRIP\_FROM\_INC\_PATH to strip a user defined part of a path.

You can also document your class as follows

```
/*! \class MyClassName include.h path/include.h
 *
 *  Docs for MyClassName
 */
```


To make doxygen put

` #include <path/include.h> `

in the documentation of the class MyClassName regardless of the name of the actual header file in which the definition of MyClassName is contained.

If you want doxygen to show that the include file should be included using quotes instead of angle brackets you should type:
```
/*! \class MyClassName myhdr.h "path/myhdr.h"
 *
 *  Docs for MyClassName
 */
```
> 6. **How can I use tag files in combination with compressed HTML?**

If you want to refer from one compressed HTML file `a.chm` to another compressed HTML file called `b.chm`, the link in `a.chm` must have the following format:
```
<a href="b.chm::/file.html">
```
Unfortunately this only works if both compressed HTML files are in the same directory.

As a result you must rename the generated `index.chm` files for all projects into something unique and put all `.chm` files in one directory.

Suppose you have a project _a_ referring to a project _b_ using tag file `b.tag`, then you could rename the `index.chm` for project _a_ into `a.chm` and the `index.chm` for project _b_ into `b.chm`. In the configuration file for project _a_ you write:
```
TAGFILES = b.tag=b.chm::
```
or you can use `installdox` to set the links as follows:
```
installdox -lb.tag@b.chm::
```
> 7. **I don't like the quick index that is put above each HTML page, what do I do?**

You can disable the index by setting DISABLE\_INDEX to YES. Then you can put in your own header file by writing your own header and feed that to HTML\_HEADER.
> 8. **The overall HTML output looks different, while I only wanted to use my own html header file**

You probably forgot to include the stylesheet `doxygen.css` that doxygen generates. You can include this by putting
```
<LINK HREF="doxygen.css" REL="stylesheet" TYPE="text/css">
```
in the HEAD section of the HTML page.
> 9. **Why does doxygen use Qt?**

The most important reason is to have a platform abstraction for most Unices and Windows by means of the QFile, QFileInfo, QDir, QDate, QTime and QIODevice classes. Another reason is for the nice and bug free utility classes, like QList, QDict, QString, QArray, QTextStream, QRegExp, QXML etc.

The GUI front-end doxywizard uses Qt for... well... the GUI!
  1. . **How can I exclude all test directories from my directory tree?**

Simply put an exclude pattern like this in the configuration file:

```
EXCLUDE_PATTERNS = */test/*
```
  1. . **Doxygen automatically generates a link to the class MyClass somewhere in the running text. How do I prevent that at a certain place?**

Put a % in front of the class name. Like this: %MyClass. Doxygen will then remove the % and keep the word unlinked.
  1. . **My favourite programming language is X. Can I still use doxygen?**

No, not as such; doxygen needs to understand the structure of what it reads. If you don't mind spending some time on it, there are several options:
  * If the grammar of X is close to C or C++, then it is probably not too hard to tweak src/scanner.l a bit so the language is supported. This is done for all other languages directly supported by doxygen (i.e. Java, IDL, C#, PHP).
  * If the grammar of X is somewhat different than you can write an input filter that translates X into something similar enough to C/C++ for doxygen to understand (this approach is taken for VB, Object Pascal, and Javascript, see [http://www.stack.nl/~dimitri/doxygen/download.html#helpers](http://www.stack.nl/~dimitri/doxygen/download.html#helpers)).
  * If the grammar is completely different one could write a parser for X and write a backend that produces a similar syntax tree as is done by src/scanner.l (and also by src/tagreader.cpp while reading tag files).
  1. . **Help! I get the cryptic message "input buffer overflow, can't enlarge buffer because scanner uses REJECT"**

This error happens when doxygen's lexical scanner has a rule that matches more than 256K of input characters in one go. I've seen this happening on a very large generated file (>256K lines), where the built-in preprocessor converted it into an empty file (with >256K of newlines). Another case where this might happen is if you have lines in your code with more than 256K characters.

If you have run into such a case and want me to fix it, you should send me a code fragment that triggers the message. To work around the problem, put some line-breaks into your file, split it up into smaller parts, or exclude it from the input using EXCLUDE.
  1. . **When running make in the latex dir I get "TeX capacity exceeded". Now what?**

You can edit the texmf.cfg file to increase the default values of the various buffers and then run "texconfig init".
  1. . **Why are dependencies via STL classes not shown in the dot graphs?**

Doxygen is unware of the STL classes, unless the option BUILTIN\_STL\_SUPPORT is turned on.
  1. . **I have problems getting the search engine to work with PHP5 and/or windows**

Please read [searchengine.html this] for hints on where to look.
  1. . **Can I configure doxygen from the command line?**

Not via command line options, but doxygen can read from `stdin`, so you can pipe things through it. Here's an example how to override an option in a configuration file from the command line (assuming a unix environment):

```
( cat Doxyfile ; echo "PROJECT_NUMBER=1.0" ) | doxygen -
```


If multiple options with the same name are specified then doxygen will use the last one. To append to an existing option you can use the += operator.
  1. . **How did doxygen get its name?**

Doxygen got its name from playing with the words documentation and generator.

```
documentation -> docs -> dox
generator -> gen
```


At the time I was looking into lex and yacc, where a lot of things start with "yy", so the "y" slipped in and made things pronounceable (the proper pronouncement is Docs-ee-gen, so with a long "e").
  1. . **What was the reason to develop doxygen?**

I once wrote a GUI widget based on the Qt library (it is still available at [http://qdbttabular.sourceforge.net/](http://qdbttabular.sourceforge.net/) and maintained by Sven Meyer). Qt had nicely generated documentation (using an internal tool which they didn't want to release) and I wrote similar docs by hand. This was a nightmare to maintain, so I wanted a similar tool. I looked at Doc++ but that just wasn't good enough (it didn't support signals and slots and did not have the Qt look and feel I had grown to like), so I started to write my own tool...





---
| [Main Page](Doxygen.md) | [Files](Doxygen_files.md) |
|:------------------------|:--------------------------|