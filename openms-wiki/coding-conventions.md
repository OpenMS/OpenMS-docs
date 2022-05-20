Coding Conventions
==================

Familiarise yourself with the following code conventions.

## Coding Style
The following section focuses on coding style. OpenMS uses coding style conventions that are automatically checked using `cpplint` (`/src/tests/coding/cpplint.py`). You can find a configuration file for the `CLion IDE` here. You can import it by selecting **Preferences** > **Code Style** > **Manage**.

### Formatting

#### Indentation

OpenMS uses two spaces to indent. Tabulators in string literals should use the escape character `\t`.

#### Spaces

OpenMS uses spaces after built-in key words (e.g. `for`, `if`, `else`, etc.), and before and after binary mathematical operators.

##### Line endings

Native line endings should be allowed on each platform. This is desirable as Visual Studio for example will always insert `CRLF` even if the file is `LF` only, leading to a mixed line ending style for this file. Native `eol` style avoids this problem.

#### Bracket placements

Matching pairs of opening and closing curly braces should be set to the same column. See the following example:
```cpp
while (continue == true)
{
  for (int i = 0; i < 10; i++)
  {
    ...
  }
  if (x < 7)
  {
    ....
  }
}
```
The main reason for this rule is to avoid constructions like:
```cpp
if (isValid(a))
  error = 0;
  return 0;
```
which might later be changed to something like:
```cpp
if (isValid(a))
  error = 0;
  return 0;
```
Use braces around a block even if you use only single line. Single line constructs for trivial tests like:
```cpp
if (test) continue;
```

are allowed.

One exception is several if/else statements, which can be written as:

```cpp
if (cond1)
{
  ...
}
else if (cond2)
{
  ...
}
else if (cond3)
{
 ...
}
else
{
  ...
}
```
This is safe because the first statement in each else branch is used, which is itself braced by the if branch.

### Example class files

### Example class interface

## Naming Conventions
The following section describes the naming conventions followed by OpenMS developers.

### Reserved words

Reserved words of the C++ language and symbols defined e. g. in the `STL` or in the standard C library must not be used as names for classes or class members. Examples include but are not limited to: `set`, `map`, `exp` and `log`.

### File names

Header files and source files should be named as the classes they contain. Source files end in ".cpp", while header files end in ".h". File names should be capitalised exactly as the class they contain (see below). Each header/source file should contain one class only, although exceptions are possible for light-weight classes.

### Underscores

Usage of underscores in names has two different meanings: A trailing "_" at the end indicates that something is protected or private to a class. Apart from that, different parts of a name are sometimes separated by an underscore, and sometimes separated by capital letters.

> **_NOTE:_** According to the C++ standard, names that start with an underscore are reserved for internal purposes of the language and its standard library (roughly speaking), so you should never use them.

### Class / type / namespace names

Class names and type names always start with a capital letter. Different parts of the name are separated by capital letters at the beginning of the word. No underscores are allowed in type names and class names, except for the names of protected types and classes in classes, which are suffixed by an underscore. The same conventions apply for namespaces.

Here is an example of some classes written using the conventions described above:

```cpp
class Simple; //ordinary class
class SimpleThing; //ordinary class
class PDBFile; //using an abbreviation
class Buffer_; //protected or private nested class
class ForwardIteratorTraits_; //protected or private nested class
```

### Variable names

Variable names are written in lower case letters. Distinguished parts of the name are separated using underscores. If parts of the name are derived from common acronyms (e.g. MS) they should be in upper case. Private or protected member variables of classes are suffixed by an underscore.

Here is an example of some variable names written using the conventions described above:

```cpp
int simple; //ordinary variable
bool is_found; //ordinary variable
string MS_instrument; //using an abbreviation
int counter_; //protected or private member
int persistent_id_; //protected or private member
```
### Method names

Function names (including class method names) always start with a lower case letter. Parts of the name are separated using capital letters (as are types and class names). They should be comprehensible, but as short as possible. The same variable names must be used in the declaration and in the definition. Arguments that are actually not used in the implementation of a function have to be commented out - this avoids compiler warnings. The argument of void functions (empty argument list) must be omitted in both the declaration and the definition. If function arguments are pointers or references, the pointer or reference qualifier is appended to the variable type. It should not prefix the variable name.

Here is an example of some method names written using the conventions described above:

```cpp
void hello(); //ordinary function, no arguments
int countPeaks(PeakArray const& p); //ordinary function
bool ignore(string& /* name */); //ordinary function with an unused argument
bool isAdjacentTo(Peak const* const* const& p) const; //an ordinary function
bool doSomething_(int i, string& name); //protected or private member function
```

### Enum and preprocessor constants

Enumerated values and preprocessor constants are all upper case letters. Parts of the name are separated by underscores.

Here is an example of some enumerated values and preprocessor constants written using the conventions described above:

```cpp
#define MYCLASS_SUPPORTS_MIN_MAX 0 //preprocessor constant
enum DimensionId { DIM_MZ = 0, DIM_RT = 1 }; //enumerated values
enum DimensionId_ { MZ = 0, RT = 1 }; //enumerated values
```

Avoid using the preprocessor. Normally, `const` and `enum` will suffice for most cases.

### Parameters

Parameters should consist of lower-case letters and underscores only. For numerical parameters, the range of reasonable values is given. Where applicable units are given in the description. This rule applies to all kinds of parameter strings, both keys and string-values.

### File extensions

The correct capitalisation of all data file extensions supported by OpenMS in documented in FileHandler::NamesOfTypes[]. The convention is to use only lowercase letters for file extensions. There are three exceptions: "ML" and "XML" are written in uppercase letters and "mzData" keeps its capital "D". Please remember to keep this consistent when adding new data files or writing new TOPP tools or UTILS (use correct capitalisation for file type restrictions, here).

###

## Exception Handling

## Expose Methods to Python

## Documentation

## Testing

## Version Control
