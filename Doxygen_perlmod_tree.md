# Nodes in the documentation tree of the Perl Module output format. #


This is a description of the structure of the documentation tree in **DoxyDocs.pm**. Each item in the list below describes a node in the tree, and the format of the description is as follows:

  * [key => ](.md) **Name** _(type)_. Explanation of the content.


Where

  * The "key =&gt;" part only appears if the parent node is a hash. "key" is the key for this node.
  * **"Name"** is a unique name for the node, defined in DoxyModel.pm.
  * _"(type)"_ is the type of the node: "string" for string nodes, "hash" for hash nodes, "list" for list nodes, and "doc" for documentation subtrees. The structure of documentation subtrees is not described anywhere yet, but you can look for example at **doxylatex.pl** to see how to process it.


The meaning of each node in the documentation tree is as follows:
  * **Root** _(hash)_. Root node.
  * classes => **Classes** _(list)_. Documented classes.
  * **Class** _(hash)_. A documented class.
  * protected\_members => **ClassProtectedMembers** _(hash)_. Information about the protected members in the class.
  * members => **ClassProtectedMemberList** _(list)_. protected member list.
  * **ClassProtectedMember** _(hash)_. A protected member.
  * protection => **ClassProtectedMemberProtection** _(string)_. Protection of the protected member.
  * detailed => **ClassProtectedMemberDetailed** _(hash)_. Detailed information about the protected member.
  * doc => **ClassProtectedMemberDetailedDoc** _(doc)_. Detailed documentation for the protected member.
  * see => **ClassProtectedMemberSee** _(doc)_. "See also" documentation for the protected member.
  * kind => **ClassProtectedMemberKind** _(string)_. Kind of protected member (usually "variable").
  * name => **ClassProtectedMemberName** _(string)_. Name of the protected member.
  * type => **ClassProtectedMemberType** _(string)_. Data type of the protected member.
  * detailed => **ClassDetailed** _(hash)_. Detailed information about the class.
  * doc => **ClassDetailedDoc** _(doc)_. Detailed documentation block for the class.
  * protected\_typedefs => **ClassProtectedTypedefs** _(hash)_. Information about the protected typedefs in the class.
  * members => **ClassProtectedTypedefList** _(list)_. protected typedef list.
  * **ClassProtectedTypedef** _(hash)_. A protected typedef.
  * protection => **ClassProtectedTypedefProtection** _(string)_. Protection of the protected typedef.
  * detailed => **ClassProtectedTypedefDetailed** _(hash)_. Detailed information about the protected typedef.
  * doc => **ClassProtectedTypedefDetailedDoc** _(doc)_. Detailed documentation for the protected typedef.
  * see => **ClassProtectedTypedefSee** _(doc)_. "See also" documentation for the protected typedef.
  * kind => **ClassProtectedTypedefKind** _(string)_. Kind of protected typedef (usually "typedef").
  * name => **ClassProtectedTypedefName** _(string)_. Name of the protected typedef.
  * type => **ClassProtectedTypedefType** _(string)_. Data type of the protected typedef.
  * name => **ClassName** _(string)_. Name of the class.
  * private\_members => **ClassPrivateMembers** _(hash)_. Information about the private members in the class.
  * members => **ClassPrivateMemberList** _(list)_. private member list.
  * **ClassPrivateMember** _(hash)_. A private member.
  * protection => **ClassPrivateMemberProtection** _(string)_. Protection of the private member.
  * detailed => **ClassPrivateMemberDetailed** _(hash)_. Detailed information about the private member.
  * doc => **ClassPrivateMemberDetailedDoc** _(doc)_. Detailed documentation for the private member.
  * see => **ClassPrivateMemberSee** _(doc)_. "See also" documentation for the private member.
  * kind => **ClassPrivateMemberKind** _(string)_. Kind of private member (usually "variable").
  * name => **ClassPrivateMemberName** _(string)_. Name of the private member.
  * type => **ClassPrivateMemberType** _(string)_. Data type of the private member.
  * private\_typedefs => **ClassPrivateTypedefs** _(hash)_. Information about the private typedefs in the class.
  * members => **ClassPrivateTypedefList** _(list)_. private typedef list.
  * **ClassPrivateTypedef** _(hash)_. A private typedef.
  * protection => **ClassPrivateTypedefProtection** _(string)_. Protection of the private typedef.
  * detailed => **ClassPrivateTypedefDetailed** _(hash)_. Detailed information about the private typedef.
  * doc => **ClassPrivateTypedefDetailedDoc** _(doc)_. Detailed documentation for the private typedef.
  * see => **ClassPrivateTypedefSee** _(doc)_. "See also" documentation for the private typedef.
  * kind => **ClassPrivateTypedefKind** _(string)_. Kind of private typedef (usually "typedef").
  * name => **ClassPrivateTypedefName** _(string)_. Name of the private typedef.
  * type => **ClassPrivateTypedefType** _(string)_. Data type of the private typedef.
  * protected\_methods => **ClassProtectedMethods** _(hash)_. Information about the protected methods in the class.
  * members => **ClassProtectedMethodList** _(list)_. protected method list.
  * **ClassProtectedMethod** _(hash)_. A protected method.
  * parameters => **ClassProtectedMethodParams** _(list)_. List of the parameters of the protected method.
  * **ClassProtectedMethodParam** _(hash)_. A parameter of the protected method.
  * declaration\_name => **ClassProtectedMethodParamName** _(string)_. The name of the parameter.
  * type => **ClassProtectedMethodParamType** _(string)_. The data type of the parameter.
  * protection => **ClassProtectedMethodProtection** _(string)_. Protection of the protected method.
  * virtualness => **ClassProtectedMethodVirtualness** _(string)_. Virtualness of the protected method.
  * detailed => **ClassProtectedMethodDetailed** _(hash)_. Detailed information about the protected method.
  * params => **ClassProtectedMethodPDBlocks** _(list)_. List of parameter documentation blocks for the protected method.
  * **ClassProtectedMethodPDBlock** _(hash)_. A parameter documentation block for the protected method.
  * parameters => **ClassProtectedMethodPDParams** _(list)_. Parameter list for this parameter documentation block.
  * **ClassProtectedMethodPDParam** _(hash)_. A parameter documented by this documentation block.
  * name => **ClassProtectedMethodPDParamName** _(string)_. Name of the parameter.
  * doc => **ClassProtectedMethodPDDoc** _(doc)_. Documentation for this parameter documentation block.
  * doc => **ClassProtectedMethodDetailedDoc** _(doc)_. Detailed documentation for the protected method.
  * see => **ClassProtectedMethodSee** _(doc)_. "See also" documentation for the protected method.
  * return => **ClassProtectedMethodReturn** _(doc)_. Documentation about the return value of the protected method.
  * kind => **ClassProtectedMethodKind** _(string)_. Kind of protected method (usually "function").
  * name => **ClassProtectedMethodName** _(string)_. Name of the protected method.
  * type => **ClassProtectedMethodType** _(string)_. Data type returned by the protected method.
  * static => **ClassProtectedMethodStatic** _(string)_. Whether the protected method is static.
  * public\_typedefs => **ClassPublicTypedefs** _(hash)_. Information about the public typedefs in the class.
  * members => **ClassPublicTypedefList** _(list)_. public typedef list.
  * **ClassPublicTypedef** _(hash)_. A public typedef.
  * protection => **ClassPublicTypedefProtection** _(string)_. Protection of the public typedef.
  * detailed => **ClassPublicTypedefDetailed** _(hash)_. Detailed information about the public typedef.
  * doc => **ClassPublicTypedefDetailedDoc** _(doc)_. Detailed documentation for the public typedef.
  * see => **ClassPublicTypedefSee** _(doc)_. "See also" documentation for the public typedef.
  * kind => **ClassPublicTypedefKind** _(string)_. Kind of public typedef (usually "typedef").
  * name => **ClassPublicTypedefName** _(string)_. Name of the public typedef.
  * type => **ClassPublicTypedefType** _(string)_. Data type of the public typedef.
  * public\_members => **ClassPublicMembers** _(hash)_. Information about the public members in the class.
  * members => **ClassPublicMemberList** _(list)_. public member list.
  * **ClassPublicMember** _(hash)_. A public member.
  * protection => **ClassPublicMemberProtection** _(string)_. Protection of the public member.
  * detailed => **ClassPublicMemberDetailed** _(hash)_. Detailed information about the public member.
  * doc => **ClassPublicMemberDetailedDoc** _(doc)_. Detailed documentation for the public member.
  * see => **ClassPublicMemberSee** _(doc)_. "See also" documentation for the public member.
  * kind => **ClassPublicMemberKind** _(string)_. Kind of public member (usually "variable").
  * name => **ClassPublicMemberName** _(string)_. Name of the public member.
  * type => **ClassPublicMemberType** _(string)_. Data type of the public member.
  * private\_methods => **ClassPrivateMethods** _(hash)_. Information about the private methods in the class.
  * members => **ClassPrivateMethodList** _(list)_. private method list.
  * **ClassPrivateMethod** _(hash)_. A private method.
  * parameters => **ClassPrivateMethodParams** _(list)_. List of the parameters of the private method.
  * **ClassPrivateMethodParam** _(hash)_. A parameter of the private method.
  * declaration\_name => **ClassPrivateMethodParamName** _(string)_. The name of the parameter.
  * type => **ClassPrivateMethodParamType** _(string)_. The data type of the parameter.
  * protection => **ClassPrivateMethodProtection** _(string)_. Protection of the private method.
  * virtualness => **ClassPrivateMethodVirtualness** _(string)_. Virtualness of the private method.
  * detailed => **ClassPrivateMethodDetailed** _(hash)_. Detailed information about the private method.
  * params => **ClassPrivateMethodPDBlocks** _(list)_. List of parameter documentation blocks for the private method.
  * **ClassPrivateMethodPDBlock** _(hash)_. A parameter documentation block for the private method.
  * parameters => **ClassPrivateMethodPDParams** _(list)_. Parameter list for this parameter documentation block.
  * **ClassPrivateMethodPDParam** _(hash)_. A parameter documented by this documentation block.
  * name => **ClassPrivateMethodPDParamName** _(string)_. Name of the parameter.
  * doc => **ClassPrivateMethodPDDoc** _(doc)_. Documentation for this parameter documentation block.
  * doc => **ClassPrivateMethodDetailedDoc** _(doc)_. Detailed documentation for the private method.
  * see => **ClassPrivateMethodSee** _(doc)_. "See also" documentation for the private method.
  * return => **ClassPrivateMethodReturn** _(doc)_. Documentation about the return value of the private method.
  * kind => **ClassPrivateMethodKind** _(string)_. Kind of private method (usually "function").
  * name => **ClassPrivateMethodName** _(string)_. Name of the private method.
  * type => **ClassPrivateMethodType** _(string)_. Data type returned by the private method.
  * static => **ClassPrivateMethodStatic** _(string)_. Whether the private method is static.
  * public\_methods => **ClassPublicMethods** _(hash)_. Information about the public methods in the class.
  * members => **ClassPublicMethodList** _(list)_. public method list.
  * **ClassPublicMethod** _(hash)_. A public method.
  * parameters => **ClassPublicMethodParams** _(list)_. List of the parameters of the public method.
  * **ClassPublicMethodParam** _(hash)_. A parameter of the public method.
  * declaration\_name => **ClassPublicMethodParamName** _(string)_. The name of the parameter.
  * type => **ClassPublicMethodParamType** _(string)_. The data type of the parameter.
  * protection => **ClassPublicMethodProtection** _(string)_. Protection of the public method.
  * virtualness => **ClassPublicMethodVirtualness** _(string)_. Virtualness of the public method.
  * detailed => **ClassPublicMethodDetailed** _(hash)_. Detailed information about the public method.
  * params => **ClassPublicMethodPDBlocks** _(list)_. List of parameter documentation blocks for the public method.
  * **ClassPublicMethodPDBlock** _(hash)_. A parameter documentation block for the public method.
  * parameters => **ClassPublicMethodPDParams** _(list)_. Parameter list for this parameter documentation block.
  * **ClassPublicMethodPDParam** _(hash)_. A parameter documented by this documentation block.
  * name => **ClassPublicMethodPDParamName** _(string)_. Name of the parameter.
  * doc => **ClassPublicMethodPDDoc** _(doc)_. Documentation for this parameter documentation block.
  * doc => **ClassPublicMethodDetailedDoc** _(doc)_. Detailed documentation for the public method.
  * see => **ClassPublicMethodSee** _(doc)_. "See also" documentation for the public method.
  * return => **ClassPublicMethodReturn** _(doc)_. Documentation about the return value of the public method.
  * kind => **ClassPublicMethodKind** _(string)_. Kind of public method (usually "function").
  * name => **ClassPublicMethodName** _(string)_. Name of the public method.
  * type => **ClassPublicMethodType** _(string)_. Data type returned by the public method.
  * static => **ClassPublicMethodStatic** _(string)_. Whether the public method is static.
  * files => **Files** _(list)_. Documented files.
  * **File** _(hash)_. A documented file.
  * detailed => **FileDetailed** _(hash)_. Detailed information about the file.
  * doc => **FileDetailedDoc** _(doc)_. Detailed documentation block for the file.
  * functions => **FileFunctions** _(hash)_. Information about the functions in the file.
  * members => **FileFunctionList** _(list)_. function list.
  * **FileFunction** _(hash)_. A function.
  * parameters => **FileFunctionParams** _(list)_. List of the parameters of the function.
  * **FileFunctionParam** _(hash)_. A parameter of the function.
  * declaration\_name => **FileFunctionParamName** _(string)_. The name of the parameter.
  * type => **FileFunctionParamType** _(string)_. The data type of the parameter.
  * protection => **FileFunctionProtection** _(string)_. Protection of the function.
  * virtualness => **FileFunctionVirtualness** _(string)_. Virtualness of the function.
  * detailed => **FileFunctionDetailed** _(hash)_. Detailed information about the function.
  * params => **FileFunctionPDBlocks** _(list)_. List of parameter documentation blocks for the function.
  * **FileFunctionPDBlock** _(hash)_. A parameter documentation block for the function.
  * parameters => **FileFunctionPDParams** _(list)_. Parameter list for this parameter documentation block.
  * **FileFunctionPDParam** _(hash)_. A parameter documented by this documentation block.
  * name => **FileFunctionPDParamName** _(string)_. Name of the parameter.
  * doc => **FileFunctionPDDoc** _(doc)_. Documentation for this parameter documentation block.
  * doc => **FileFunctionDetailedDoc** _(doc)_. Detailed documentation for the function.
  * see => **FileFunctionSee** _(doc)_. "See also" documentation for the function.
  * return => **FileFunctionReturn** _(doc)_. Documentation about the return value of the function.
  * kind => **FileFunctionKind** _(string)_. Kind of function (usually "function").
  * name => **FileFunctionName** _(string)_. Name of the function.
  * type => **FileFunctionType** _(string)_. Data type returned by the function.
  * static => **FileFunctionStatic** _(string)_. Whether the function is static.
  * name => **FileName** _(string)_. Name of the file.
  * variables => **FileVariables** _(hash)_. Information about the variables in the file.
  * members => **FileVariableList** _(list)_. variable list.
  * **FileVariable** _(hash)_. A variable.
  * protection => **FileVariableProtection** _(string)_. Protection of the variable.
  * detailed => **FileVariableDetailed** _(hash)_. Detailed information about the variable.
  * doc => **FileVariableDetailedDoc** _(doc)_. Detailed documentation for the variable.
  * see => **FileVariableSee** _(doc)_. "See also" documentation for the variable.
  * kind => **FileVariableKind** _(string)_. Kind of variable (usually "variable").
  * name => **FileVariableName** _(string)_. Name of the variable.
  * type => **FileVariableType** _(string)_. Data type of the variable.
  * typedefs => **FileTypedefs** _(hash)_. Information about the typedefs in the file.
  * members => **FileTypedefList** _(list)_. typedef list.
  * **FileTypedef** _(hash)_. A typedef.
  * protection => **FileTypedefProtection** _(string)_. Protection of the typedef.
  * detailed => **FileTypedefDetailed** _(hash)_. Detailed information about the typedef.
  * doc => **FileTypedefDetailedDoc** _(doc)_. Detailed documentation for the typedef.
  * see => **FileTypedefSee** _(doc)_. "See also" documentation for the typedef.
  * kind => **FileTypedefKind** _(string)_. Kind of typedef (usually "typedef").
  * name => **FileTypedefName** _(string)_. Name of the typedef.
  * type => **FileTypedefType** _(string)_. Data type of the typedef.



---
| [Main Page](Doxygen.md) | [Files](Doxygen_files.md) |
|:------------------------|:--------------------------|