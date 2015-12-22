First go to the [download](http://www.doxygen.org/download.html) page  to get the latest distribution, if you did not have it already.

This section is divided into the following sections:
  * [Compiling from source on Unix](Doxygen_install.md)
  * [Installing the binaries on Unix](Doxygen_install.md)
  * [Known compilation problems for Unix](Doxygen_install.md)
  * [Compiling from source on Windows](Doxygen_install.md)
  * [Installing the binaries on Windows](Doxygen_install.md)
  * [Tools used to develop doxygen](Doxygen_install.md)


# Compiling from source on Unix #

If you downloaded the source distribution, you need at least the following to build the executable:
  * The [GNU](ftp://prep.ai.mit.edu/pub/gnu/) tools flex, bison and make
  * In order to generate a Makefile for your platform, you need [perl](http://www.perl.com/) .


To take full advantage of doxygen's features the following additional tools should be installed.

  * Troll Tech's GUI toolkit [Qt](http://www.trolltech.com/products/qt.html)   version 3.2 or higher. This is needed to build the GUI front-end doxywizard.
  * A ![http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png](http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png)  distribution: for instance [teTeX 1.0](http://www.tug.org/interest.html#free) . This is needed for generating LaTeX, Postscript, and PDF output.
  * [the Graph visualization toolkit version 1.8.10 or higher](http://www.graphviz.org/) . Needed for the include dependency graphs, the graphical inheritance graphs, and the collaboration graphs. If you compile graphviz yourself, make sure you do include freetype support (which requires the freetype library and header files), otherwise the graphs will not render proper text labels.
  * The ghostscript interpreter. To be found at [www.ghostscript.com](http://www.ghostscript.com/).


Compilation is now done by performing the following steps:

  1. Unpack the archive, unless you already have done that:

```
    gunzip doxygen-$VERSION.src.tar.gz    # uncompress the archive
    tar xf doxygen-$VERSION.src.tar       # unpack it
```
> 2. Run the configure script:

```
    sh ./configure
```


The script tries to determine the platform you use, the make tool (which _must_ be GNU make) and the perl interpreter. It will report what it finds.

To override the auto detected platform and compiler you can run configure as follows:

```
    configure --platform platform-type
```


See the `PLATFORMS` file for a list of possible platform options.

If you have Qt-3.2.x or higher installed and want to build the GUI front-end, you should run the configure script with the `--with-doxywizard` option:

```
    configure --with-doxywizard
```


For an overview of other configuration options use

```
    configure --help
```
> 3. Compile the program by running make:

```
    make
```


The program should compile without problems and three binaries (`doxygen` and `doxytag`) should be available in the bin directory of the distribution.
> 4. Optional: Generate the user manual.

```
    make docs
```


To let doxygen generate the HTML documentation.

You will need the stream editor `sed` for this, but this should be available on any Unix platform.


The HTML directory of the distribution will now contain the html documentation (just point a HTML browser to the file `index.html` in the html directory).
> 5. Optional: Generate a PDF version of the manual (you will need `pdflatex`, `makeindex`, and `egrep` for this).

```
    make pdf
```


The PDF manual `doxygen_manual.pdf` will be located in the latex directory of the distribution. Just view and print it via the acrobat reader.


# Installing the binaries on Unix #

After the compilation of the source code do a `make install` to install doxygen. If you downloaded the binary distribution for Unix, type:

```
    ./configure
    make install
```


Binaries are installed into the directory `<prefix>/bin`. Use `make install_docs` to install the documentation and examples into `<docdir>/doxygen`.

`<prefix>` defaults to `/usr/local` but can be changed with the `--prefix` option of the configure script. The default `<docdir>` directory is `<prefix>/share/doc/packages` and can be changed with the `--docdir` option of the configure script.

Alternatively, you can also copy the binaries from the `bin` directory manually to some `bin` directory in your search path. This is sufficient to use doxygen.

You need the GNU install tool for this to work (it is part of the coreutils package). Other install tools may put the binaries in the wrong directory!


If you have a RPM or DEP package, then please follow the standard installation procedure that is required for these packages.

# Known compilation problems for Unix #

**Qt problems**

The Qt include files and libraries are not a subdirectory of the directory pointed to by QTDIR on some systems (for instance on Red Hat 6.0 includes are in /usr/include/qt and libs are in /usr/lib).

The solution: go to the root of the doxygen distribution and do:
```
   mkdir qt
   cd qt
   ln -s your-qt-include-dir-here include
   ln -s your-qt-lib-dir-here lib
   export QTDIR=$PWD
```


If you have a csh-like shell you should use `setenv QTDIR $PWD` instead of the `export` command above.

Now install doxygen as described above.

**Bison problems**

Versions 1.31 to 1.34 of bison contain a "bug" that results in a compiler errors like this:

ce\_parse.cpp:348: member `class CPPValue yyalloc::yyvs' with constructor not allowed in union

This problem has been solved in version 1.35 (versions before 1.31 will also work).

**Latex problems**

The file `a4wide.sty` is not available for all distributions. If your distribution does not have it please select another paper type in the config file (see the PAPER\_TYPE  tag in the config file).

**HP-UX & Digital Unix problems**

If you are compiling for HP-UX with aCC and you get this error:
```
    /opt/aCC/lbin/ld: Unsatisfied symbols:
    alloca (code)
```
then you should (according to Anke Selig) edit `ce_parse.cpp` and replace
```
    extern "C" {
      void *alloca (unsigned int);
    };
```
with
```
    #include <alloca.h>  
```


If that does not help, try removing `ce_parse.cpp` and let bison rebuild it (this worked for me).

If you are compiling for Digital Unix, the same problem can be solved (according to Barnard Schmallhof) by replacing the following in ce\_parse.cpp:

```
    #else /* not GNU C.  */
    #if (!defined (__STDC__) && defined (sparc)) || defined (__sparc__) \
        || defined (__sparc) || defined (__sgi)
    #include <alloca.h>
```


with

```
    #else /* not GNU C.  */
    #if (!defined (__STDC__) && defined (sparc)) || defined (__sparc__) \
        || defined (__sparc) || defined (__sgi) || defined (__osf__)
    #include <alloca.h>
```


Alternatively, one could fix the problem at the bison side. Here is patch for bison.simple (provided by Andre Johansen):

```
--- bison.simple~       Tue Nov 18 11:45:53 1997
+++ bison.simple        Mon Jan 26 15:10:26 1998
@@ -27,7 +27,7 @@
 #ifdef __GNUC__
 #define alloca __builtin_alloca
 #else /* not GNU C.  */
-#if (!defined (__STDC__) && defined (sparc)) || defined (__sparc__) \
     || defined (__sparc) || defined (__sgi)
+#if (!defined (__STDC__) && defined (sparc)) || defined (__sparc__) \
     || defined (__sparc) || defined (__sgi) || defined (__alpha)
 #include <alloca.h>
 #else /* not sparc */
 #if defined (MSDOS) && !defined (__TURBOC__)
```


The generated scanner.cpp that comes with doxygen is build with this patch applied.

**Sun compiler problems**

It appears that doxygen doesn't work properly if it is compiled with Sun's C++ WorkShop Compiler. I cannot verify this myself as I do not have access to a Solaris machine with this compiler. With GNU compiler it does work.

when configuring with `--static` I got:

```
Undefined                       first referenced
 symbol                             in file
dlclose                             /usr/lib/libc.a(nss_deffinder.o)
dlsym                               /usr/lib/libc.a(nss_deffinder.o)
dlopen                              /usr/lib/libc.a(nss_deffinder.o)
```


Manually adding `-Bdynamic` after the target rule in `Makefile.doxygen` and `Makefile.doxytag` will fix this:

```
$(TARGET): $(OBJECTS) $(OBJMOC) 
        $(LINK) $(LFLAGS) -o $(TARGET) $(OBJECTS) $(OBJMOC) $(LIBS) -Bdynamic
```


**GCC compiler problems**

Older versions of the GNU compiler have problems with constant strings containing characters with character codes larger than 127. Therefore the compiler will fail to compile some of the translator\_xx.h files. A workaround, if you are planning to use the English translation only, is to configure doxygen with the `--english-only` option.

On some platforms (such as OpenBSD) using some versions of gcc with -O2 can lead to eating all memory during the compilation of files such as config.cpp. As a workaround use --debug as a configure option or omit the -O2 for the particular files in the Makefile.

Gcc versions before 2.95 may produce broken binaries due to bugs in these compilers.

**Dot problems**

Due to a change in the way image maps are generated, older versions of doxygen (<=1.2.17) will not work correctly with newer versions of graphviz (>=1.8.8). The effect of this incompatibility is that generated graphs in HTML are not properly clickable. For doxygen 1.3 it is recommended to use at least graphviz 1.8.10 or higher. For doxygen 1.4.7 or higher it is recommended to use GraphViz 2.8 or higher to avoid font issues.

**Red Hat 9.0 problems**

If you get the following error after running make
```
tmake error: qtools.pro:70: Syntax error
```
then first type
```
export LANG=
```
before running make.

# Compiling from source on Windows #

From version 1.5.0 onwards, build files are provided for Visual Studio 2005. Also the free "Express" version of Developer Studio can be used to compile doxygen. Alternatively, you can compile doxygen [the Unix way](Doxygen_install.md)  using [Cygwin](http://en.wikipedia.org/wiki/Cygwin) or [MinGW](http://www.mingw.org/).

Before you can compile doxygen you need to download and install the C++ compiler of Visual Studio. Since Microsoft apparently wants to lure everyone into using their .NET stuff, you need to [do some manual steps](http://msdn.microsoft.com/vstudio/express/visualc/usingpsdk/) in order to setup a proper working environment for building native win32 applications.

Once your environment is setup, you can [download](http://www.stack.nl/~dimitri/doxygen/download.html#latestsrc) the source distribution of doxygen and unpack it. If you don't have a tool like WinZip, then I suggest to download [unxutils](http://sourceforge.net/projects/unxutils/) and untar the archive from within a command box using
```
  tar zxvf doxygen-version.src.tar.gz
```
Inside the archive you will find a `winbuild` directory containing a `Doxygen.sln` file. Just open this file in Visual Studio. You can now build the Doxygen, Doxytag, and Doxywizard projects for Release or Debug to compile the executables.

Note that compiling Doxywizard currently requires a [commercial license for Qt 3](http://www.trolltech.com/products/qt/qt3).

Also read the next section for additional tools you may need to install.

# Installing the binaries on Windows #

Doxygen comes as a self-installing archive, so installation is extremely simple. Just follow the dialogs.

After installation it is recommended to also download and install GraphViz (version 2.8 or better is highly recommended). Doxygen can use the `dot` tool of the GraphViz package to render nicer diagrams, see the HAVE\_DOT  option in the configuration file.

If you want to produce compressed HTML files (see GENERATE\_HTMLHELP ) in the config file, then you need the Microsoft HTML help workshop. You can download it from [Microsoft](http://msdn.microsoft.com/library/default.asp?url=/library/en-us/htmlhelp/html/vsconHH1Start.asp).

In order to generate PDF output or use scientific formulas you will also need to install [LaTeX](http://en.wikipedia.org/wiki/LaTeX) and [Ghostscript](http://en.wikipedia.org/wiki/Ghostscript).

For LaTeX a number of distributions exists. Popular onces that should work with doxygen are [MikTex](http://www.miktex.org) and [XemTex](http://www.xemtex.org).

Ghostscript can be [downloaded](http://sourceforge.net/projects/ghostscript/) from Sourceforge.

After installing LaTeX and Ghostscript you'll need to make sure the tools latex.exe, pdflatex.exe, and gswin32c.exe are present in the search path of a command box. Follow [these](http://www.computerhope.com/issues/ch000549.htm) instructions if you are unsure and run the commands from a command box to verify it works.

# Tools used to develop doxygen #

Doxygen was developed and tested under Linux & MacOSX using the following open-source tools:
  * GCC version 3.3.6 (Linux) and 4.0.1 (MacOSX)
  * GNU flex version 2.5.33 (Linux) and 2.5.4 (MacOSX)
  * GNU bison version 1.75
  * GNU make version 3.80
  * Perl version 5.8.1
  * VIM version 6.2
  * Firefox 1.5
  * Troll Tech's tmake version 1.3 (included in the distribution)
  * teTeX version 2.0.2
  * CVS 1.12.12





---
| [Main Page](Doxygen.md) | [Files](Doxygen_files.md) |
|:------------------------|:--------------------------|