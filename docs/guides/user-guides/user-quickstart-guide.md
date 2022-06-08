User Quickstart Guide
====================

Read the User Quickstart guide to gain a brief understanding of key concepts and how to use the tools. For more in-depth
information, consult [OpenMS API Reference](https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/nightly/html/index.html).

## What is OpenMS

[OpenMS](https://www.openms.de/) is a free, open-source C++ library with Python bindings. It is commonly used for liquid
chromatography-mass spectrometry ({term}`LC-MS`) data management and analyses. OpenMS provides an infrastructure for the rapid
development of mass spectrometry related software as well as a rich toolset built on top of it. OpenMS is available
under the [three clause BSD licence](https://github.com/OpenMS/OpenMS/blob/develop/LICENSE) and runs under Windows, macOS, and Linux operating systems.

## Background

Before using OpenMS, become familiar with the following terms:

| Tool and Utilities | Description |
|--------------------|-------------|
|**TOPPView**        |A tool that is used to view and explore {term}`LC-MS` data, alignments, groups, peptide identifications, and more.|
|**TOPPAS**          |A graphical workflow design tool that is used to create pipelines from all {term}`TOPP tools` (and {term}`UTILS`).|
|**TOPP tools**      |A set of command line tools. Each of these command line tools is a building block of an analysis pipeline and are chained together in a way that fits the requirements of the user. The {term}`TOPP tools` are accessible from a command prompt/shell or via {term}`TOPPAS`. See also: [TOPP tutorial](../../tutorials/TOPP/TOPP-tutorial.md) and [TOPP documentation](../../topp/topp.md)|
|**UTILS**           |Similar to {term}`TOPP tools`, but with more supporting character, which are rarely used in a productive pipeline, but rather during pipeline construction or parameter optimization. See also: [UTILS documentation](https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/nightly/html/UTILS_documentation.html)|

## How to run a Tool

A good start are the example pipelines (select **File** > **Open example file** within {term}`TOPPAS`).

Read the documentation of the tools see [TOPP tutorial](../../tutorials/TOPP/TOPP-tutorial.md), [TOPP documentation](../../topp/topp.md) and the one of ([TOPPAS tutorial](../../tutorials/TOPPAS/TOPPAS-tutorial.md)).

Alternatively, use the command line and call tools directly. In this case, you'll probably want to use some type of shell
script for automation.

## Adapt pipeline parameters

The default parameters of each tool can usually be tweaked to fit the data and improve results.

### Where do you change pipeline parameters?

1. **TOPPAS**: Double-click the node of which you want to change the parameters of. A short docu for each parameter will
               show up once it is selected. All parameters which would be available on the command line and in the INI
	       file are shown here as well.
2. **Command line**: Very basic parameters can be set on the command line, e.g. `FileFilter -rt 1000:2000 .....`
3. Doing 2 for all parameters would create a very long list, thus, use so-called `.ini` files to provide full parameter
   sets to {term}`TOPP tools`. If no INI file is given, default parameters are used. To get a default `.ini` use

   `<tool> -write_ini <file>`

   e.g. `FileFilter -write_ini filefilter.ini`

   Now, edit the INI file (which is a XML file) using the [INIFileEditor](../../topp/ini-file-editor.md), which is another GUI tool shipped with
   OpenMS and similar to the one build into {term}`TOPPAS`.

### How do I feed the INI file to a Tool?

1. **TOPPAS**: Once you changed the parameters of a node and clicked **Ok**, the parameters are in effect. Because
   they are part of the {term}`TOPPAS` workflow, they are saved together with the workflow.
2. **Command line** : Supply the INI file via the `-ini` flag,
   `<tool> -ini <file>`

   e.g. `FileFilter -ini filefilter.ini`

### What parameters to set and to what value?

The answer is complex, in general, read the tool description, change the parameters and compare the results using
{term}`TOPPView` if possible. If that does not help, [contact us](../../contact-us.md). Please include all the necessary
details we need in order to help you.
