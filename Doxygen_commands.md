# Introduction #

All commands in the documentation start with a backslash (**\**) or an at-sign (**@**). If you prefer you can replace all commands starting with a backslash below by their counterparts that start with an at-sign.

Some commands have one or more arguments. Each argument has a certain range:
  * If 

&lt;sharp&gt;

 braces are used the argument is a single word.
  * If (round) braces are used the argument extends until the end of the line on which the command was found.
  * If {curly} braces are used the argument extends until the next paragraph. Paragraphs are delimited by a blank line or by a section indicator.
If [square](square.md) brackets are used the argument is optional.

Here is an alphabetically sorted list of all commands with references to their documentation: [\a](Doxygen_commands.md) [\addindex](Doxygen_commands.md) [\addtogroup](Doxygen_commands.md) [\anchor](Doxygen_commands.md) [\arg](Doxygen_commands.md) [\attention](Doxygen_commands.md) [\author](Doxygen_commands.md) [\b](Doxygen_commands.md) [\brief](Doxygen_commands.md) [\bug](Doxygen_commands.md) [\c](Doxygen_commands.md) [\callgraph](Doxygen_commands.md) [\callergraph](Doxygen_commands.md) [\category](Doxygen_commands.md) [\class](Doxygen_commands.md) [\code](Doxygen_commands.md) [\cond](Doxygen_commands.md) [\copydoc](Doxygen_commands.md) [\date](Doxygen_commands.md) [\def](Doxygen_commands.md) [\defgroup](Doxygen_commands.md) [\deprecated](Doxygen_commands.md) [\dir](Doxygen_commands.md) [\dontinclude](Doxygen_commands.md) [\dot](Doxygen_commands.md) [\dotfile](Doxygen_commands.md) [\e](Doxygen_commands.md) [\else](Doxygen_commands.md) [\elseif](Doxygen_commands.md) [\em](Doxygen_commands.md) [\endcode](Doxygen_commands.md) [\endcond](Doxygen_commands.md) [\enddot](Doxygen_commands.md) [\endhtmlonly](Doxygen_commands.md) [\endif](Doxygen_commands.md) [\endlatexonly](Doxygen_commands.md) [\endlink](Doxygen_commands.md) [\endmanonly](Doxygen_commands.md) [\endmsc](Doxygen_commands.md) [\endverbatim](Doxygen_commands.md) [\endxmlonly](Doxygen_commands.md) [\enum](Doxygen_commands.md) [\example](Doxygen_commands.md) [\exception](Doxygen_commands.md) [\f$](Doxygen_commands.md) [\f[](Doxygen_commands.md) [\f](Doxygen_commands.md)] [\file](Doxygen_commands.md) [\fn](Doxygen_commands.md) [\hideinitializer](Doxygen_commands.md) [\htmlinclude](Doxygen_commands.md) [\htmlonly](Doxygen_commands.md) [\if](Doxygen_commands.md) [\ifnot](Doxygen_commands.md) [\image](Doxygen_commands.md) [\include](Doxygen_commands.md) [\includelineno](Doxygen_commands.md) [\ingroup](Doxygen_commands.md) [\internal](Doxygen_commands.md) [\invariant](Doxygen_commands.md) [\interface](Doxygen_commands.md) [\latexonly](Doxygen_commands.md) [\li](Doxygen_commands.md) [\line](Doxygen_commands.md) [\link](Doxygen_commands.md) [\mainpage](Doxygen_commands.md) [\manonly](Doxygen_commands.md) [\msc](Doxygen_commands.md) [\n](Doxygen_commands.md) [\name](Doxygen_commands.md) [\namespace](Doxygen_commands.md) [\nosubgrouping](Doxygen_commands.md) [\note](Doxygen_commands.md) [\overload](Doxygen_commands.md) [\p](Doxygen_commands.md) [\package](Doxygen_commands.md) [\page](Doxygen_commands.md) [\par](Doxygen_commands.md) [\paragraph](Doxygen_commands.md) [\param](Doxygen_commands.md) [\post](Doxygen_commands.md) [\pre](Doxygen_commands.md) [\private (PHP only)](Doxygen_commands.md) [\privatesection (PHP only)](Doxygen_commands.md) [\property](Doxygen_commands.md) [\protected (PHP only)](Doxygen_commands.md) [\protectedsection (PHP only)](Doxygen_commands.md) [\protocol](Doxygen_commands.md) [\public (PHP only)](Doxygen_commands.md) [\publicsection (PHP only)](Doxygen_commands.md) [\ref](Doxygen_commands.md) [\relates](Doxygen_commands.md) [\relatesalso](Doxygen_commands.md) [\remarks](Doxygen_commands.md) [\return](Doxygen_commands.md) [\retval](Doxygen_commands.md) [\sa](Doxygen_commands.md) [\section](Doxygen_commands.md) [\see](Doxygen_commands.md) [\showinitializer](Doxygen_commands.md) [\since](Doxygen_commands.md) [\skip](Doxygen_commands.md) [\skipline](Doxygen_commands.md) [\struct](Doxygen_commands.md) [\subpage](Doxygen_commands.md) [\subsection](Doxygen_commands.md) [\subsubsection](Doxygen_commands.md) [\test](Doxygen_commands.md) [\throw](Doxygen_commands.md) [\todo](Doxygen_commands.md) [\typedef](Doxygen_commands.md) [\union](Doxygen_commands.md) [\until](Doxygen_commands.md) [\var](Doxygen_commands.md) [\verbatim](Doxygen_commands.md) [\verbinclude](Doxygen_commands.md) [\version](Doxygen_commands.md) [\warning](Doxygen_commands.md) [\weakgroup](Doxygen_commands.md) [\xmlonly](Doxygen_commands.md) [\xrefitem](Doxygen_commands.md) [\$](Doxygen_commands.md) [\@](Doxygen_commands.md) [\\](Doxygen_commands.md) [\&](Doxygen_commands.md) [\~](Doxygen_commands.md) [\<](Doxygen_commands.md) [\>](Doxygen_commands.md) [\#](Doxygen_commands.md) [\%](Doxygen_commands.md)

The following subsections provide a list of all commands that are recognized by doxygen. Unrecognized commands are treated as normal text.

# Structural indicators #


# \addtogroup 

&lt;name&gt;

 [(title)] #

Defines a group just like [\defgroup](Doxygen_commands.md) , but in contrast to that command using the same 

&lt;name&gt;

 more than once will not result in a warning, but rather one group with a merged documentation and the first title found in any of the commands.

The title is optional, so this command can also be used to add a number of entities to an existing group using @{ and @} like this:

```
  /*! \addtogroup mygrp
   *  Additional documentation for group `mygrp'
   *  @{
   */

  /*!
   *  A function 
   */
  void func1()
  {
  }

  /*! Another function */
  void func2()
  {
  }

  /*! @} */
```


page [Grouping](Doxygen_grouping.md) , sections [\defgroup](Doxygen_commands.md) , [\ingroup](Doxygen_commands.md)  and [\weakgroup](Doxygen_commands.md) .




# \callgraph #

When this command is put in a comment block of a function or method and HAVE\_DOT  is set to YES, then doxygen will generate a call graph for that function (provided the implementation of the function or method calls other documented functions). The call graph will generated regardless of the value of CALL\_GRAPH .

The completeness (and correctness) of the call graph depends on the doxygen code parser which is not perfect.




# \callergraph #

When this command is put in a comment block of a function or method and HAVE\_DOT  is set to YES, then doxygen will generate a caller graph for that function (provided the implementation of the function or method calls other documented functions). The caller graph will generated regardless of the value of CALLER\_GRAPH .

The completeness (and correctness) of the caller graph depends on the doxygen code parser which is not perfect.




# \category 

&lt;name&gt;

 [

&lt;header-file&gt;

] [

&lt;header-name&gt;

] #

For Objective-C only: Indicates that a comment block contains documentation for a class category with name 

&lt;name&gt;

. The arguments are equal to the \class command.

section [\class](Doxygen_commands.md) .




# \class 

&lt;name&gt;

 [

&lt;header-file&gt;

] [

&lt;header-name&gt;

] #

Indicates that a comment block contains documentation for a class with name 

&lt;name&gt;

. Optionally a header file and a header name can be specified. If the header-file is specified, a link to a verbatim copy of the header will be included in the HTML documentation. The 

&lt;header-name&gt;

 argument can be used to overwrite the name of the link that is used in the class documentation to something other than 

&lt;header-file&gt;

. This can be useful if the include name is not located on the default include path (like <X11/X.h>). With the 

&lt;header-name&gt;

 argument you can also specify how the include statement should look like, by adding either quotes or sharp brackets around the name. Sharp brackets are used if just the name is given.

# Example: #

```
```





# \def 

&lt;name&gt;

 #

Indicates that a comment block contains documentation for a `#define` macro.

# Example: #

```
```





# \defgroup 

&lt;name&gt;

 (group title) #

Indicates that a comment block contains documentation for a [group](Doxygen_grouping.md)  of classes, files or namespaces. This can be used to categorize classes, files or namespaces, and document those categories. You can also use groups as members of other groups, thus building a hierarchy of groups.

The 

&lt;name&gt;

 argument should be a single-word identifier.

page [Grouping](Doxygen_grouping.md) , sections [\ingroup](Doxygen_commands.md) , [\addtogroup](Doxygen_commands.md) , [\weakgroup](Doxygen_commands.md) .




# \dir [<path fragment>] #

Indicates that a comment block contains documentation for a directory. The "path fragment" argument should include the directory name and enough of the path to be unique w.r.t. the other directories in the project. The SHOW\_DIRECTORIES  option determines whether or not the directory information is shown and the STRIP\_FROM\_PATH  option determines what is stripped from the full path before it appears in the output.



# \enum 

&lt;name&gt;

 #

Indicates that a comment block contains documentation for an enumeration, with name 

&lt;name&gt;

. If the enum is a member of a class and the documentation block is located outside the class definition, the scope of the class should be specified as well. If a comment block is located directly in front of an enum declaration, the \enum comment may be omitted.

# Note: #

The type of an anonymous enum cannot be documented, but the values of an anonymous enum can.



# Example: #

```
```





# \example 

&lt;file-name&gt;

 #

Indicates that a comment block contains documentation for a source code example. The name of the source file is 

&lt;file-name&gt;

. The text of this file will be included in the documentation, just after the documentation contained in the comment block. All examples are placed in a list. The source code is scanned for documented members and classes. If any are found, the names are cross-referenced with the documentation. Source files or directories can be specified using the EXAMPLE\_PATH  tag of doxygen's configuration file.

If 

&lt;file-name&gt;

 itself is not unique for the set of example files specified by the EXAMPLE\_PATH  tag, you can include part of the absolute path to disambiguate it.

If more that one source file is needed for the example, the \include command can be used.

# Example: #

```
```
Where the example file `example_test.cpp` looks as follows:
```
```




section [\include](Doxygen_commands.md) .




# \file [

&lt;name&gt;

] #

Indicates that a comment block contains documentation for a source or header file with name 

&lt;name&gt;

. The file name may include (part of) the path if the file-name alone is not unique. If the file name is omitted (i.e. the line after \file is left blank) then the documentation block that contains the \file command will belong to the file it is located in.

# Important: #

The documentation of global functions, variables, typedefs, and enums will only be included in the output if the file they are in is documented as well.



# Example: #

```
```




In the above example JAVADOC\_AUTOBRIEF  has been set to YES in the configuration file.




# \fn (function declaration) #

Indicates that a comment block contains documentation for a function (either global or as a member of a class). This command is _only_ needed if a comment block is _not_ placed in front (or behind) the function declaration or definition.

If your comment block _is_ in front of the function declaration or definition this command can (and to avoid redundancy should) be omitted.

A full function declaration including arguments should be specified after the \fn command on a _single_ line, since the argument ends at the end of the line!

Do not use this command if it is not absolutely needed, since it will lead to duplication of information and thus to errors.



# Example: #

```
```




section [\var](Doxygen_commands.md)  and [\typedef](Doxygen_commands.md) .




# \hideinitializer #

By default the value of a define and the initializer of a variable are displayed unless they are longer than 30 lines. By putting this command in a comment block of a define or variable, the initializer is always hidden.

section [\showinitializer](Doxygen_commands.md) .




# \ingroup (

&lt;groupname&gt;

 [

&lt;groupname&gt;

 

&lt;groupname&gt;

]) #

If the \ingroup command is placed in a comment block of a class, file or namespace, then it will be added to the group or groups identified by 

&lt;groupname&gt;

.

page [Grouping](Doxygen_grouping.md) , sections [\defgroup](Doxygen_commands.md) , [\addtogroup](Doxygen_commands.md)  and [\weakgroup](Doxygen_commands.md)




# \interface 

&lt;name&gt;

 [

&lt;header-file&gt;

] [

&lt;header-name&gt;

] #

Indicates that a comment block contains documentation for an interface with name 

&lt;name&gt;

. The arguments are equal to the \class command.

section [\class](Doxygen_commands.md) .




# \internal #

This command writes the message `For internal use only' to the output and all text _after_ an `\internal` command until the end of the comment block or the end of the section (whichever comes first) is marked as "internal".

If the \internal command is put inside a section (see for example [\section](Doxygen_commands.md) ) all subsection after the command are considered to be internal as well. Only a new section at the same level will be visible again.

You can use INTERNAL\_DOCS  in the config file to show or hide the internal documentation.



# \mainpage [(title)] #


If the \mainpage command is placed in a comment block the block is used to customize the index page (in HTML) or the first chapter (in ![http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png](http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png) ).

The title argument is optional and replaces the default title that doxygen normally generates. If you do not want any title you can specify `notitle` as the argument of \mainpage.

Here is an example:
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


You can refer to the main page using \ref index (if the treeview is disabled, otherwise you should use \ref main).

section [\section](Doxygen_commands.md) , section [\subsection](Doxygen_commands.md)  and section [\page](Doxygen_commands.md) .




# \name (header) #

This command turns a comment block into a header definition of a member group. The comment block should be followed by a `//@{ ... //@}` block containing the members of the group.

See section [Member Groups](Doxygen_grouping.md)  for an example.



# \namespace 

&lt;name&gt;

 #

Indicates that a comment block contains documentation for a namespace with name 

&lt;name&gt;

.



# \nosubgrouping #

This command can be put in the documentation of a class. It can be used in combination with member grouping to avoid that doxygen puts a member group as a subgroup of a Public/Protected/Private/... section.



# \overload [(function declaration)] #

This command can be used to generate the following standard text for an overloaded member function:

`This is an overloaded member function, provided for convenience. It differs from the above function only in what argument(s) it accepts.'

If the documentation for the overloaded member function is not located in front of the function declaration or definition, the optional argument should be used to specify the correct function.

Any other documentation that is inside the documentation block will by appended after the generated message.

# Note 1: #

You are responsible that there is indeed an earlier documented member that is overloaded by this one. To prevent that document reorders the documentation you should set SORT\_MEMBER\_DOCS  to NO in this case.



# Note 2: #

The \overload command does not work inside a one-line comment.



# Example: #

```
```





# \package 

&lt;name&gt;

 #

Indicates that a comment block contains documentation for a Java package with name 

&lt;name&gt;

.



# \page 

&lt;name&gt;

 (title) #

Indicates that a comment block contains a piece of documentation that is not directly related to one specific class, file or member. The HTML generator creates a page containing the documentation. The ![http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png](http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png)  generator starts a new section in the chapter `Page documentation'.

# Example: #

```
```




# Note: #

The 

&lt;name&gt;

 argument consists of a combination of letters and number digits. If you wish to use upper case letters (e.g. `MYPAGE1`), or mixed case letters (e.g. `MyPage1`) in the 

&lt;name&gt;

 argument, you should set `CASE_SENSE_NAMES` to `YES`. However, this is advisable only if your file system is case sensitive. Otherwise (and for better portability) you should use all lower case letters (e.g. `mypage1`) for 

&lt;name&gt;

 in all references to the page.



section [\section](Doxygen_commands.md) , section [\subsection](Doxygen_commands.md) , and section [\ref](Doxygen_commands.md) .




# \property (qualified property name) #

Indicates that a comment block contains documentation for a property (either global or as a member of a class). This command is equivalent to \var and \fn.

section [\fn](Doxygen_commands.md)  and [\var](Doxygen_commands.md) .




# \protocol 

&lt;name&gt;

 [

&lt;header-file&gt;

] [

&lt;header-name&gt;

] #

Indicates that a comment block contains documentation for a protocol in Objective-C with name 

&lt;name&gt;

. The arguments are equal to the \class command.

section [\class](Doxygen_commands.md) .




# \relates 

&lt;name&gt;

 #

This command can be used in the documentation of a non-member function 

&lt;name&gt;

. It puts the function inside the `related function' section of the class documentation. This command is useful for documenting non-friend functions that are nevertheless strongly coupled to a certain class. It prevents the need of having to document a file, but only works for functions.

# Example: #

```
```





# \relatesalso 

&lt;name&gt;

 #

This command can be used in the documentation of a non-member function 

&lt;name&gt;

. It puts the function both inside the `related function' section of the class documentation as well as leaving its normal file documentation location. This command is useful for documenting non-friend functions that are nevertheless strongly coupled to a certain class. It only works for functions.



# \showinitializer #

By default the value of a define and the initializer of a variable are only displayed if they are less than 30 lines long. By putting this command in a comment block of a define or variable, the initializer is shown unconditionally.

section [\hideinitializer](Doxygen_commands.md) .




# \struct 

&lt;name&gt;

 [

&lt;header-file&gt;

] [

&lt;header-name&gt;

] #

Indicates that a comment block contains documentation for a struct with name 

&lt;name&gt;

. The arguments are equal to the \class command.

section [\class](Doxygen_commands.md) .




# \typedef (typedef declaration) #

Indicates that a comment block contains documentation for a typedef (either global or as a member of a class). This command is equivalent to \var and \fn.

section [\fn](Doxygen_commands.md)  and [\var](Doxygen_commands.md) .




# \union 

&lt;name&gt;

 [

&lt;header-file&gt;

] [

&lt;header-name&gt;

] #

Indicates that a comment block contains documentation for a union with name 

&lt;name&gt;

. The arguments are equal to the \class command.

section [\class](Doxygen_commands.md) .




# \var (variable declaration) #

Indicates that a comment block contains documentation for a variable or enum value (either global or as a member of a class). This command is equivalent to \typedef and \fn.

section [\fn](Doxygen_commands.md)  and [\typedef](Doxygen_commands.md) .




# \weakgroup 

&lt;name&gt;

 [(title)] #

Can be used exactly like [\addtogroup](Doxygen_commands.md) , but has a lower priority when it comes to resolving conflicting grouping definitions.

page [Grouping](Doxygen_grouping.md)  and [\addtogroup](Doxygen_commands.md) .




# Section indicators #




# \attention { attention text } #

Starts a paragraph where a message that needs attention may be entered. The paragraph will be indented. The text of the paragraph has no special internal structure. All visual enhancement commands may be used inside the paragraph. Multiple adjacent \attention commands will be joined into a single paragraph. The \attention command ends when a blank line or some other sectioning command is encountered.

# \author { list of authors } #

Starts a paragraph where one or more author names may be entered. The paragraph will be indented. The text of the paragraph has no special internal structure. All visual enhancement commands may be used inside the paragraph. Multiple adjacent \author commands will be joined into a single paragraph and separated by commas. Alternatively, one \author command may mention several authors. The \author command ends when a blank line or some other sectioning command is encountered.

# Example: #

```
```





# \brief {brief description} #

Starts a paragraph that serves as a brief description. For classes and files the brief description will be used in lists and at the start of the documentation page. For class and file members, the brief description will be placed at the declaration of the member and prepended to the detailed description. A brief description may span several lines (although it is advised to keep it brief!). A brief description ends when a blank line or another sectioning command is encountered. If multiple \brief commands are present they will be joined. See section [\author](Doxygen_commands.md)  for an example.

Synonymous to \short.



# \bug { bug description } #

Starts a paragraph where one or more bugs may be reported. The paragraph will be indented. The text of the paragraph has no special internal structure. All visual enhancement commands may be used inside the paragraph. Multiple adjacent \bug commands will be joined into a single paragraph. Each bug description will start on a new line. Alternatively, one \bug command may mention several bugs. The \bug command ends when a blank line or some other sectioning command is encountered. See section [\author](Doxygen_commands.md)  for an example.



# \cond [

&lt;section-label&gt;

] #

Starts a conditional section that ends with a corresponding [\endcond](Doxygen_commands.md)  command, which is typically found in another comment block. The main purpose of this pair of commands is to (conditionally) exclude part of a file from processing (traditionally this could only be achieved using C processor commands).

The section between \cond and \endcond commands can be included by adding its section label to the ENABLED\_SECTIONS  configuration option. If the section label is omitted, the section will be excluded from processing unconditionally.

For conditional sections within a comment block one should use a [\if](Doxygen_commands.md)  ... [\endif](Doxygen_commands.md)  block.

Conditional sections can be nested. In this case a nested section will only be shown if it and its containing section are included.

Here is an example showing the commands in action:

```
/** An interface */
class Intf
{
  public:
    /** A method */
    virtual void func() = 0;

    /// @cond TEST

    /** A method used for testing */
    virtual void test() = 0;

    /// @endcond
};

/// @cond DEV
/*
 *  The implementation of the interface 
 */
class Implementation : public Intf
{
  public:
    void func();

    /// @cond TEST
    void test();
    /// @endcond

    /// @cond
    /** This method is obsolete and does
     *  not show up in the documentation.
     */
    void obsolete();
    /// @endcond
};

/// @endcond 
```


The output will be different depending on whether `ENABLED_SECTIONS` is empty, `TEST`, `DEV`, or `DEV` `TEST`.



# \date { date description } #

Starts a paragraph where one or more dates may be entered. The paragraph will be indented. The text of the paragraph has no special internal structure. All visual enhancement commands may be used inside the paragraph. Multiple adjacent \date commands will be joined into a single paragraph. Each date description will start on a new line. Alternatively, one \date command may mention several dates. The \date command ends when a blank line or some other sectioning command is encountered. See section [\author](Doxygen_commands.md)  for an example.



# \deprecated { description } #

Starts a paragraph indicating that this documentation block belongs to a deprecated entity. Can be used to describe alternatives, expected life span, etc.



# \else #

Starts a conditional section if the previous conditional section was not enabled. The previous section should have been started with a `\if`, `\ifnot`, or `\elseif` command.

[\if](Doxygen_commands.md) , [\ifnot](Doxygen_commands.md) , [\elseif](Doxygen_commands.md) , [\endif.](Doxygen_commands.md)




# \elseif 

&lt;section-label&gt;

 #

Starts a conditional documentation section if the previous section was not enabled. A conditional section is disabled by default. To enable it you must put the section-label after the ENABLED\_SECTIONS  tag in the configuration file. Conditional blocks can be nested. A nested section is only enabled if all enclosing sections are enabled as well.

sections [\endif](Doxygen_commands.md) , [\ifnot](Doxygen_commands.md) , [\else](Doxygen_commands.md) , and [\elseif](Doxygen_commands.md) .




# \endcond #

Ends a conditional section that was started by [\cond](Doxygen_commands.md) .

[\cond](Doxygen_commands.md) .




# \endif #

Ends a conditional section that was started by `\if` or `\ifnot` For each `\if` or `\ifnot` one and only one matching `\endif` must follow.

[\if](Doxygen_commands.md) , and [\ifnot](Doxygen_commands.md) .




# \exception 

&lt;exception-object&gt;

 { exception description } #

Starts an exception description for an exception object with name 

&lt;exception-object&gt;

. Followed by a description of the exception. The existence of the exception object is not checked. The text of the paragraph has no special internal structure. All visual enhancement commands may be used inside the paragraph. Multiple adjacent \exception commands will be joined into a single paragraph. Each parameter description will start on a new line. The \exception description ends when a blank line or some other sectioning command is encountered. See section [\fn](Doxygen_commands.md)  for an example.

# Note: #

the tag \exceptions is a synonym for this tag.




# \if 

&lt;section-label&gt;

 #

Starts a conditional documentation section. The section ends with a matching `\endif` command. A conditional section is disabled by default. To enable it you must put the section-label after the ENABLED\_SECTIONS  tag in the configuration file. Conditional blocks can be nested. A nested section is only enabled if all enclosing sections are enabled as well.

# Example: #

```
  /*! Unconditionally shown documentation.
   *  \if Cond1
   *    Only included if Cond1 is set.
   *  \endif
   *  \if Cond2
   *    Only included if Cond2 is set.
   *    \if Cond3
   *      Only included if Cond2 and Cond3 are set.
   *    \endif
   *    More text.
   *  \endif
   *  Unconditional text.
   */
```



You can also use conditional commands inside aliases. To document a class in two languages you could for instance use:

# Example 2: #

```
/*! \english
 *  This is English.
 *  \endenglish
 *  \dutch
 *  Dit is Nederlands.
 *  \enddutch
 */
class Example
{
};
```



Where the following aliases are defined in the configuration file:

```
ALIASES  = "english=\if english" \
           "endenglish=\endif" \
           "dutch=\if dutch" \
           "enddutch=\endif"
```


and `ENABLED_SECTIONS` can be used to enable either `english` or `dutch`.

sections [\endif](Doxygen_commands.md) , [\ifnot](Doxygen_commands.md) , [\else](Doxygen_commands.md) , and [\elseif](Doxygen_commands.md) .




# \ifnot 

&lt;section-label&gt;

 #

Starts a conditional documentation section. The section ends with a matching `\endif` command. This conditional section is enabled by default. To disable it you must put the section-label after the ENABLED\_SECTIONS  tag in the configuration file.

sections [\endif](Doxygen_commands.md) , [\if](Doxygen_commands.md) , [\else](Doxygen_commands.md) , and [\elseif](Doxygen_commands.md) .




# \invariant { description of invariant } #

Starts a paragraph where the invariant of an entity can be described. The paragraph will be indented. The text of the paragraph has no special internal structure. All visual enhancement commands may be used inside the paragraph. Multiple adjacent \invariant commands will be joined into a single paragraph. Each invariant description will start on a new line. Alternatively, one \invariant command may mention several invariants. The \invariant command ends when a blank line or some other sectioning command is encountered.



# \note { text } #

Starts a paragraph where a note can be entered. The paragraph will be indented. The text of the paragraph has no special internal structure. All visual enhancement commands may be used inside the paragraph. Multiple adjacent \note commands will be joined into a single paragraph. Each note description will start on a new line. Alternatively, one \note command may mention several notes. The \note command ends when a blank line or some other sectioning command is encountered. See section [\par](Doxygen_commands.md)  for an example.



# \par [(paragraph title)] { paragraph } #

If a paragraph title is given this command starts a paragraph with a user defined heading. The heading extends until the end of the line. The paragraph following the command will be indented.

If no paragraph title is given this command will start a new paragraph. This will also work inside other paragraph commands (like \param or \warning) without ending the that command.

The text of the paragraph has no special internal structure. All visual enhancement commands may be used inside the paragraph. The \par command ends when a blank line or some other sectioning command is encountered.

# Example: #

```
```





# \param 

&lt;parameter-name&gt;

 { parameter description } #

Starts a parameter description for a function parameter with name 

&lt;parameter-name&gt;

. Followed by a description of the parameter. The existence of the parameter is checked and a warning is given if the documentation of this (or any other) parameter is missing or not present in the function declaration or definition.

The \param command has an optional attribute specifying the direction of the attribute. Possible values are "in" and "out". Here is an example for the function memcpy:
**/**! Copies bytes from a source memory area to a destination memory area, where both areas may not overlap. @param[out](out.md) dest The memory area to copy to. @param[in](in.md)  src  The memory area to copy from. @param[in](in.md)  n    The number of bytes to copy **/**
**void****memcpy(****void**dest, const void **src, size\_t n);**

If a parameter is both input and output, use [in,out] as an attribute.

The parameter description is a paragraph with no special internal structure. All visual enhancement commands may be used inside the paragraph.

Multiple adjacent \param commands will be joined into a single paragraph. Each parameter description will start on a new line. The \param description ends when a blank line or some other sectioning command is encountered. See section [\fn](Doxygen_commands.md)  for an example.



# \post { description of the postcondition } #

Starts a paragraph where the postcondition of an entity can be described. The paragraph will be indented. The text of the paragraph has no special internal structure. All visual enhancement commands may be used inside the paragraph. Multiple adjacent \post commands will be joined into a single paragraph. Each postcondition will start on a new line. Alternatively, one \post command may mention several postconditions. The \post command ends when a blank line or some other sectioning command is encountered.



# \pre { description of the precondition } #

Starts a paragraph where the precondition of an entity can be described. The paragraph will be indented. The text of the paragraph has no special internal structure. All visual enhancement commands may be used inside the paragraph. Multiple adjacent \pre commands will be joined into a single paragraph. Each precondition will start on a new line. Alternatively, one \pre command may mention several preconditions. The \pre command ends when a blank line or some other sectioning command is encountered.



# \remarks { remark text } #

Starts a paragraph where one or more remarks may be entered. The paragraph will be indented. The text of the paragraph has no special internal structure. All visual enhancement commands may be used inside the paragraph. Multiple adjacent \remark commands will be joined into a single paragraph. Each remark will start on a new line. Alternatively, one \remark command may mention several remarks. The \remark command ends when a blank line or some other sectioning command is encountered.



# \return { description of the return value } #

Starts a return value description for a function. The text of the paragraph has no special internal structure. All visual enhancement commands may be used inside the paragraph. Multiple adjacent \return commands will be joined into a single paragraph. The \return description ends when a blank line or some other sectioning command is encountered. See section [\fn](Doxygen_commands.md)  for an example.



# \retval <return value> { description } #

Starts a return value description for a function with name <return value>. Followed by a description of the return value. The text of the paragraph that forms the description has no special internal structure. All visual enhancement commands may be used inside the paragraph. Multiple adjacent \retval commands will be joined into a single paragraph. Each return value description will start on a new line. The \retval description ends when a blank line or some other sectioning command is encountered.



# \sa { references } #

Starts a paragraph where one or more cross-references to classes, functions, methods, variables, files or URL may be specified. Two names joined by either `::` or `#` are understood as referring to a class and one of its members. One of several overloaded methods or constructors may be selected by including a parenthesized list of argument types after the method name.

Synonymous to \see.

section [autolink](Doxygen_autolink.md)  for information on how to create links to objects.




# \see { references } #

Equivalent to [\sa](Doxygen_commands.md) . Introduced for compatibility with Javadoc.



# \since { text } #

This tag can be used to specify since when (version or time) an entity is available. The paragraph that follows \since does not have any special internal structure. All visual enhancement commands may be used inside the paragraph. The \since description ends when a blank line or some other sectioning command is encountered.



# \test { paragraph describing a test case } #

Starts a paragraph where a test case can be described. The description will also add the test case to a separate test list. The two instances of the description will be cross-referenced. Each test case in the test list will be preceded by a header that indicates the origin of the test case.



# \throw 

&lt;exception-object&gt;

 { exception description } #

Synonymous to \exception (see section [\exception](Doxygen_commands.md) ).

# Note: #

the tag \throws is a synonym for this tag.




# \todo { paragraph describing what is to be done } #

Starts a paragraph where a TODO item is described. The description will also add an item to a separate TODO list. The two instances of the description will be cross-referenced. Each item in the TODO list will be preceded by a header that indicates the origin of the item.



# \version { version number } #

Starts a paragraph where one or more version strings may be entered. The paragraph will be indented. The text of the paragraph has no special internal structure. All visual enhancement commands may be used inside the paragraph. Multiple adjacent \version commands will be joined into a single paragraph. Each version description will start on a new line. Alternatively, one \version command may mention several version strings. The \version command ends when a blank line or some other sectioning command is encountered. See section [\author](Doxygen_commands.md)  for an example.



# \warning { warning message } #

Starts a paragraph where one or more warning messages may be entered. The paragraph will be indented. The text of the paragraph has no special internal structure. All visual enhancement commands may be used inside the paragraph. Multiple adjacent \warning commands will be joined into a single paragraph. Each warning description will start on a new line. Alternatively, one \warning command may mention several warnings. The \warning command ends when a blank line or some other sectioning command is encountered. See section [\author](Doxygen_commands.md)  for an example.

# \xrefitem 

&lt;key&gt;

 "(heading)" "(list title)" {text} #

This command is a generalization of commands such as [\todo](Doxygen_commands.md)  and [\bug](Doxygen_commands.md) . It can be used to create user-defined text sections which are automatically cross-referenced between the place of occurrence and a related page, which will be generated. On the related page all sections of the same type will be collected.

The first argument 

&lt;key&gt;

 is a identifier uniquely representing the type of the section. The second argument is a quoted string representing the heading of the section under which text passed as the forth argument is put. The third argument (list title) is used as the title for the related page containing all items with the same key. The keys "todo", "test", "bug", and "deprecated" are predefined.

To get an idea on how to use the \xrefitem command and what its effect is, consider the todo list, which (for English output) can be seen an alias for the command
```
\xrefitem todo "Todo" "Todo List" 
```


Since it is very tedious and error-prone to repeat the first three parameters of the command for each section, the command is meant to be used in combination with the ALIASES  option in the configuration file. To define a new command \reminder, for instance, one should add the following line to the configuration file:
```
ALIASES += "reminder=\xrefitem reminders \"Reminder\" \"Reminders\"" 
```
Note the use of escaped quotes for the second and third argument of the \xrefitem command.

# Commands to create links #


# \addindex (text) #

This command adds (text) to the ![http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png](http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png)  index.



# \anchor 

&lt;word&gt;

 #

This command places an invisible, named anchor into the documentation to which you can refer with the \ref command.

Anchors can currently only be put into a comment block that is marked as a page (using [\page](Doxygen_commands.md) ) or mainpage ([\mainpage](Doxygen_commands.md) ).



section [\ref](Doxygen_commands.md) .




# \endlink #

This command ends a link that is started with the \link command.

section [\link](Doxygen_commands.md) .




# \link 

&lt;link-object&gt;

 #

The links that are automatically generated by doxygen always have the name of the object they point to as link-text.

The \link command can be used to create a link to an object (a file, class, or member) with a user specified link-text. The link command should end with an \endlink command. All text between the \link and \endlink commands serves as text for a link to the 

&lt;link-object&gt;

 specified as the first argument of \link.

See section [autolink](Doxygen_autolink.md)  for more information on automatically generated links and valid link-objects.



# \ref 

&lt;name&gt;

 ["(text)"] #

Creates a reference to a named section, subsection, page or anchor. For HTML documentation the reference command will generate a link to the section. For a sections or subsections the title of the section will be used as the text of the link. For anchor the optional text between quotes will be used or 

&lt;name&gt;

 if no text is specified. For ![http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png](http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png)  documentation the reference command will generate a section number for sections or the text followed by a page number if 

&lt;name&gt;

 refers to an anchor.

Section [\page](Doxygen_commands.md)  for an example of the \ref command.




# \subpage 

&lt;name&gt;

 ["(text)"] #

This command can be used to create a hierarchy of pages. The same structure can be made using the [\defgroup](Doxygen_commands.md)  and [\ingroup](Doxygen_commands.md)  commands, but for pages the \subpage command is often more convenient. The main page (see [\mainpage](Doxygen_commands.md) ) is typically the root of hierarchy.

This command behaves similar as [\ref](Doxygen_commands.md)  in the sense that it creates a reference to a page labeled 

&lt;name&gt;

 with the optional link text as specified in the second argument.

It differs from the \ref command in that it only works for pages, and creates a parent-child relation between pages, where the child page (or sub page) is identified by label 

&lt;name&gt;

.

See the [\section](Doxygen_commands.md)  and [\subsection](Doxygen_commands.md)  commands if you want to add structure without creating multiple pages.

Each page can be the sub page of only one other page and no cyclic relations are allowed, i.e. the page hierarchy must have a tree structure.


Here is an example:
```
/*! \mainpage A simple manual

Some general info.
  
This manual is divided in the following sections:
- \subpage intro 
- \subpage advanced "Advanced usage"
*/

//-----------------------------------------------------------

/*! \page intro Introduction
This page introduces the user to the topic.
Now you can proceed to the \ref advanced "advanced section".  
*/

//-----------------------------------------------------------

/*! \page advanced Advanced Usage
This page is for advanced users.
Make sure you have first read \ref intro "the introduction".
*/
```




# \section 

&lt;section-name&gt;

 (section title) #

Creates a section with name 

&lt;section-name&gt;

. The title of the section should be specified as the second argument of the \section command.

This command only works inside related page documentation and _not_ in other documentation blocks!




# \subsection 

&lt;subsection-name&gt;

 (subsection title) #

Creates a subsection with name 

&lt;subsection-name&gt;

. The title of the subsection should be specified as the second argument of the \subsection command.

This command only works inside a section of a related page documentation block and _not_ in other documentation blocks!



Section [\page](Doxygen_commands.md)  for an example of the [\subsection](Doxygen_commands.md)  command.




# \subsubsection 

&lt;subsubsection-name&gt;

 (subsubsection title) #

Creates a subsubsection with name 

&lt;subsubsection-name&gt;

. The title of the subsubsection should be specified as the second argument of the \subsubsection command.

This command only works inside a subsection of a related page documentation block and _not_ in other documentation blocks!



Section [\page](Doxygen_commands.md)  for an example of the [\subsubsection](Doxygen_commands.md)  command.




# \paragraph 

&lt;paragraph-name&gt;

 (paragraph title) #

Creates a named paragraph with name 

&lt;paragraph-name&gt;

. The title of the paragraph should be specified as the second argument of the \paragraph command.

This command only works inside a subsubsection of a related page documentation block and _not_ in other documentation blocks!



Section [\page](Doxygen_commands.md)  for an example of the [\paragraph](Doxygen_commands.md)  command.




# Commands for displaying examples #


# \dontinclude 

&lt;file-name&gt;

 #

This command can be used to parse a source file without actually verbatim including it in the documentation (as the \include command does). This is useful if you want to divide the source file into smaller pieces and add documentation between the pieces. Source files or directories can be specified using the EXAMPLE\_PATH  tag of doxygen's configuration file.

The class and member declarations and definitions inside the code fragment are `remembered' during the parsing of the comment block that contained the \dontinclude command.

For line by line descriptions of source files, one or more lines of the example can be displayed using the \line, \skip, \skipline, and \until commands. An internal pointer is used for these commands. The \dontinclude command sets the pointer to the first line of the example.

# Example: #

```
```
Where the example file `example_test.cpp` looks as follows:
```
```




sections [\line](Doxygen_commands.md) , [\skip](Doxygen_commands.md) , [\skipline](Doxygen_commands.md) , and [\until](Doxygen_commands.md) .




# \include 

&lt;file-name&gt;

 #

This command can be used to include a source file as a block of code. The command takes the name of an include file as an argument. Source files or directories can be specified using the EXAMPLE\_PATH  tag of doxygen's configuration file.

If 

&lt;file-name&gt;

 itself is not unique for the set of example files specified by the EXAMPLE\_PATH  tag, you can include part of the absolute path to disambiguate it.

Using the \include command is equivalent to inserting the file into the documentation block and surrounding it with [\code](Doxygen_commands.md)  and [\endcode](Doxygen_commands.md)  commands.

The main purpose of the \include command is to avoid code duplication in case of example blocks that consist of multiple source and header files.

For a line by line description of a source files use the [\dontinclude](Doxygen_commands.md)  command in combination with the [\line](Doxygen_commands.md) , [\skip](Doxygen_commands.md) , [\skipline](Doxygen_commands.md) , and \until commands.

Doxygen's special commands do not work inside blocks of code. It is allowed to nest C-style comments inside a code block though.



section [\example](Doxygen_commands.md) , [\dontinclude](Doxygen_commands.md) , and section [\verbatim](Doxygen_commands.md) .




# \includelineno 

&lt;file-name&gt;

 #

This command works the same way as \include, but will add line numbers to the included file.

section [\include](Doxygen_commands.md) .




# \line ( pattern ) #

This command searches line by line through the example that was last included using \include or \dontinclude until it finds a non-blank line. If that line contains the specified pattern, it is written to the output.

The internal pointer that is used to keep track of the current line in the example, is set to the start of the line following the non-blank line that was found (or to the end of the example if no such line could be found).

See section [\dontinclude](Doxygen_commands.md)  for an example.



# \skip ( pattern ) #

This command searches line by line through the example that was last included using \include or \dontinclude until it finds a line that contains the specified pattern.

The internal pointer that is used to keep track of the current line in the example, is set to the start of the line that contains the specified pattern (or to the end of the example if the pattern could not be found).

See section [\dontinclude](Doxygen_commands.md)  for an example.



# \skipline ( pattern ) #

This command searches line by line through the example that was last included using \include or \dontinclude until it finds a line that contains the specified pattern. It then writes the line to the output.

The internal pointer that is used to keep track of the current line in the example, is set to the start of the line following the line that is written (or to the end of the example if the pattern could not be found).

# Note: #

The command:
```
\skipline pattern
```
is equivalent to:
```
\skip pattern
\line pattern
```



See section [\dontinclude](Doxygen_commands.md)  for an example.



# \until ( pattern ) #

This command writes all lines of the example that was last included using \include or \dontinclude to the output, until it finds a line containing the specified pattern. The line containing the pattern will be written as well.

The internal pointer that is used to keep track of the current line in the example, is set to the start of the line following last written line (or to the end of the example if the pattern could not be found).

See section [\dontinclude](Doxygen_commands.md)  for an example.



# \verbinclude 

&lt;file-name&gt;

 #

This command includes the file 

&lt;file-name&gt;

 verbatim in the documentation. The command is equivalent to pasting the file in the documentation and placing \verbatim and \endverbatim commands around it.

Files or directories that doxygen should look for can be specified using the EXAMPLE\_PATH  tag of doxygen's configuration file.



# \htmlinclude 

&lt;file-name&gt;

 #

This command includes the file 

&lt;file-name&gt;

 as is in the HTML documentation. The command is equivalent to pasting the file in the documentation and placing \htmlonly and \endhtmlonly commands around it.

Files or directories that doxygen should look for can be specified using the EXAMPLE\_PATH  tag of doxygen's configuration file.

# Commands for visual enhancements #


# \a 

&lt;word&gt;

 #

Displays the argument 

&lt;word&gt;

 using a special font. Use this command to refer to member arguments in the running text.

# Example: #

```
  ... the \a x and \a y coordinates are used to ...
  
```
This will result in the following text:

... the _x_ and _y_ coordinates are used to ...




# \arg { item-description } #

This command has one argument that continues until the first blank line or until another \arg is encountered. The command can be used to generate a simple, not nested list of arguments. Each argument should start with a \arg command.

# Example: #

Typing:
```
  \arg \c AlignLeft left alignment.
  \arg \c AlignCenter center alignment.
  \arg \c AlignRight right alignment
  
  No other types of alignment are supported.
  
```
will result in the following text:


  * `AlignLeft` left alignment.
  * `AlignCenter` center alignment.
  * `AlignRight` right alignment

No other types of alignment are supported.



# Note: #

For nested lists, HTML commands should be used.


Equivalent to [\li](Doxygen_commands.md)



# \b 

&lt;word&gt;

 #

Displays the argument 

&lt;word&gt;

 using a bold font. Equivalent to <b>word</b>. To put multiple words in bold use <b>multiple words</b>.



# \c 

&lt;word&gt;

 #

Displays the argument 

&lt;word&gt;

 using a typewriter font. Use this to refer to a word of code. Equivalent to <tt>word</tt>.

# Example: #

Typing:
```
     ... This function returns \c void and not \c int ...
  
```
will result in the following text:

... This function returns `void` and not `int` ...


Equivalent to [\p](Doxygen_commands.md)  To have multiple words in typewriter font use <tt>multiple words</tt>.



# \code #

Starts a block of code. A code block is treated differently from ordinary text. It is interpreted as C/C++ code. The names of the classes and members that are documented are automatically replaced by links to the documentation.

section [\endcode](Doxygen_commands.md) , section [\verbatim](Doxygen_commands.md) .




# \copydoc 

&lt;link-object&gt;

 #

Copies a documentation block from the object specified by 

&lt;link-object&gt;

 and pastes it at the location of the command. This command can be useful to avoid cases where a documentation block would otherwise have to be duplicated or it can be used to extend the documentation of an inherited member.

The link object can point to a member (of a class, file or group), a class, a namespace, a group, a page, or a file (checked in that order). Note that if the object pointed to is a member (function, variable, typedef, etc), the compound (class, file, or group) containing it should also be documented for the copying to work.

To copy the documentation for a member of a class for instance one can put the following in the documentation

```
  /*! @copydoc MyClass::myfunction() 
   *  More documentation.
   */
```


if the member is overloaded, you should specify the argument types explicitly (without spaces!), like in the following:

```
  /*! @copydoc MyClass::myfunction(type1,type2) */
```


Qualified names are only needed if the context in which the documentation block is found requires them.

The copydoc command can be used recursively, but cycles in the copydoc relation will be broken and flagged as an error.



# \dot #

Starts a text fragment which should contain a valid description of a dot graph. The text fragment ends with [\enddot](Doxygen_commands.md) . Doxygen will pass the text on to dot and include the resulting image (and image map) into the output. The nodes of a graph can be made clickable by using the URL attribute. By using the command \ref inside the URL value you can conveniently link to an item inside doxygen. Here is an example:
**/**! class B **/**
**class****B {};**

**/**! class C **/**
**class****C {};**

**/**! \mainpage  Class relations expressed via an inline dot graph:  \dot  digraph example {      node [shape=record, fontname=Helvetica, fontsize=10];      b [label="class B" URL="\ref B"](.md);      c [label="class C" URL="\ref C"](.md);      b -> c [arrowhead="open", style="dashed" ](.md);  }  \enddot  Note that the classes in the above graph are clickable   (in the HTML output). **/**




# \msc #

Starts a text fragment which should contain a valid description of a message sequence chart. See [http://www.mcternan.me.uk/mscgen/](http://www.mcternan.me.uk/mscgen/) for examples. The text fragment ends with [\endmsc](Doxygen_commands.md) .

The text fragment should only include the part of the message sequence chart that is within the `msc {...}` block.

You need to install the `mscgen` tool, if you want to use this command.


Here is an example of the use of the \msc command.
**/****Sender class. Can be used to send a command to the server.**
**The receiver will acknowlegde the command by calling Ack().**
**\msc**
**Sender,Receiver;**
**Sender->Receiver [label="Command()", URL="\ref Receiver::Command()"];**
**Sender<-Receiver [label="Ack()", URL="\ref Ack()", ID="1"];**
**\endmsc**
/class Sender{  public:    / Acknowledgement from server **/**
**void****Ack(****bool****ok);**
**};**

**/****Receiver class. Can be used to receive and execute commands.**
**After execution of a command, the receiver will send an acknowledgement**
**\msc**
**Receiver,Sender;**
**Receiver<-Sender [label="Command()", URL="\ref Command()"];**
**Receiver->Sender [label="Ack()", URL="\ref Sender::Ack()", ID="1"];**
**\endmsc**
/class Receiver{  public:    / Executable a command on the server **/**
**void****Command(****int****commandId);**
**};**




# \dotfile 

&lt;file&gt;

 ["caption"] #

Inserts an image generated by dot from 

&lt;file&gt;

 into the documentation.

The first argument specifies the file name of the image. doxygen will look for files in the paths (or files) that you specified after the DOTFILE\_DIRS  tag. If the dot file is found it will be used as an input file to the dot tool. The resulting image will be put into the correct output directory. If the dot file name contains spaces you'll have to put quotes (") around it.

The second argument is optional and can be used to specify the caption that is displayed below the image. This argument has to be specified between quotes even if it does not contain any spaces. The quotes are stripped before the caption is displayed.



# \e 

&lt;word&gt;

 #

Displays the argument 

&lt;word&gt;

 in italics. Use this command to emphasize words.

# Example: #

Typing:
```
  ... this is a \e really good example ... 
  
```
will result in the following text:

... this is a _really_ good example ...


Equivalent to [\em](Doxygen_commands.md) . To emphasis multiple words use <em>multiple words</em>.



# \em 

&lt;word&gt;

 #

Displays the argument 

&lt;word&gt;

 in italics. Use this command to emphasize words.

# Example: #

Typing:
```
  ... this is a \em really good example ... 
  
```
will result in the following text:

... this is a _really_ good example ...


Equivalent to [\e](Doxygen_commands.md)



# \endcode #

Ends a block of code.

section [\code](Doxygen_commands.md)




# \enddot #

Ends a blocks that was started with [\dot](Doxygen_commands.md) .



# \endmsc #

Ends a blocks that was started with [\msc](Doxygen_commands.md) .



# \endhtmlonly #

Ends a block of text that was started with a \htmlonly command.

section [\htmlonly](Doxygen_commands.md) .




# \endlatexonly #

Ends a block of text that was started with a \latexonly command.

section [\latexonly](Doxygen_commands.md) .




# \endmanonly #

Ends a block of text that was started with a \manonly command.

section [\manonly](Doxygen_commands.md) .




# \endverbatim #

Ends a block of text that was started with a \verbatim command.

section [\endcode](Doxygen_commands.md) , section [\verbatim](Doxygen_commands.md) .




# \endxmlonly #

Ends a block of text that was started with a \xmlonly command.

section [\xmlonly](Doxygen_commands.md) .




# \f$ #


Marks the start and end of an in-text formula.

section [formulas](Doxygen_formulas.md)  for an example.




# \f[ #


Marks the start of a long formula that is displayed centered on a separate line.

section [\f](Doxygen_commands.md)]  and section [formulas](Doxygen_formulas.md) .




# \f] #


Marks the end of a long formula that is displayed centered on a separate line.

section [\f[](Doxygen_commands.md)  and section [formulas](Doxygen_formulas.md) .




# \htmlonly #

Starts a block of text that will be verbatim included in the generated HTML documentation only. The block ends with a endhtmlonly command.

This command can be used to include HTML code that is too complex for doxygen (i.e. applets, java-scripts, and HTML tags that require attributes). You can use the \latexonly and \endlatexonly pair to provide a proper ![http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png](http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png)  alternative.

**Note:** environment variables (like $(HOME) ) are resolved inside a HTML-only block.

section [\manonly](Doxygen_commands.md)  and section [\latexonly](Doxygen_commands.md) .




# \image 

&lt;format&gt;

 

&lt;file&gt;

 ["caption"] [

&lt;sizeindication&gt;

=

&lt;size&gt;

] #

Inserts an image into the documentation. This command is format specific, so if you want to insert an image for more than one format you'll have to repeat this command for each format.

The first argument specifies the output format. Currently, the following values are supported: `html` and `latex`.

The second argument specifies the file name of the image. doxygen will look for files in the paths (or files) that you specified after the IMAGE\_PATH  tag. If the image is found it will be copied to the correct output directory. If the image name contains spaces you'll have to put quotes (") around it. You can also specify an absolute URL instead of a file name, but then doxygen does not copy the image nor check its existance.

The third argument is optional and can be used to specify the caption that is displayed below the image. This argument has to be specified on a single line and between quotes even if it does not contain any spaces. The quotes are stripped before the caption is displayed.

The fourth argument is also optional and can be used to specify the width or height of the image. This is only useful for ![http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png](http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png)  output (i.e. format=`latex`). The `sizeindication` can be either `width` or `height`. The size should be a valid size specifier in ![http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png](http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png)  (for example `10cm` or `6in` or a symbolic width like `\textwidth`).

Here is example of a comment block:

```
  /*! Here is a snapshot of my new application:
   *  \image html application.jpg
   *  \image latex application.eps "My application" width=10cm
   */
```


And this is an example of how the relevant part of the configuration file may look:

```
  IMAGE_PATH     = my_image_dir
```


The image format for HTML is limited to what your browser supports. For ![http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png](http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png) , the image format must be Encapsulated PostScript (eps).

Doxygen does not check if the image is in the correct format. So _you_ have to make sure this is the case!




# \latexonly #

Starts a block of text that will be verbatim included in the generated ![http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png](http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png)  documentation only. The block ends with a endlatexonly command.

This command can be used to include ![http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png](http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png)  code that is too complex for doxygen (i.e. images, formulas, special characters). You can use the \htmlonly and \endhtmlonly pair to provide a proper HTML alternative.

**Note:** environment variables (like $(HOME) ) are resolved inside a ![http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png](http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png) -only block.

section [\latexonly](Doxygen_commands.md)  and section [\htmlonly](Doxygen_commands.md) .




# \manonly #

Starts a block of text that will be verbatim included in the generated MAN documentation only. The block ends with a endmanonly command.

This command can be used to include groff code directly into MAN pages. You can use the \htmlonly and \latexonly and \endhtmlonly and \endlatexonly pairs to provide proper HTML and ![http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png](http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png)  alternatives.

section [\htmlonly](Doxygen_commands.md)  and section [\latexonly](Doxygen_commands.md) .




# \li { item-description } #

This command has one argument that continues until the first blank line or until another \li is encountered. The command can be used to generate a simple, not nested list of arguments. Each argument should start with a \li command.

# Example: #

Typing:
```
  \li \c AlignLeft left alignment.
  \li \c AlignCenter center alignment.
  \li \c AlignRight right alignment
  
  No other types of alignment are supported.
  
```
will result in the following text:


  * `AlignLeft` left alignment.
  * `AlignCenter` center alignment.
  * `AlignRight` right alignment

No other types of alignment are supported.



# Note: #

For nested lists, HTML commands should be used.


Equivalent to [\arg](Doxygen_commands.md)



# \n #

Forces a new line. Equivalent to <br> and inspired by the printf function.<br>
<br>
<br>
<br>
<h1>\p <br>
<br>
<word><br>
<br>
</h1>

Displays the parameter <br>
<br>
<word><br>
<br>
 using a typewriter font. You can use this command to refer to member function parameters in the running text.<br>
<br>
<h1>Example:</h1>

<pre><code>  ... the \p x and \p y coordinates are used to ...<br>
  <br>
</code></pre>
This will result in the following text:<br>
<br>
... the <code>x</code> and <code>y</code> coordinates are used to ...<br>
<br>
<br>
Equivalent to <a href='Doxygen_commands.md'>\c</a>



<h1>\verbatim</h1>

Starts a block of text that will be verbatim included in both the HTML and the <img src='http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png' />  documentation. The block should end with a \endverbatim block. All commands are disabled in a verbatim block.<br>
<br>
Make sure you include a \endverbatim command for each \verbatim command or the parser will get confused!<br>
<br>
<br>
<br>
section <a href='Doxygen_commands.md'>\code</a> , and section <a href='Doxygen_commands.md'>\verbinclude</a> .<br>
<br>
<br>
<br>
<br>
<h1>\xmlonly</h1>

Starts a block of text that will be verbatim included in the generated XML output only. The block ends with a endxmlonly command.<br>
<br>
This command can be used to include custom XML tags.<br>
<br>
section <a href='Doxygen_commands.md'>\htmlonly</a>  and section <a href='Doxygen_commands.md'>\latexonly</a> .<br>
<br>
<br>
<br>
<br>
<h1>\\</h1>

This command writes a backslash character (\) to the HTML and <img src='http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png' />  output. The backslash has to be escaped in some cases because doxygen uses it to detect commands.<br>
<br>
<br>
<br>
<h1>\@</h1>

This command writes an at-sign (@) to the HTML and <img src='http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png' />  output. The at-sign has to be escaped in some cases because doxygen uses it to detect JavaDoc commands.<br>
<br>
<br>
<br>
<h1>\~<a href='LanguageId.md'>LanguageId</a></h1>

This command enables/disables a language specific filter. This can be used to put documentation for different language into one comment block and use the <code>OUTPUT_LANGUAGE</code> tag to filter out only a specific language. Use \~language_id to enable output for a specific language only and \~ to enable output for all languages (this is also the default mode).<br>
<br>
Example:<br>
<pre><code>/*! \~english This is english \~dutch Dit is Nederlands \~german Dieses ist<br>
    deutsch. \~ output for all languages.<br>
 */<br>
</code></pre>




<h1>\&</h1>

This command writes the & character to output. This character has to be escaped because it has a special meaning in HTML.<br>
<br>
<br>
<br>
<h1>\$</h1>

This command writes the $ character to the output. This character has to be escaped in some cases, because it is used to expand environment variables.<br>
<br>
<br>
<br>
<h1>\#</h1>

This command writes the # character to the output. This character has to be escaped in some cases, because it is used to refer to documented entities.<br>
<br>
<br>
<br>
<h1>\<</h1>

This command writes the < character to the output. This character has to be escaped because it has a special meaning in HTML.<br>
<br>
<br>
<br>
<h1>\></h1>

This command writes the > character to the output. This character has to be escaped because it has a special meaning in HTML.<br>
<br>
<h1>\%</h1>

This command writes the % character to the output. This character has to be escaped in some cases, because it is used to prevent auto-linking to word that is also a documented class or struct.<br>
<br>
<br>
<br>
<h1>PHP only commands</h1>

For PHP files there are a number of additional commands, that can be used inside classes to make members public, private, or protected even though the language itself doesn't support this notion.<br>
<br>
To mark a single item use one of \private, \protected, \public. For starting a section with a certain protection level use one of: \privatesection, \protectedsection, \publicsection. The latter commands are similar to "private:", "protected:", and "public:" in C++.<br>
<br>
<h1>Commands included for Qt compatibility</h1>




The following commands are supported to remain compatible to the Qt class browser generator. Do <i>not</i> use these commands in your own documentation.<br>
<ul><li>\annotatedclasslist<br>
</li><li>\classhierarchy<br>
</li><li>\define<br>
</li><li>\functionindex<br>
</li><li>\header<br>
</li><li>\headerfilelist<br>
</li><li>\inherit<br>
</li><li>\l<br>
</li><li>\postheader</li></ul>



---<br>
<table><thead><th> <a href='Doxygen.md'>Main Page</a> </th><th> <a href='Doxygen_files.md'>Files</a> </th></thead><tbody>