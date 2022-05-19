User Quickstart Guide
====================

Read the User Quickstart guide to gain a brief understanding of key concepts and how to use the tools. For more in-depth
information, consult [OpenMS documentation]().

## What is OpenMS

[OpenMS](https://www.openms.de/) is a free, open-source C++ library with Python bindings. It is commonly used for liquid
chromatography-mass spectrometry (LC-MS) data management and analyses. OpenMS provides an infrastructure for the rapid
development of mass spectrometry related software as well as a rich toolset built on top of it. OpenMS is available
under the three clause BSD licence and runs under Windows, macOS, and Linux operating systems.

## Background

Before using [OpenMS](https://www.openms.de/), you need to be familiar with the following terms:

| Tool and Utilities | Description |
|--------------------|-------------|
|**TOPPView**        |A design tool that is used to view and explore LC-MS data, alignments, groups, peptide identifications, and more.|
|**TOPPAS**          |A graphical workflow design tool that is used to create pipelines from all TOPP tools (and UTILS).|
|**TOPP tools**      |A set of command line tools. Each of these command line tools is a building block of an analysis pipeline and are chained together in a way that fits the requirements of the user. The TOPP tools are accessible from a command prompt/shell or via TOPPAS. See also: [TOPP tutorial]() and [TOPP documentation](https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/nightly/html/TOPP_documentation.html)|
|**UTILS**           |Similar to TOPP tools, but with more supporting character, which are rarely used in a productive pipeline, but rather during pipeline construction or parameter optimization. See also: [UTILS documentation](https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/nightly/html/UTILS_documentation.html)|

## How to run a Tool

It is recommended to use TOPPAS. A good start are the example pipelines (see "File" –> "Open example file" within TOPPAS).
In parallel read the documentation of the tools (see [TOPP tutorial](), [TOPP documentation](https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/nightly/html/TOPP_documentation.html)) and the one of TOPPAS ([TOPPAS tutorial](https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/nightly/html/TOPP_documentation.html)).

Alternatively, you can use the command line and call tools directly. In this case you'll probably want to use some type of shell
script for automation.

## Adapting your Pipeline Parameters

The default parameters of each tool can usually be tweaked to fit the data and improve results.

### Where do you change them?

1. **TOPPAS**: Double-click the node of which you want to change the parameters of. A short docu for each parameter will
               show up once it is selected. All parameters which would be available on the command line and in the INI
	       file are shown here as well.
2. **Command line**: Very basic parameters can be set on the command line, e.g. `FileFilter -rt 1000:2000 .....`
3. Doing 2 for all parameters would create a very long list, thus, use so-called ".ini" files to provide full parameter
   sets to TOPP tools. If no INI file is given, default parameters are used. To get a default `.ini` use
   
   `<tool> -write_ini <file>`
   
   e.g. `FileFilter -write_ini filefilter.ini`

   Now, edit the INI file (which is a XML file) using the [INIFileEditor](), which is another GUI tool shipped with
   OpenMS and similar to the one build into TOPPAS.

### How do I feed the INI file to a Tool?

1. **TOPPAS**: Once you changed the parameters of a node and clicked "Ok", the parameters are in effect. Because
   they are part of the TOPPAS workflow, they are saved together with the workflow.
2. **Command line** : Simply supply the INI file via the `-ini` flag,  
   `<tool> -ini <file>`
   
   e.g. `FileFilter -ini filefilter.ini`

### What parameters require to be changed and to what value?

This is tricky and its not possible to give a general answer. In general, read the tool description, change the
parameters and compare the results using TOPPView if possible. If that does not help, drop us an email on the
[OpenMS mailing list]() and ask. Please include all the necessary details we need in order to help you.





