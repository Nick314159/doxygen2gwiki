Most documentation systems have special `see also' sections where links to other pieces of documentation can be inserted. Although doxygen also has a command to start such a section (See section [\sa](Doxygen_commands.md) ), it does allow you to put these kind of links anywhere in the documentation. For ![http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png](http://doxygen2gwiki.googlecode.com/svn/wiki/Doxygen_form_0.png)  documentation a reference to the page number is written instead of a link. Furthermore, the index at the end of the document can be used to quickly find the documentation of a member, class, namespace or file. For man pages no reference information is generated.

The next sections show how to generate links to the various documented entities in a source file.

# Links to web pages and mail addresses #

Doxygen will automatically replace any URLs and mail addresses found in the documentation by links (in HTML).

# Links to classes. #

All words in the documentation that correspond to a documented class and contain at least one upper case character will automatically be replaced by a link to the page containing the documentation of the class. If you want to prevent that a word that corresponds to a documented class is replaced by a link you should put a % in front of the word.

# Links to files. #

All words that contain a dot (`.`) that is not the last character in the word are considered to be file names. If the word is indeed the name of a documented input file, a link will automatically be created to the documentation of that file.

# Links to functions. #

Links to functions are created if one of the following patterns is encountered:
  1. `<functionName>"("<argument-list>")"`
> 2. `<functionName>"()"`
> 3. `"::"<functionName>`
> 4. `(<className>"::")^n^<functionName>"("<argument-list>")"`
> 5. `(<className>"::")^n^<functionName>"("<argument-list>")"<modifiers>`
> 6. `(<className>"::")^n^<functionName>"()"`
> 7. `(<className>"::")^n^<functionName>`
where n>0.

# Note 1: #

Function arguments should be specified with correct types, i.e. 'fun(const std::string&,bool)' or '()' to match any prototype.



# Note 2: #

Member function modifiers (like 'const' and 'volatile') are required to identify the target, i.e. 'func(int) const' and 'fun(int)' target different member functions.



# Note 3: #

For JavaDoc compatibility a # may be used instead of a :: in the patterns above.



# Note 4: #

In the documentation of a class containing a member foo, a reference to a global variable is made using foo, whereas #foo will link to the member.


For non overloaded members the argument list may be omitted.

If a function is overloaded and no matching argument list is specified (i.e. pattern 2 or 5 is used), a link will be created to the documentation of one of the overloaded members.

For member functions the class scope (as used in patterns 4 to 6) may be omitted, if:
  1. The pattern points to a documented member that belongs to the same class as the documentation block that contains the pattern.
> 2. The class that corresponds to the documentation blocks that contains the pattern has a base class that contains a documented member that matches the pattern.


# Links to variables, typedefs, enum types, enum values and defines. #

All of these entities can be linked to in the same way as described in the previous section. For sake of clarity it is advised to only use patterns 3 and 6 in this case.

# Example: #

```
```





# typedefs. #

Typedefs that involve classes, structs and unions, like
```
typedef struct StructName TypeName
```
create an alias for StructName, so links will be generated to StructName, when either StructName itself or TypeName is encountered.

# Example: #

```
```






---
| [Main Page](Doxygen.md) | [Files](Doxygen_files.md) |
|:------------------------|:--------------------------|