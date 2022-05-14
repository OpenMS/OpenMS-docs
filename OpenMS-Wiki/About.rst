=====
About
=====


.. contents:: Contents

Background
##########
OpenMS is an open-source C++ library for mass spectrometry (MS) data management and analysis. It offers an infrastructure for the rapid development of mass spectrometry-related software. OpenMS is free software available under the three-clause BSD license. It runs under Windows, Mac OS X and Linux.

OpenMS comes with a vast variety of pre-built and ready-to-use tools for proteomics and metabolomics data analysis (TOPP tools) and powerful 2D and 3D visualization (TOPPView). It supports analyses for various quantification protocols, including label-free shotgun, SILAC, iTRAQ, SRM, SWATH, .... It also provides built-in algorithms for peptide/protein identification, both de-novo and via database searching, as well as adapters to state-of-the art tools like X! Tandem,  Mascot, OMSSA and others.

Through the TOPP tools concept and unified parameter handling (CTD), OpenMS supports easy integration into workflow engines like TOPPAS (included), KNIME, Galaxy or WS-PGRADE.
With PyOpenMS, OpenMS offers Python bindings to a large part of the API to enable rapid algorithm development.

OpenMS supports the Proteomics Standard Initiative (PSI) file formats for MS data.
The main contributors of OpenMS are currently Eberhard-Karls Universität in Tübingen, Freie Universität Berlin and ETH Zurich.

For Users
#########

Getting Started with OpenMS
***************************
The current stable version of OpenMS can be downloaded from the [OpenMS download site](http://open-ms.de/downloads/) or can be obtained via the [[OpenMS docker containers|OpenMS Docker Containers]].

As a general primer to OpenMS, we also recommend to read [Röst et al, OpenMS: a flexible open-source software platform for mass spectrometry data analysis. Nat Methods. 2016](https://www.ncbi.nlm.nih.gov/pubmed/27575624) as well as the [Getting Started](http://www.openms.de/getting-started/) page on openms.de.

Novice users should start by reading the OpenMS documentation (especially for TOPP) available from the [OpenMS documentation site](http://www.openms.de/current_doxygen/) or in the folder doc/index.html of stable releases. Some example workflows with optimised parameter settings can be downloaded from the [repository](https://github.com/OpenMS/OpenMS/wiki/Workflow-Collection). To understand which tools are available, please read the [TOPP Tool documentation page](http://www.openms.de/current_doxygen/html/TOPP_documentation.html) as well as the [UTILS Tool documentation page](http://www.openms.de/current_doxygen/html/UTILS_documentation.html).

Getting in Contact
******************
For general usage problems, bug reports and questions, please contact us directly on [Gitter](https://gitter.im/OpenMS/OpenMS) for real-time interaction with the developers or write to the mailing list [open-ms-general](https://lists.sourceforge.net/lists/listinfo/open-ms-general/).

If you only want to be informed of new versions of OpenMS, please subscribe to the mailing list [open-ms-announcements](https://lists.sourceforge.net/lists/listinfo/open-ms-announcements).

Reporting Bugs/Issues
*********************
A list of known issues in the current OpenMS release can be found here. Please check if your OpenMS version matches the current version and if the bug has already been reported.

In order to report a new bug, please use either our [GitHub issues system](Writing-and-labelling-GitHub-issues) or contact us through the general OpenMS mailing list.

Please include the following information into your bug report:
* the command line (i.e. call) including the TOPP tool and the arguments you used, or the steps you followed in a GUI tool (e.g. TOPPView) - e.g. "FeatureFinderCentroided -in myfile.mzML -out myfile.featureXML"
* the output of OpenMS/TOPP (or a screenshot in case of a GUI problem)
* operating system (e.g. "Windows XP 32bit", "Win 7 64bit", "Fedora 8 32bit", "MacOS 10.6 64bit")
* OpenMS version (e.g. "OpenMS 1.11.1", "Revision 63082 from the SVN repository")
* OpenMS architecture ("32 bit" or "64 bit")

Please provide files that we need to reproduce the bug (e.g. TOPP INI files, data files - usually mzML) via a download link, via the mailing list or by directly contacting one of the developers.

For Developers
##############

Developing with OpenMS
**********************
If you would like to contribute to OpenMS, this is how to best get started:

- Familiarize yourself with our [online documentation](https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/release/latest/html/index.html).

- Learn how to [[build OpenMS|Building OpenMS]].

- Start reading the [OpenMS tutorial for developers](https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/release/latest/html/OpenMS_tutorial.html).

- Any questions can be directed at the mailing list.

OpenMS tutorial for developers
******************************
Please read the [OpenMS tutorial for developers](https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/release/latest/html/OpenMS_tutorial.html)
which contains general information about the structure of OpenMS, the concepts
behind it and example code.

Technical Documentation
***********************
See the documentation for the nightly snapshot of [develop](https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/nightly/html/index.html) ([doxygen log](https://abibuilder.informatik.uni-tuebingen.de/jenkins/job/openms_nightly_packaging/lastBuild/compiler=appleclang-7.3.0,os_label=elcapitan/artifact/build/doc/doxygen/doxygen-error.log)).

See the documentation for the latest [release](https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/release/latest/html/index.html) ([doxygen log](https://abibuilder.informatik.uni-tuebingen.de/jenkins/job/openms_release_packaging/lastBuild/compiler=appleclang-7.3.0,os_label=elcapitan/artifact/build/doc/doxygen/doxygen-error.log)).


Development model
*****************
OpenMS follows the Gitflow development workflow which is excellently described [here](http://nvie.com/posts/a-successful-git-branching-model/). Additionally we encourage every developer (even if he is eligible to push directly to OpenMS) to create his own fork (e.g. @username). The GitHub people provide superb documentation on [forking](https://help.github.com/articles/fork-a-repo) and how to keep your fork [up-to-date](https://help.github.com/articles/syncing-a-fork). With your own fork you can follow the Gitflow development model directly, but instead of merging into "develop" in your own fork you can open a [pull request](https://help.github.com/articles/using-pull-requests). Before opening the pull request, please check the [checklist](Pull-Request-Checklist)

Some more details and tips are collected [here](OpenMS-Git-Workflow).

Coding Conventions
******************
See the manual for proper coding style: [Coding conventions](Coding-conventions)
also see: [C++ Guide](https://github.com/OpenMS/OpenMS/wiki/Cpp-Guide)

See the [manual](NewBuildUnit) for creating a new build unit (to be completed)

We automatically test for common coding convention violations using a modified version of cpplint.
Style testing can be enabled using CMake options. We also provide a configuration file for Uncrustify for automated style corrections (see "tools/uncrustify.cfg").

Commit Messages
***************
In order to ease the creation of a CHANGELOG we use a defined format for our commit messages.

See the manual for proper commit messages: [How to write commit messages](https://github.com/OpenMS/OpenMS/wiki/HowTo---Write-Commit-Messages)

Automated Unit Tests
********************
We perform nightly test runs on different platforms. Even if everything compiled well on your machine and all tests passed, please check if you broke another platform on the next day.

Nightly tests: [CDASH](http://cdash.openms.de/index.php?project=OpenMS)


Further developer resources
***************************

Guidelines for addition of new dependency libraries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
See [here](https://github.com/OpenMS/OpenMS/wiki/Developer-Guidelines-for-adding-new-dependent-libraries).

Experimental Installers
^^^^^^^^^^^^^^^^^^^^^^^
We automatically build installers for different platforms. These usually contain unstable or partially untested code - so use them at your own risk.

The nightly (unstable) installers are available [here](https://abibuilder.informatik.uni-tuebingen.de/archive/openms/OpenMSInstaller/nightly/).

Developer FAQ (formerly Internal FAQ)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The [FAQ](https://github.com/OpenMS/OpenMS/wiki/Developer-FAQ) for developers is currently expanded and might contain answers to your questions.
