Doxygen is a command line based utility. Calling `doxygen` with the `--help` option at the command line will give you a brief description of the usage of the program.

All options consist of a leading character `-`, followed by one character and one or more arguments depending on the option.

To generate a manual for your project you typically need to follow these steps:
  1. You document your source code with special documentation blocks (see section [Special documentation blocks](Doxygen_docblocks.md) ).
> 2. You generate a configuration file (see section [Configuration](Doxygen_config.md) ) by calling doxygen with the `-g` option:
```
doxygen -g <config_file>
```
> 3. You edit the configuration file so it matches your project. In the configuration file you can specify the input files and a lot of optional information.
> 4. You let doxygen generate the documentation, based on the settings in the configuration file:
```
doxygen <config_file>
```


If you have a configuration file generated with an older version of doxygen, you can upgrade it to the current version by running doxygen with the -u option.
```
doxygen -u <config_file>
```
All configuration settings in the orginal configuration file will be copied to the new configuration file. Any new options will have their default value. Note that comments that you may have added in the original configuration file will be lost.

If you want to fine-tune the way the output looks, doxygen allows you generate default style sheet, header, and footer files that you can edit afterwards:
  * For HTML output, you can generate the default header file (see HTML\_HEADER ), the default footer (see HTML\_FOOTER ), and the default style sheet (see HTML\_STYLESHEET ), using the following command:
```
doxygen -w html header.html footer.html stylesheet.css
```
  * For LaTeX output, you can generate the first part of `refman.tex` (see LATEX\_HEADER ) and the style sheet included by that header (normally `doxygen.sty`), using:
```
doxygen -w latex header.tex doxygen.sty
```
If you need non-default options (for instance to use pdflatex) you need to make a config file with those options set correctly and then specify that config file as the forth argument.
  * For RTF output, you can generate the default style sheet file (see RTF\_STYLESHEET\_FILE ) using:
```
doxygen -w rtf rtfstyle.cfg
```


**Note:**

  * If you do not want documentation for each item inside the configuration file then you can use the optional `-s` option. This can use be used in combination with the `-u` option, to add or strip the documentation from an existing configuration file. Please use the `-s` option if you send me a configuration file as part of a bug report!
  * To make doxygen read/write to standard input/output instead of from/to a file, use `-` for the file name.



---
| [Main Page](Doxygen.md) | [Files](Doxygen_files.md) |
|:------------------------|:--------------------------|