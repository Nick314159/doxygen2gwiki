Source files that are used as input to doxygen can be parsed by doxygen's built-in C-preprocessor.

By default doxygen does only partial preprocessing. That is, it evaluates conditional compilation statements (like #if) and evaluates macro definitions, but it does not perform macro expansion.

So if you have the following code fragment
```
#define VERSION 200
#define CONST_STRING const char *

#if VERSION >= 200
  static CONST_STRING version = "2.xx";
#else
  static CONST_STRING version = "1.xx";
#endif
```


Then by default doxygen will feed the following to its parser:

```
#define VERSION
#define CONST_STRING

  static CONST_STRING version = "2.xx";
```


You can disable all preprocessing by setting ENABLE\_PREPROCESSING  to `NO` in the configuation file. In the case above doxygen will then read both statements, i.e:

```
  static CONST_STRING version = "2.xx";
  static CONST_STRING version = "1.xx";
```


In case you want to expand the `CONST_STRING` macro, you should set the MACRO\_EXPANSION  tag in the config file to `YES`. Then the result after preprocessing becomes:

```
#define VERSION
#define CONST_STRING

  static const char * version = "1.xx";
```


Note that doxygen will now expand _all_ macro definitions (recursively if needed). This is often too much. Therefore, doxygen also allows you to expand only those defines that you explicitly specify. For this you have to set the EXPAND\_ONLY\_PREDEF  tag to `YES` and specify the macro definitions after the PREDEFINED  or EXPAND\_AS\_DEFINED  tag.

A typically example where some help from the preprocessor is needed is when dealing with Microsoft's declspec language extension. Here is an example function.

```
extern "C" void __declspec(dllexport) ErrorMsg( String aMessage,...);
```


When nothing is done, doxygen will be confused and see declspec as some sort of function. To help doxygen one typically uses the following preprocessor settings:

```
ENABLE_PREPROCESSING   = YES
MACRO_EXPANSION        = YES
EXPAND_ONLY_PREDEF     = YES
PREDEFINED             = __declspec(x)=
```


This will make sure the declspec(dllexport) is removed before doxygen parses the source code.

For a more complex example, suppose you have the following obfuscated code fragment of an abstract base class called `IUnknown:`

```
/*! A reference to an IID */
#ifdef __cplusplus
#define REFIID const IID &
#else
#define REFIID const IID *
#endif


/*! The IUnknown interface */
DECLARE_INTERFACE(IUnknown)
{
  STDMETHOD(HRESULT,QueryInterface) (THIS_ REFIID iid, void **ppv) PURE;
  STDMETHOD(ULONG,AddRef) (THIS) PURE;
  STDMETHOD(ULONG,Release) (THIS) PURE;
};
```


without macro expansion doxygen will get confused, but we may not want to expand the REFIID macro, because it is documented and the user that reads the documentation should use it when implementing the interface.

By setting the following in the config file:

```
ENABLE_PREPROCESSING = YES
MACRO_EXPANSION      = YES
EXPAND_ONLY_PREDEF   = YES
PREDEFINED           = "DECLARE_INTERFACE(name)=class name" \
                       "STDMETHOD(result,name)=virtual result name" \
                       "PURE= = 0" \
                       THIS_= \
                       THIS= \
		       __cplusplus
```


we can make sure that the proper result is fed to doxygen's parser:
```
/*! A reference to an IID */
#define REFIID

/*! The IUnknown interface */
class  IUnknown
{
  virtual  HRESULT   QueryInterface ( REFIID iid, void **ppv) = 0;
  virtual  ULONG   AddRef () = 0;
  virtual  ULONG   Release () = 0;
};
```


Note that the PREDEFINED  tag accepts function like macro definitions (like `DECLARE_INTERFACE` ), normal macro substitutions (like `PURE` and `THIS`) and plain defines (like `__cplusplus`).

Note also that preprocessor definitions that are normally defined automatically by the preprocessor (like `__cplusplus`), have to be defined by hand with doxygen's parser (this is done because these defines are often platform/compiler specific).

In some cases you may want to substitute a macro name or function by something else without exposing the result to further macro substitution. You can do this but using the `:=` operator instead of `=`

As an example suppose we have the following piece of code:
```
#define QList QListT
class QListT
{
};
```


Then the only way to get doxygen interpret this as a class definition for class QList is to define:
```
PREDEFINED = QListT:=QList
```


Here is an example provided by Valter Minute and Reyes Ponce that helps doxygen to wade through the boilerplate code in Microsoft's ATL & MFC libraries:

```
PREDEFINED           = "DECLARE_INTERFACE(name)=class name" \
                       "STDMETHOD(result,name)=virtual result name" \
                       "PURE= = 0" \
                       THIS_= \
                       THIS= \
                       DECLARE_REGISTRY_RESOURCEID=// \
                       DECLARE_PROTECT_FINAL_CONSTRUCT=// \
                       "DECLARE_AGGREGATABLE(Class)= " \
                       "DECLARE_REGISTRY_RESOURCEID(Id)= " \
                       DECLARE_MESSAGE_MAP= \
                       BEGIN_MESSAGE_MAP=/* \
                       END_MESSAGE_MAP=*/// \
                       BEGIN_COM_MAP=/* \
                       END_COM_MAP=*/// \
                       BEGIN_PROP_MAP=/* \
                       END_PROP_MAP=*/// \
                       BEGIN_MSG_MAP=/* \
                       END_MSG_MAP=*/// \
                       BEGIN_PROPERTY_MAP=/* \
                       END_PROPERTY_MAP=*/// \
                       BEGIN_OBJECT_MAP=/* \
                       END_OBJECT_MAP()=*/// \
                       DECLARE_VIEW_STATUS=// \
                       "STDMETHOD(a)=HRESULT a" \
                       "ATL_NO_VTABLE= " \
                       "__declspec(a)= " \
                       BEGIN_CONNECTION_POINT_MAP=/* \
                       END_CONNECTION_POINT_MAP=*/// \
                       "DECLARE_DYNAMIC(class)= " \
                       "IMPLEMENT_DYNAMIC(class1, class2)= " \
                       "DECLARE_DYNCREATE(class)= " \
                       "IMPLEMENT_DYNCREATE(class1, class2)= " \
                       "IMPLEMENT_SERIAL(class1, class2, class3)= " \
                       "DECLARE_MESSAGE_MAP()= " \
                       TRY=try \
                       "CATCH_ALL(e)= catch(...)" \
                       END_CATCH_ALL= \
                       "THROW_LAST()= throw"\
                       "RUNTIME_CLASS(class)=class" \
                       "MAKEINTRESOURCE(nId)=nId" \
                       "IMPLEMENT_REGISTER(v, w, x, y, z)= " \
                       "ASSERT(x)=assert(x)" \
                       "ASSERT_VALID(x)=assert(x)" \
                       "TRACE0(x)=printf(x)" \
                       "OS_ERR(A,B)={ #A, B }" \
                       __cplusplus \
                       "DECLARE_OLECREATE(class)= " \
                       "BEGIN_DISPATCH_MAP(class1, class2)= " \
                       "BEGIN_INTERFACE_MAP(class1, class2)= " \
                       "INTERFACE_PART(class, id, name)= " \
                       "END_INTERFACE_MAP()=" \
                       "DISP_FUNCTION(class, name, function, result, id)=" \
                       "END_DISPATCH_MAP()=" \
                       "IMPLEMENT_OLECREATE2(class, name, id1, id2, id3, id4,\
                        id5, id6, id7, id8, id9, id10, id11)="
```


As you can see doxygen's preprocessor is quite powerful, but if you want even more flexibility you can always write an input filter and specify it after the INPUT\_FILTER  tag.

If you are unsure what the effect of doxygen's preprocessing will be you can run doxygen as follows:
```
  doxygen -d Preprocessor
```
This will instruct doxygen to dump the input sources to standard output after preprocessing has been done (Hint: set `QUIET = YES` and `WARNINGS = NO` in the configuration file to disable any other output).




---
| [Main Page](Doxygen.md) | [Files](Doxygen_files.md) |
|:------------------------|:--------------------------|