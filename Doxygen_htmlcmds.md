Here is a list of all HTML commands that may be used inside the documentation. Note that although these HTML tags are translated to the proper commands for outer formats other than HTML, all attributes of a HTML tag are passed on to the HTML output only (the HREF and NAME attributes for the A tag are the only exception).

  * `<A HREF="...">` Starts a HTML hyper-link (HTML only).
  * `<A NAME="...">` Starts an named anchor (HTML only).
  * `</A>` Ends a link or anchor (HTML only).
  * `<B>` Starts a piece of text displayed in a bold font.
  * `</B>` Ends a `<B>` section.
  * `<BODY>` Does not generate any output.
  * `</BODY>` Does not generate any output.
  * `<BR>` Forces a line break.
  * `<CENTER>` starts a section of centered text.
  * `</CENTER>` ends a section of centered text.
  * `<CAPTION>` Starts a caption. Use within a table only.
  * `</CAPTION>` Ends a caption. Use within a table only.
  * `<CODE>` Starts a piece of text displayed in a typewriter font. Note that for C# code, this command is equivalent to [\code](Doxygen_commands.md) .
  * `</CODE>` End a `<CODE>` section. Note that for C# code, this command is equivalent to [\endcode](Doxygen_commands.md) .
  * `<DD>` Starts an item description.
  * `<DFN>` Starts a piece of text displayed in a typewriter font.
  * `</DFN>` Ends a `<DFN>` section.
  * `<DIV>` Starts a section with a specific style (HTML only)
  * `</DIV>` Ends a section with a specific style (HTML only)
  * `<DL>` Starts a description list.
  * `</DL>` Ends a description list.
  * `<DT>` Starts an item title.
  * `</DT>` Ends an item title.
  * `<EM>` Starts a piece of text displayed in an italic font.
  * `</EM>` Ends a `<EM>` section.
  * `<FORM>` Does not generate any output.
  * `</FORM>` Does not generate any output.
  * `<HR>` Writes a horizontal ruler.
  * `<H1>` Starts an unnumbered section.
  * `</H1>` Ends an unnumberd section.
  * `<H2>` Starts an unnumbered subsection.
  * `</H2>` Ends an unnumbered subsection.
  * `<H3>` Starts an unnumbered subsubsection.
  * `</H3>` Ends an unnumbered subsubsection.
  * `<I>` Starts a piece of text displayed in an italic font.
  * `<INPUT>` Does not generate any output.
  * `</I>` Ends a `<I>` section.
  * `<IMG>` This command is written with attributes to the HTML output only.
  * `<LI>` Starts a new list item.
  * `</LI>` Ends a list item.
  * `<META>` Does not generate any output.
  * `<MULTICOL>` ignored by doxygen.
  * `</MUTLICOL>` ignored by doxygen.
  * `<OL>` Starts a numbered item list.
  * `</OL>` Ends a numbered item list.
  * `<P>` Starts a new paragraph.
  * `</P>` Ends a paragraph.
  * `<PRE>` Starts a preformatted fragment.
  * `</PRE>` Ends a preformatted fragment.
  * `<SMALL>` Starts a section of text displayed in a smaller font.
  * `</SMALL>` Ends a `<SMALL>` section.
  * `<SPAN>` Starts an inline text fragment with a specific style (HTML only)
  * `</SPAN>` Ends an inline text fragment with a specific style (HTML only)
  * `<STRONG>` Starts a section of bold text.
  * `</STRONG>` Ends a section of bold text.
  * `<SUB>` Starts a piece of text displayed in subscript.
  * `</SUB>` Ends a `<SUB>` section.
  * `<SUP>` Starts a piece of text displayed in superscript.
  * `</SUP>` Ends a `</SUP>` section.
  * `<TABLE>` starts a table.
  * `</TABLE>` ends a table.
  * `<TD>` Starts a new table data element.
  * `</TD>` Ends a table data element.
  * `<TR>` Starts a new table row.
  * `</TR>` Ends a table row.
  * `<TT>` Starts a piece of text displayed in a typewriter font.
  * `</TT>` Ends a `<TT>` section.
  * `<KBD>` Starts a piece of text displayed in a typewriter font.
  * `</KBD>` Ends a `<KBD>` section.
  * `<UL>` Starts an unnumbered item list.
  * `</UL>` Ends an unnumbered item list.
  * `<VAR>` Starts a piece of text displayed in an italic font.
  * `</VAR>` Ends a `</VAR>` section.


The special HTML character entities that are recognized by Doxygen:

  * `&copy;` the copyright symbol
  * `&tm;` the trade mark symbol
  * `&reg;` the registered trade mark symbol
  * `&lt;` less-than symbol
  * `&gt;` greater-than symbol
  * `&amp;` ampersand
  * `&apos;` single quotation mark (straight)
  * `&quot;` double quotation mark (straight)
  * `&lsquo;` left single quotation mark
  * `&rsquo;` right single quotation mark
  * `&ldquo;` left double quotation mark
  * `&rdquo;` right double quotation mark
  * `&ndash;` n-dash (for numeric ranges, eg. 2–8)
  * `&mdash;` m-dash (for parenthetical punctuation — like this)
  * `&?uml;` where ? is one of {A,E,I,O,U,Y,a,e,i,o,u,y}, writes a character with a diaeresis accent (like ä).
  * `&?acute;` where ? is one of {A,E,I,O,U,Y,a,e,i,o,u,y}, writes a character with a acute accent (like á).
  * `&?grave;` where ? is one of {A,E,I,O,U,a,e,i,o,u,y}, writes a character with a grave accent (like à).
  * `&?circ;` where ? is one of {A,E,I,O,U,a,e,i,o,u,y}, writes a character with a circumflex accent (like â).
  * `&?tilde;` where ? is one of {A,N,O,a,n,o}, writes a character with a tilde accent (like ã).
  * `&szlig;` write a sharp s (i.e. ß) to the output.
  * `&?cedil;` where ? is one of {c,C}, writes a c-cedille (like ç).
  * `&?ring;` where ? is one of {a,A}, writes an `a` with a ring (like å).
  * `&nbsp;` a non breakable space.


Finally, to put invisible comments inside comment blocks, HTML style comments can be used:
```
/*! <!-- This is a comment with a comment block --> Visible text */
```



---
| [Main Page](Doxygen.md) | [Files](Doxygen_files.md) |
|:------------------------|:--------------------------|