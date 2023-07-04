Entry Points to OpenMS
======================

OpenMS has been structured so that users from a wide range of fields can access what they need to solve their particular problem, depending on their skillset.

![openms architecture](/images/introduction/openms-architecture.png)

The following entry points for OpenMS and its TOPP tools are available for users (click the card for more information):

::::{grid} 1 1 2 2

:::{grid-item-card} {material-regular}`account_tree;5em;sd-text-info` **Workflows** <br/> Use a supported workflow editor to create or run predefined workflows
  :link: /run-workflows-with-openms-tools/recommended-workflow-systems
  :link-type: doc

  Suppose you want to run the same sequence of TOPP tools on a number of data sets. You can use applications such as KNIME, Nextflow and Galaxy (where TOPP tools are available as a plugin), to apply predefined workflows or custom workflows you have designed on your data.

:::

:::{grid-item-card} {material-regular}`insert_chart;5em;sd-text-info` **Graphical apps** <br/> Use OpenMS graphical user interfaces to easily process data and inspect results
  :link: /openms-applications-and-tools/openms-graphical-user-interfaces
  :link-type: doc
  When OpenMS is installed, a number of graphical user interfaces are available. Life science experts that want to quickly process their mass spectrometry data with the TOPP tools available can use this option.

:::

::::

::::{grid} 1 1 2 2

:::{grid-item-card} {octicon}`terminal;5em;sd-text-info` **Command-line tools** <br/> Use over 100 command-line tools to automate pre-defined tasks efficiently
  :link: /openms-applications-and-tools/command-line-interface
  :link-type: doc

  All TOPP tools can be executed from a Command Line Interface (CLI) directly or using a shell script. By using a CLI, users can easily automate tasks and create workflows that can be saved, stored and used on multiple datasets. Command line interfaces include, but are not limited to PowerShell in Windows or Terminal in Linux or macOS.
:::

:::{grid-item-card} {fab}`python;sd-text-info fa-xl` **pyOpenMS** <br/> Use the pyOpenMS python library to rapidly prototype methods and scripts
  :link: https://pyopenms.readthedocs.io/en/latest/user_guide/installation.html
  :link-type: url
  :class-title: flex

  Classes and methods originally written in C++ have been exposed to a Python interface (pyOpenMS) using Python bindings (via Cython). Central data structures even provide fast export to pandas dataframes or numpy arrays. pyOpenMS was created for users with Python knowledge who want to quickly prototype new methods and scripts or interface with other prominent data science, machine learning or visualization libraries such as tensorflow or plotly.
:::

::::


:::{card} {octicon}`cpu;5em;sd-text-info` **OpenMS C++ core library** <br/> Build the OpenMS C++ core library from source to develop your own efficient tools and methods
  :link: /develop-with-openms/openms-core-cplusplus-library
  :link-type: doc

  As shown in the image above, TOPP tools have been created using the OpenMS core library and some external libraries, which are written in C++. Using the OpenMS core library directly provides faster access to tools and shorter run-times. Additional TOPP tools can also be developed, customized or extended based on the user’s needs.
:::



