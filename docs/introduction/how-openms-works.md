How OpenMS Works
================

OpenMS has been structured so that users from a wide range of fields can access what they need to solve their particular problem, depending on their skillset.

The following entry points for OpenMS and its TOPP tools are available for users:
- **Download the OpenMS C++ core library**

  As shown in the image below, TOPP tools have been created using the OpenMS core library and some external libraries, which are written in C++. Using the OpenMS core library directly provides faster access to tools and shorter run-times. Additional TOPP tools can also be developed, customized or extended based on the user’s needs. View the instructions to download the OpenMS core library here.
- **Install the pyOpenMs python library**

  Classes and methods originally written in C++ have been exposed to a Python interface (pyOpenMS) using python bindings. pyOpenMS was created for users with Python knowledge who want to quickly prototype new methods. View the instructions to install pyOpenMS here.

- **Use command-line tools**

  All TOPP tools can be executed from a Command Line Interface (CLI) directly or using a shell script. By using a CLI, users can easily automate tasks and create workflows that can be saved, stored and used on multiple datasets. Command line interfaces include, but are not limited to PowerShell in Windows or Terminal in Linux or macOS. View the command-line usage quick start guide here.

- **Use OpenMS graphical applications**

  When OpenMS is installed, a number of graphical user interfaces are available. Life science experts that want to quickly process their mass spectrometry data with the TOPP tools available can use this option. View the instructions to install OpenMS here.

- **Use a supported workflow editor**

  Suppose you want to run the same sequence of TOPP tools on a number of data sets. You can use applications such as KNIME and Galaxy (where TOPP tools are available as a plugin), to apply predefined workflows or custom workflows you have designed on your data. KNIME and Galaxy are recommended over TOPPAS, which can also be used to create workflows however is no longer supported.
