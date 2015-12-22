Doxygen supports most of the XML commands that are typically used in C# code comments. The XML tags are defined in Appendix E of the [ECMA-334](http://www.ecma-international.org/publications/standards/Ecma-334.htm) standard, which defines the C# language. Unfortunately, the specification is not very precise and a number of the examples given are of poor quality.

Here is the list of tags supported by doxygen:

  * `<c>` Identifies inline text that should be rendered as a piece of code. Similar to using `<tt>`text`</tt>`.
  * `<code>` Set one or more lines of source code or program output. Note that this command behaves like `\code ... \endcode` for C# code, but it behaves like the HTML equivalent `<code>...</code>` for other languages.
  * `<description>` Part of a `<list>` command, describes an item.
  * `<example>` Marks a block of text as an example, ignored by doxygen.
  * `<exception cref="member">` Identifies the exception a method can throw.
  * `<include>` Can be used to import a piece of XML from an external file. Ignored by doxygen at the moment.
  * `<item>` List item. Can only be used inside a `<list>` context.
  * `<list type="type">` Starts a list, supported types are `bullet` or `number`. A list consists of a number of `<item>` tags.
  * `<para>` Identifies a paragraph of text.
  * `<param name="paramName">` Marks a piece of text as the documentation for parameter "paramName". Similar to using [\param](Doxygen_commands.md) .
  * `<paramref name="paramName">` Refers to a parameter with name "paramName". Similar to using [\a](Doxygen_commands.md) .
  * `<permission>` Identifies the security accessibility of a member. Ignored by doygen.
  * `<remarks>` Identifies the detailed description.
  * `<returns>` Marks a piece of text as the return value of a function or method. Similar to using [\return](Doxygen_commands.md) .
  * `<see cref="member">` Refers to a member. Similar to [\ref](Doxygen_commands.md) .
  * `<seealso cref="member">` Starts a "See also" section referring to "member". Similar to using [\sa](Doxygen_commands.md)  member.
  * `<summary>` Identifies the brief description. Similar to using [\brief](Doxygen_commands.md) .
  * `<value>` Identifies a property. Ignored by doxygen.


Here is an example of a typical piece of code using some of the above commands:

**///**

&lt;summary&gt;

/// A search engine./// 

&lt;/summary&gt;

class Engine{  /// 

&lt;summary&gt;

  /// The Search method takes a series of parameters to specify the search criterion  /// and returns a dataset containing the result set.  /// 

&lt;/summary&gt;

  /// 

&lt;param name="connectionString"&gt;

the connection string to connect to the  /// database holding the content to search

&lt;/param&gt;

  /// 

&lt;param name="maxRows"&gt;

The maximum number of rows to  /// return in the result set

&lt;/param&gt;

  /// 

&lt;param name="searchString"&gt;

The text that we are searching for

&lt;/param&gt;

  /// 

&lt;returns&gt;

A DataSet instance containing the matching rows. It contains a maximum  /// number of rows specified by the maxRows parameter

&lt;/returns&gt;

  public DataSet Search(string connectionString, int maxRows, int searchString)  {    DataSet ds = new DataSet();    return ds;  }}




---
| [Main Page](Doxygen.md) | [Files](Doxygen_files.md) |
|:------------------------|:--------------------------|