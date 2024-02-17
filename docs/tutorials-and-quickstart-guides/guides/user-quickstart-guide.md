User Quickstart Guide
====================

Read the User Quickstart guide to gain a brief understanding of key concepts and how to use the tools. For more in-depth
information, consult [OpenMS API Reference](https://openms.de/current_doxygen/).

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
|**TOPPAS**          |A graphical workflow design tool that is used to create pipelines from all {term}`TOPP tools`.|
|**TOPP tools**      |A set of command line tools. Each of these command line tools is a building block of an analysis pipeline and are chained together in a way that fits the requirements of the user. The {term}`TOPP tools` are accessible from a command prompt/shell or via {term}`TOPPAS`. |


## How to run a Tool

In general TOPP tools are invoked via the command line, directly or indirectly (e.g. via worflow systems such as {term}`KNIME`, {term}`Nextflow`, snakemake, or {term}`TOPPAS`).

## Adapt pipeline parameters

The default parameters of each tool can usually be tweaked to fit the data and improve results.
Here, we describe how to work with TOPP tools on a command line (irrespective of the operating system) or using TOPPAS workflow system, which is shipped with OpenMS. 
For [external workflow systems](../../run-workflows-with-openms-tools/recommended-workflow-systems.md), please refer to their documentation.


### Where do you change pipeline parameters?

1. **TOPPAS**: Double-click the node of which you want to change the parameters of. A short docu for each parameter will
               show up once it is selected. All parameters which would be available on the command line and in the INI
	       file are shown here as well.
2. **Command line**: Very basic parameters can be set on the command line, e.g. `FileFilter -rt 1000:2000 .....`
3. Passing all parameters via commandline would create a very long list, thus, use so-called `.ini` files to provide full parameter
   sets to {term}`TOPP tools`. If no INI file is given, default parameters are used. To get a default `.ini` use

   `<tool> -write_ini <file>`

   e.g. `FileFilter -write_ini filefilter.ini`

   Now, edit the INI file (which is a XML file) using the [INIFileEditor](../../openms-applications-and-tools/openms-applications/ini-file-editor.md), which is another GUI tool shipped with
   OpenMS and similar to the one build into {term}`TOPPAS`.

### How do I feed the INI file to a Tool?

1. **TOPPAS**: Once you changed the parameters of a node and clicked **Ok**, the parameters are in effect. Because
   they are part of the {term}`TOPPAS` workflow, they are saved together with the workflow.
2. **Command line** : Supply the INI file via the `-ini` flag,
   `<tool> -ini <file>`

   e.g. `FileFilter -ini filefilter.ini`

### What parameters to set and to what value?

The answer is complex, in general, read the tool description, change the parameters and compare the results using
{term}`TOPPView` if possible. If that does not help, [contact us](/quick-reference/contact-us.md). Please include all the necessary
details we need in order to help you.
