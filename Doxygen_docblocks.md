# Special documentation blocks #

A special documentation block is a C or C++ style comment block with some additional markings, so doxygen knows it is a piece of documentation that needs to end up in the generated documentation. For Python code there is a different comment convention, which can be found in section [Special documentation blocks in Python](Doxygen_docblocks.md)

For each code item there are two types of descriptions, which together form the documentation: a _brief_ description and _detailed_ description, both are optional. Having more than one brief or detailed description however, is not allowed.

As the name suggest, a brief description is a short one-liner, whereas the detailed description provides longer, more detailed documentation.

There are several ways to mark a comment block as a detailed description:
  1. You can use the JavaDoc style, which consist of a C-style comment block starting with two **'s, like this:**

```
/**
 * ... text ...
 */
```
> 2. or you can use the Qt style and add an exclamation mark (!) after the opening of a C-style comment block, as shown in this example:

```
/*!
 * ... text ...
 */
```


In both cases the intermediate **'s are optional, so**

```
/*!
 ... text ...
*/
```


is also valid.
> 3. A third alternative is to use a block of at least two C++ comment lines, where each line starts with an additional slash or an exclamation mark. Here are examples of the two cases:

```
///
/// ... text ...
///
```


or

```
//!
//!... text ...
//!
```
> 4. Some people like to make their comment blocks more visible in the documentation. For this purpose you can use the following:

```
/////////////////////////////////////////////////
/// ... text ...
/////////////////////////////////////////////////
```


For the brief description there are also several posibilities:
  1. One could use the [\brief](Doxygen_commands.md)  command with one of the above comment blocks. This command ends at the end of a paragraph, so the detailed description follows after an empty line.

Here is an example:

```
/*! \brief Brief description.
 *         Brief description continued.
 *
 *  Detailed description starts here.
 */
```
> 2. If JAVADOC\_AUTOBRIEF  is set to `YES` in the configuration file, then using JavaDoc style comment blocks will automatically start a brief description which ends at the first dot followed by a space or new line. Here is an example:

```
/** Brief description which ends at this dot. Details follow
 *  here.
 */
```
The option has the same effect for multi-line special C++ comments:
```
/// Brief description which ends at this dot. Details follow
/// here.
```
> 3. A third option is to use a special C++ style comment which does not span more than one line. Here are two examples:
```
/// Brief description.
/** Detailed description. */
```


or

```
//! Brief descripion.

//! Detailed description 
//! starts here.
```


Note the blank line in the last example, which is required to separate the brief description from the block containing the detailed description. The JAVADOC\_AUTOBRIEF  should also be set to `NO` for this case.


As you can see doxygen is quite flexible. The following however is not legal

```
//! Brief description, which is
//! really a detailed description since it spans multiple lines.
/*! Oops, another detailed description!
 */
```


because doxygen only allows one brief and one detailed description.

Furthermore, if there is one brief description before a declaration and one before a definition of a code item, only the one before the _declaration_ will be used. If the same situation occurs for a detailed description, the one before the _definition_ is preferred and the one before the declaration will be ignored.

Here is an example of a documented piece of C++ code using the Qt style:



The one-line comments contain a brief description, whereas the multi-line comment blocks contain a more detailed description.

The brief descriptions are included in the member overview of a class, namespace or file and are printed using a small italic font (this description can be hidden by setting BRIEF\_MEMBER\_DESC  to `NO` in the config file). By default the brief descriptions become the first sentence of the detailed descriptions (but this can be changed by setting the REPEAT\_BRIEF  tag to `NO`). Both the brief and the detailed descriptions are optional for the Qt style.

By default a JavaDoc style documentation block behaves the same way as a Qt style documentation block. This is not according the JavaDoc specification however, where the first sentence of the documentation block is automatically treated as a brief description. To enable this behaviour you should set JAVADOC\_AUTOBRIEF  to YES in the configuration file. If you enable this option and want to put a dot in the middle of a sentence without ending it, you should put a backslash and a space after it. Here is an example:
```
  /** Brief description (e.g.\ using only a few words). Details follow. */
```


Here is the same piece of code as shown above, this time documented using the JavaDoc style and JAVADOC\_AUTOBRIEF  set to YES:



Unlike most other documentation systems, doxygen also allows you to put the documentation of members (including global functions) in front of the _definition_. This way the documentation can be placed in the source file instead of the header file. This keeps the header file compact, and allows the implementer of the members more direct access to the documentation. As a compromise the brief description could be placed before the declaration and the detailed description before the member definition.

# Putting documentation after members #

If you want to document the members of a file, struct, union, class, or enum, and you want to put the documentation for these members inside the compound, it is sometimes desired to place the documentation block after the member instead of before. For this purpose you have to put an additional < marker in the comment block. Note that this also works for the parameters of a function.

Here are some examples:
```
int var; /*!< Detailed description after the member */
```
This block can be used to put a Qt style detailed documentation block _after_ a member. Other ways to do the same are:
```
int var; /**< Detailed description after the member */
```
or
```
int var; //!< Detailed description after the member
         //!< 
```
or
```
int var; ///< Detailed description after the member
         ///< 
```


Most often one only wants to put a brief description after a member. This is done as follows:
```
int var; //!< Brief description after the member
```
or
```
int var; ///< Brief description after the member
```


Note that these blocks have the same structure and meaning as the special comment blocks in the previous section only the < indicates that the member is located in front of the block instead of after the block.

Here is an example of the use of these comment blocks:



These blocks can only be used to document _members_ and _parameters_. They cannot be used to document files, classes, unions, structs, groups, namespaces and enums themselves. Furthermore, the structural commands mentioned in the next section (like `\class`) are ignored inside these comment blocks.




# Documentation at other places #

So far we have assumed that the documentation blocks are always located _in_ _front_ of the declaration or definition of a file, class or namespace or in front or after one of its members. Although this is often comfortable, there may sometimes be reasons to put the documentation somewhere else. For documenting a file this is even required since there is no such thing as "in front of a file".

Doxygen allows you to put your documentation blocks practically anywhere (the exception is inside the body of a function or inside a normal C style comment block).

The price you pay for not putting the documentation block directly before (or after) an item is the need to put a structural command inside the documentation block, which leads to some duplication of information. So in practice you should _avoid_ the use of structural commands _unless_ other requirements force you to do so.

Structural commands (like all other commands) start with a backslash (`\`), or an at-sign (`@`) if you prefer JavaDoc style, followed by a command name and one or more parameters. For instance, if you want to document the class `Test` in the example above, you could have also put the following documentation block somewhere in the input that is read by doxygen:
```
/*! \class Test
    \brief A test class.

    A more detailed class description.
*/
```


Here the special command `\class` is used to indicate that the comment block contains documentation for the class `Test`. Other structural commands are:
  * `\struct` to document a C-struct.
  * `\union` to document a union.
  * `\enum` to document an enumeration type.
  * `\fn` to document a function.
  * `\var` to document a variable or typedef or enum value.
  * `\def` to document a #define.
  * `\typedef` to document a type definition.
  * `\file` to document a file.
  * `\namespace` to document a namespace.
  * `\package` to document a Java package.
  * `\interface` to document an IDL interface.
See section [Special Commands](Doxygen_commands.md)  for detailed information about these and many other commands.

To document a member of a C++ class, you must also document the class itself. The same holds for namespaces. To document a global C function, typedef, enum or preprocessor definition you must first document the file that contains it (usually this will be a header file, because that file contains the information that is exported to other source files).

Let's repeat that, because it is often overlooked: to document global objects (functions, typedefs, enum, macros, etc), you _must_ document the file in which they are defined. In other words, there _must_ at least be a
```
/*! \file */ 
```
or a
```
/** @file */ 
```
line in this file.

Here is an example of a C header named `structcmd.h` that is documented using structural commands:



Because each comment block in the example above contains a structural command, all the comment blocks could be moved to another location or input file (the source file for instance), without affecting the generated documentation. The disadvantage of this approach is that prototypes are duplicated, so all changes have to be made twice! Because of this you should first consider if this is really needed, and avoid structural commands if possible. I often receive examples that contain \fn command in comment blocks which are place in front of a function. This is clearly a case where the \fn command is redundant and will only lead to problems.

# Special documentation blocks in Python #

For Python there is a standard way of documenting the code using so called documentation strings. Such strings are stored in `__doc__` and can be retrieved at runtime. Doxygen will extract such comments and assume they have to be represented in a preformatted way.




Note that in this case none of doxygen's [special commands](Doxygen_commands.md)  are supported.

There is also another way to document Python code using comments that start with "##". These type of comment blocks are more in line with the way documentation blocks work for the other languages supported by doxygen and this also allows the use of special commands.

Here is the same example again but now using doxygen style comments:




Since python looks more like Java than like C or C++, you should set OPTMIZE\_OUTPUT\_JAVA  to `YES` in the config file.




---
| [Main Page](Doxygen.md) | [Files](Doxygen_files.md) |
|:------------------------|:--------------------------|