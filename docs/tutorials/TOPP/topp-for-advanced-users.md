TOPP for Advanced Users
======================

This tutorials has some advanced concepts of TOPP, which will increase productivity and easy usage.

## Global database for search engine adapters

In your `$HOME` directory find an `OpenMS.ini` in the `.OpenMS` subfolder. This INI file contains global parameters
which are used by many/all TOPP tools, depending on what the parameters refer to. The `id\_db\_dir` parameter allows to
specify one or more directories where FASTA files (or related, e.g., `.psq` files) are placed. Specified filename
(without path) in an ID engine adapter, will be looked up in the current working directory. If its not found, the
directories specified in `id_db_dir` will be searched. This allows to build scripts and/or TOPPAS pipelines which are
portable across several computers, just adapt the OpenMS.ini once on each machine.

> **_NOTE:_** When using TOPPAS: Use an "input file" node to specify the FASTA file for several engines simultaneously.
However, when selecting the file, TOPPAS will use the absolute pathname and the dialog will not allow to name a
non-existing file. After selecting the file you can however edit the filename and remove the path (this will issue a
warning which can be ignored).

> **_NOTE:_** This approach does not work for OpenMS MascotAdapters, as each Mascot instance has its own database
managed internally. Make sure that the database is present on all mascot servers you're going to use, thus making the
INI settings portable.

## Using external tools in workflows

OpenMS supports the wrapping of external tools (like msconvert from ProteoWizard), thus allowing to build scripts and/or
TOPPAS pipelines containing external tools.

**See also**

     `share/OpenMS/TOOLS/EXTERNAL/ReadMe.txt` in your local installation for details.
