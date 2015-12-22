Doxygen has three mechanisms to group things together. One mechanism works at a global level, creating a new page for each group. These groups are called ['modules'](Doxygen_grouping.md)  in the documentation. The second mechanism works within a member list of some compound entity, and is refered to as a ['member groups'](Doxygen_grouping.md) . For [pages](Doxygen_commands.md)  there is a third grouping mechanism referred to as [subpaging](Doxygen_grouping.md) .

# Modules #

Modules are a way to group things together on a separate page. You can document a group as a whole, as well as all individual members. Members of a group can be files, namespaces, classes, functions, variables, enums, typedefs, and defines, but also other groups.

To define a group, you should put the [\defgroup](Doxygen_commands.md)  command in a special comment block. The first argument of the command is a label that should uniquely identify the group. The second argument is the name or title of the group as it should appear in the documentation.

You can make an entity a member of a specific group by putting a [\ingroup](Doxygen_commands.md)  command inside its documentation block.

To avoid putting [\ingroup](Doxygen_commands.md)  commands in the documentation for each member you can also group members together by the open marker `@{` before the group and the closing marker `@}` after the group. The markers can be put in the documentation of the group definition or in a separate documentation block.

Groups themselves can also be nested using these grouping markers.

You will get an error message when you use the same group label more than once. If you don't want doxygen to enforce unique labels, then you can use [\addtogroup](Doxygen_commands.md)  instead of [\defgroup](Doxygen_commands.md) . It can be used exactly like [\defgroup](Doxygen_commands.md) , but when the group has been defined already, then it silently merges the existing documentation with the new one. The title of the group is optional for this command, so you can use
```
/** \addtogroup <label> */
/*\@{*/
/*\@}*/
```
to add additional members to a group that is defined in more detail elsewhere.

Note that compound entities (like classes, files and namespaces) can be put into multiple groups, but members (like variable, functions, typedefs and enums) can only be a member of one group (this restriction is in place to avoid ambiguous linking targets in case a member is not documented in the context of its class, namespace or file, but only visible as part of a group).

Doxygen will put members into the group whose definition has the highest "priority": e.g. An explicit [\ingroup](Doxygen_commands.md)  overrides an implicit grouping definition via `@{` `@}`. Conflicting grouping definitions with the same priority trigger a warning, unless one definition was for a member without any explicit documentation.

The following example puts VarInA into group A and silently resolves the conflict for IntegerVariable by putting it into group IntVariables, because the second instance of IntegerVariable is undocumented:

```
/**
 * \ingroup A
 */
extern int VarInA;

/**
 * \defgroup IntVariables Global integer variables
 */
/*@{*/

/** an integer variable */
extern int IntegerVariable;

/*@}*/

....

/**
 * \defgroup Variables Global variables
 */
/*@{*/

/** a variable in group A */
int VarInA;

int IntegerVariable;

/*@}*/
```


The [\ref](Doxygen_commands.md)  command can be used to refer to a group. The first argument of the \ref command should be group's label. To use a custom link name, you can put the name of the links in double quotes after the label, as shown by the following example
```
This is the \ref group_label "link" to this group.
```


The priorities of grouping definitions are (from highest to lowest): [\ingroup](Doxygen_commands.md) , [\defgroup](Doxygen_commands.md) , [\addtogroup](Doxygen_commands.md) , [\weakgroup](Doxygen_commands.md) . The last command is exactly like [\addtogroup](Doxygen_commands.md)  with a lower priority. It was added to allow "lazy" grouping definitions: you can use commands with a higher priority in your .h files to define the hierarchy and [\weakgroup](Doxygen_commands.md)  in .c files without having to duplicate the hierarchy exactly.

# Example: #

```
```





# Member Groups #

If a compound (e.g. a class or file) has many members, it is often desired to group them together. Doxygen already automatically groups things together on type and protection level, but maybe you feel that this is not enough or that that default grouping is wrong. For instance, because you feel that members of different (syntactic) types belong to the same (semantic) group.

A member group is defined by a
```
//@{ 
  ...
//@}
```
block or a
```
/*@{*/ 
  ... 
/*@}*/ 
```
block if you prefer C style comments. Note that the members of the group should be physcially inside the member group's body.

Before the opening marker of a block a separate comment block may be placed. This block should contain the [@name](Doxygen_commands.md)  (or [\name](Doxygen_commands.md) ) command and is used to specify the header of the group. Optionally, the comment block may also contain more detailed information about the group.

Nesting of member groups is not allowed.

If all members of a member group inside a class have the same type and protection level (for instance all are static public members), then the whole member group is displayed as a subgroup of the type/protection level group (the group is displayed as a subsection of the "Static Public Members" section for instance). If two or more members have different types, then the group is put at the same level as the automatically generated groups. If you want to force all member-groups of a class to be at the top level, you should put a [\nosubgrouping](Doxygen_commands.md)  command inside the documentation of the class.

# Example: #

```
```





Here Group1 is displayed as a subsection of the "Public Members". And Group2 is a separate section because it contains members with different protection levels (i.e. public and protected).


# Subpaging #

Information can be grouped into pages using the [\page](Doxygen_commands.md)  and [\mainpage](Doxygen_commands.md)  commands. Normally, this results in a flat list of pages, where the "main" page is the first in the list.

Instead of adding structure using the approach decribed in section [modules](Doxygen_grouping.md)  it is often more natural and convienent to add additional structure to the pages using the [\subpage](Doxygen_commands.md)  command.

For a page A the \subpage command adds a link to another page B and at the same time makes page B a subpage of A. This has the effect of making two groups GA and GB, where GB is part of GA, page A is put in group GA, and page B is put in group GB.




---
| [Main Page](Doxygen.md) | [Files](Doxygen_files.md) |
|:------------------------|:--------------------------|