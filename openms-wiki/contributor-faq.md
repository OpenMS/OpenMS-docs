Contributor FAQ
===============

The following contains answers to typical questions from developers about OpenMS.

> **_NOTE:_**  Some actions require special permissions like e.g. updating the website.

## General

The following section provides general information to new contributors.

### I am new to OpenMS. What should I do first?

* Check out the development version of OpenMS (see website).
* Try and build OpenMS according to the installation instructions.
* Read the OpenMS Coding Convention.
* Read the OpenMS Tutorial.
* Create a GitHub account
* Register to the open-ms-general and open-ms-developers mailing list. (You can see the developers list only if you are logged in to Sourceforge and if you are a OpenMS developer).

### What is the difference between an OpenMS tool and util?

A tool starts its lifecycle in `UTILS` and may exist without being thoroughly tested. Tools may be promoted from `UTILS` to `TOOLS` if they are stable enough, are fully tested, fully documented, and a test workflow exists.

### I have written a class for OpenMS. What should I do?

Follow the [OpenMS coding conventions](coding-conventions.md).

Coding style (brackets, variable names, etc.) must conform to the conventions.

* The class and all the members must be documented thoroughly.
* You can check your code with the tool  `tools/checker.php`. Call `php tools/checker.php` for detailed instructions.

Please open a pull request and follow the [checklist](pull-request-checklist.md).

### How do I update the [openms.de](https://www.openms.de)?

Login to the [wordpress admin area](www.openms.de/wp-admin) with your username and password assigned by the current Homepage maintainers.

## Troubleshooting

The following section provides information about how to troubleshoot common OpenMS issues.

### OpenMS complains about boost not being found but I'm sure its there!

`CMake` got confused. Set up a new build directory and try again. If you build in-source (not recommended), deleting the `CMakeCache.txt` and `cmake` directory might help.

## Build System

The following questions are related to the build system.

### What is CMake?

`CMake` builds BuildSystems for different platforms, e.g. VisualStudio Solutions on Windows, Makefiles on Linux etc.
This allows us to define in one central location (namely `CMakeLists.txt`) how OpenMS is build and have the platform specific stuff handled by `CMake`.
View the [cmake website[(http://www.cmake.org) for more information.

### How do I use CMake?

See Installation instructions for your platform.
In general, you call `CMake(.exe)` with some parameters to create the native build-system.
Afterwards you can (but usually don't have to edit the current configuration using a GUI named `ccmake` (or `CMake-GUI` in Windows), which ships with `CMake`).

> **_NOTE:_**  whenever `ccmake` is mentioned in this document, substitute this by `CMake-GUI` if your OS is Windows. You can also edit the `CMakeCache.txt` file directly.

### How do I generate a build-system for Eclipse, KDevelop, CodeBlocks etc?

Type `cmake` into a console. This will list the available code generators available on your platform, which you can pass to `CMake` using the `-G` option.

### What are user definable CMake cache variables?

They allow the user to pass options to `CMake` which will influence the build system. The most important option which should be given when calling `CMake.exe` is:

`CMAKE_FIND_ROOT_PATH`, which is where `CMake` will search for additional libraries if they are not found in the default system paths. By default we add `OpenMS/contrib`.

If your have installed all libraries on your system already there is no need to change `CMAKE_FIND_ROOT_PATH`. If you need the `contrib` libraries, you will need to set this variable.
On Windows, you always need the `contrib` folder, as there are no system developer packages. To pass this variable to `CMake` use the `-D` switch e.g. `cmake -D CMAKE_FIND_ROOT_PATH:PATH="D:\\somepath\\contrib"`.
Everything else can be edited using `ccmake` afterwards.

The following options are of interest:

* `CMAKE_BUILD_TYPE` Define if you want to build Debug or Release version of OpenMS. Release is the default.

* `CMAKE_FIND_ROOT_PATH` The path to the `contrib` libraries.
  > **_NOTE:_**  that you can also provide more then one value here (e.g., `-D CMAKE_FIND_ROOT_PATH="/path/to/contrib;/usr/"` will search in your `contrib` path and in `/usr` for the required libraries)

* `STL_DEBUG` Enables STL debug mode.

* `DB_TEST` (deprecated) Enables database testing.

* `QT_DB_PLUGIN` (deprecated) Defines the db plugin used by Qt.

* `MT_CUDA_BUILD_TYPE` ...

View the description for each option by calling `ccmake`.

### How do I switch to debug or release configuration?

For Makefile generators (typically on Linux), you can set the `CMAKE_BUILD_TYPE` variable to either Debug or Release by calling `ccmake`.
For Visual Studio, this is not necessary as all configurations are generated and you can choose the one you like within the IDE itself.
The 'Debug' configuration enabled debug information. The 'Release' configuration disables debug information and enables optimisation.

### I changed the `contrib` path, but re-running `CMake` won't change the library paths?

Once a library is found and its location is stored in a cache variable, it will only be searched again if the corresponding entry in the cache file is set to false.
You can delete the `CMakeCache.txt`, but all other custom settings will be lost.

### What are the most useful `make` targets?

In Visual Studio you can see all targets on the left. For Makefiles type make help. However, this list is quite long.
The most useful targets will be shown to you by calling the targets target, i.e. make targets.

### `CMake` can't seem to find a `Qt` library (usually `QtCore`). What now?

`CMake` finds `QT` by looking for `qmake` in your PATH or for the Environment Variable `QTDIR`. Set these accordingly.
If the problem still persists: do you have a second installation of Qt (especially the MinGW version)? This might lead ``CMake`` to the wrong path (it's searching for the ``Qt*.lib`` files).
You should only move or delete the offending `Qt` version if you know what you are doing!
A save workaround is to edit the `CMakeCache` file (e.g. via `ccmake`) and set all paths relating to `QT` (e.g. `QT_LIBRARY_DIR`) manually.

### (Windows) What version of Visual Studio should I use?

Use the latest if possible. Get the latest `CMake`, as its generator needs to support your VS. If your VS is too new and there is no `CMake` for that yet, you're gonna be faced with a lot of conversion issues.
This happens whenever the Build-System calls `CMake` (which can be quite often, e.g., after changes to `CMakeLists.txt`).

### How do I add a new class to the build system?

1. Create the new class in the corresponding sub-folder of the sub-project. The header has to be created in `src/<sub-project>/include/OpenMS` and the cpp file in `src/<sub-project>/source`, e.g., `src/openms/include/OpenMS/FORMAT/NewFileFormat.h` and `src/openms/source/FORMAT/NewFileFormat.cpp`.
2. Add both to the respective sources.cmake file in the same directory (e.g., `src/openms/source/FORMAT/` and `src/openms/include/OpenMS/FORMAT/`).
3. Add the corresponding class test to src/tests/class_tests/<sub-project>/ (e.g., `src/tests/class_tests/openms/source/NewFileFormat_test.cpp`).
4. Add the test to the `executables.cmake` file in the test folder (e.g., `src/tests/class_tests/openms/executables.cmake`).
5. Add them to git by using the command `git add`.

### How do I add a new directory to the build system?

1. Create two new `sources.cmake` files (one for `src/<sub-project>/include/OpenMS/MYDIR`, one for `src/<sub-project>/source/MYDIR`), using existing `sources.cmake` files as template.
2. Add the new `sources.cmake` files to `src/<sub-project>/includes.cmake`
3. If you created a new directory directly under `src/openms/source`, then have a look at `src/tests/class_tests/openms/executables.cmake`.
4. Add a new section that makes the unit testing system aware of the new (upcoming) tests.
5. Look at the very bottom and augment `TEST_executables`.
6. Add a new group target to `src/tests/class_tests/openms/CMakeLists.txt`.

### Class/Unit tests and TOPP/Tool tests

Class or unit tests are built as standalone, additional executables that include the class to be tested and the testing utility classes to test outcomes of single functions of the class in question.

Only add tests for functions added outside of your additional mode.

Tool tests are using the tool executable that the user would also receive. We use those executables to run the full algorithm on a small test dataset, to ensure that from version to version the results stay the same and are meaningful.

Each tool test consists of:

* An executable call on a test dataset (by using either fixed command line parameters or an ini file).

* A `FuzzyDiff` call that compares the temporary output file of the last call and a reference test output that you have to provide.

* A line to add a dependency of the FuzzyDiff call on the actual executable call (so they get executed after each other).

Use e.g., `ctest -V -R IDMapper` to only test tests that include the regex `IDMapper` (-V is just verbose). Make sure to build the `IDMapper` and `IDMapper_test` (if edited) executable first everytime.
`ctest` does not have any automatic dependency on the timestamps of the executables.

### How do I add a test for a new class?

You should always add a test alongside every new class added to OpenMS.

To add a new class test:

1. Add the class test to `src/tests/class_tests/<sub-project>/` (e.g., `src/tests/class_tests/openms/source/NewFileFormat_test.cpp`).
2. Add the test to the `executables.cmake` file in the test folder.
3. Add them to git using the `git add` command.

A test template for your specific class can be generated by the `create_test.php` script found in `tools/`.

To generate a test template for your class:

1. Make sure your generated XML files containing the class information make doc_xml.
2. Call:
```bash
php tools/create_test.php /BUILD_DIRECTORY/ /    PATH_TO_HEADER/MyClass.h \ "FIRSTNAME LASTNAME" > ./src/tests/class_tests/openms/source/MyClass_test.cpp
```

### How do I add a new GUI test (for QT Gui classes) for the class `MyClass`?
To add a new GUI test:

1. Create the `MyClass_test.cpp` in `src/tests/class_tests/openms_gui/source`.
2. Add it to `src/tests/class_tests/openms_gui/CMakeLists.txt` in the GUI section.
3. Have a look at existing GUI tests, as they use the `QT TestLib` framework and not the OpenMS macros.

### (Linux) All tests fail when you execute `make test`

Check the `LD_LIBRARY_PATH` environment variable:

You can print the `LD_LIBRARY_PATH` with `echo $LD_LIBRARY_PATH`. If your `/lib/` folder is included, check that `libOpenMS.so` is present.
With the `ldd` command, you can show the libraries used by an executable, e.g. `ldd /bin/ClassTest_test`.

## Release

View [Preparation of a new OpenMS release](https://github.com/OpenMS/OpenMS/wiki/Preparation-of-a-new-OpenMS-release#release_developer) to learn more about contributing to releases.

## Debugging

The following section provides information about how to debug your code.

### How do I run a single test?

You can can execute an OpenMS class test using the CTest regular expressions:

```bash

ctest -V -R "^<class>_test"

# To build a class test, you simply call the respective make target in ./source/TEST:

make <class>_test
```
To run a TOPP test, you can use:

```bash

ctest -V -R "TOPP_<tool>"
```

To build the tool, use:

```bash
make <tool>
```
### How do I debug uncaught exceptions?

You can dump a core if an uncaught exception occurs, by setting the environment variable `OPENMS_DUMP_CORE`.

Each time an uncaught exception occurs, the `OPENMS_DUMP_CORE` variable is checked and a segmentation fault is caused, if it is set.

### (Linux) Why is no core dumped, although a fatal error occured?

Try the `ulimit -c` unlimited command. It sets the maximum size of a core to unlimited.

> **_NOTE:_**  We observed that, on some systems, no core is dumped even if the size of the core file is set to unlimited. We are not sure what causes this problem

### (Linux) How can I set breakpoints in gdb to debug OpenMS?

Imagine you want to debug the TOPPView application and you want it to stop at line 341 of SpectrumMDIWindow.C.

1. Enter the following in your terminal:

  ```bash
  Run gdb:
 shell> gdb TOPPView
```

2. Start the application (and close it):

  ```bash
 gdb> run [arguments]
```
3. Set the breakpoint:
  ```bash
 gdb> break SpectrumMDIWindow.C:341
```
4. Start the application again (with the same arguments):

  ```bash
 gdb> run
 ```

### How can I find out which shared libraries are used by an application?

Linux: Use `ldd`.

Windows (Visual studio console): Try [Dependency Walker](http://www.dependencywalker.com/) (use x86 for 32bit builds and the x64 version for 64bit builds. Using the wrong version of depends.exe will give the wrong results) or ``dumpbin /DEPENDENTS OpenMS.dll``.

### How can I get a list of the symbols defined in a (shared) library or object file?

Linux: Use `nm <library>`.

Use `nm -C` to switch on demangling of low-level symbols into their C++-equivalent names. `nm` also accepts .a and .o files.

Windows (Visual studio console): Use ``dumpbin /ALL <library>``.

You can use dumpbin on object files (.o) or (shared) library files (.lib) or the DLL itself e.g. `dumpbin /EXPORTS OpenMS.dll`.

## Cross-platform thoughts

OpenMS runs on three major platforms. Here are the most prominent causes of "it runs on Platform A, but not on B. What now?"

### Reading or writing binary files
Reading or writing binary files causes different behaviour. Usually Linux does not make a difference between text-mode and binary-mode when reading files. This is quite different on Windows as some bytes are interpreted as `EOF`, which lead might to a premature end of the reading process.

If reading binary files, make sure that you explicitly state that the file is binary when opening it.

During writing in text-mode on Windows a line-break (`\n`) is expanded to (`\r\n`). Keep this in mind or use the `eol-style` property of subversion to ensure that line endings are correctly checked out on non-Windows systems.

### `UInt` vs `Size`
Both `unsigned int` vs `size_t` `UInt` and `Size` have the same size on Linux GCC (32bit on 32bit systems, 64bit on 64 bit systems), however on Windows this only holds for 32bit. On a 64bit Windows, the `UInt` type is still 32bit, while the `Size` type is 64bit. This might lead to warnings (at best) or overflows and other drawbacks.
Therefore, do not assume that `UInt` is equal to `Size`.

### Paths and system functions

Avoid hardcoding e.g.`String tmp_dir = "/tmp";`. This will fail on Windows. Use Qt's `QDir` to get a path to the systems temporary directory if required.

Avoid names like uname which are only available on Linux.

When working with files or directories, it is usually safe to use "/" on all platforms. Take care of spaces in directory names though. You should always quote paths if they are used in a system call to ensure that the subsequent interpreter takes the spaced path as a single entity.

## Doxygen Documentation

### Where can I find the definition of the main page?

You can find a definition of the main page [here](https://github.com/OpenMS/OpenMS/edit/develop/doc/doxygen/public/Main.doxygen).

### Where can I add a new module?

You can add a new module [here](https://github.com/OpenMS/OpenMS/edit/develop/doc/doxygen/public/Modules.doxygen).


### How is the command line documentation for TOPP/UTILS tools created?

The program `OpenMS/doc/doxygen/parameters/TOPPDocumenter.cpp` creates the command line documentation for all classes that are included in the static `ToolHandler.cpp` tools list. It can be included in the documentation using the following `doxygen` command:

`@verbinclude TOPP_<tool name>.cli`

You can test if everything worked by calling `make doc_param_internal`. The command line documentation is written to `OpenMS/doc/doxygen/parameters/output/`.

### What are the important files for adding a new tutorial section?

View the following OpenMS tutorials:

* `OpenMS/doc/OpenMS_tutorial/refman_overwrite.tex.in` (for PDF tutorials)
* `OpenMS/doc/doxygen/public/OpenMS_Tutorial_html.doxygen~` (for html tutorials)

For TOPP and TOPPView tutorials, view:

* `OpenMS/doc/TOPP_tutorial/refman_overwrite.tex.in` (for PDF tutorials)
* `OpenMS/doc/doxygen/public/TOPP_Tutorial_html.doxygen` (for html tutorials)

## Bug Fixes

### How to contribute a bug fix?

To contribute to a bug fix:
1. Submit the bug as a GitHub issue.
2. Create a feature branch (e.g. `feature/fix_missing_filename_issue_615`) from your (up-to-date) develop branch in your fork of OpenMS.
3. Fix the bug and add a test.
4. Create a pull request for your branch.
5. After approval and merge make sure the issue is closed.

### How can I profile my code?

Try IBM's profiler, available for all platforms (and free for academic use): Purify(Plus) and/or Quantify.

Windows: this is directly supported by Visual Studio (Depending on the edition: Team and above). Follow their documentation.

Linux:

1. Build OpenMS in debug mode (set `CMAKE_BUILD_TYPE` to `Debug`).
2. Call the executable with valgrind: `valgrind –tool=callgrind`.
  > **_NOTE:_**  other processes running on the same machine can influence the profiling. Make sure your application gets enough resources (memory, CPU time).

3. You can start and stop the profiling while the executable is running e.g. to skip initialization steps:
4. Start valgrind with the option `–instr-atstart=no`.
5. Call `callgrind -i [on|off]` to start/stop the profiling.
6. The output can be viewed with `kcachegrind callgrind.out`.

### (Linux) How do I check my code for memory leaks?

* Build OpenMS in debug mode (set ``CMAKE_BUILD_TYPE`` to ``Debug``).
* Call the executable with ``valgrind: valgrind --suppressions=OpenMS/tools/valgrind/openms_external.supp –leak-check=full <executable> <parameters>``.

Common errors are:

* ``'Invalid write/read ...'`` - Violation of container boundaries.
* ``'... depends on uninitialized variable'`` - Uninitialized variables:
* ``'... definitely lost'`` - Memory leak that has to be fixed
* ``'... possibly lost'`` - Possible memory leak, so have a look at the code

For more information see the [`valgrind` documentation](http://valgrind.org/docs/manual/) .
