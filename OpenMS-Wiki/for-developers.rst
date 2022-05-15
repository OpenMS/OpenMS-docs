==============
For Developers
==============

Developing with OpenMS
**********************
If you would like to contribute to OpenMS, this is how to best get started:

- Familiarize yourself with our `online documentation <https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/release/latest/html/index.html>`_.

- Learn how to `build OpenMS <https://github.com/OpenMS/OpenMS/wiki/Building-OpenMS>`_.

- Start reading the `OpenMS tutorial for developers <https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/release/latest/html/OpenMS_tutorial.html>`_.

- Any questions can be directed at the mailing list.

OpenMS tutorial for developers
******************************
Please read the `OpenMS tutorial for developers <https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/release/latest/html/OpenMS_tutorial.html>`_)
which contains general information about the structure of OpenMS, the concepts
behind it and example code.

Technical Documentation
***********************
See the documentation for the nightly snapshot of `develop <https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/nightly/html/index.html>`_ (`doxygen log <https://abibuilder.informatik.uni-tuebingen.de/jenkins/job/openms_nightly_packaging/lastBuild/compiler=appleclang-7.3.0,os_label=elcapitan/artifact/build/doc/doxygen/doxygen-error.log>`_).

See the documentation for the latest `release <https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/release/latest/html/index.html>`_ (`doxygen log <https://abibuilder.informatik.uni-tuebingen.de/jenkins/job/openms_release_packaging/lastBuild/compiler=appleclang-7.3.0,os_label=elcapitan/artifact/build/doc/doxygen/doxygen-error.log>`_).

Development model
*****************
OpenMS follows the Gitflow development workflow which is excellently described `here <http://nvie.com/posts/a-successful-git-branching-model/>`_. Additionally we encourage every developer (even if he is eligible to push directly to OpenMS) to create his own fork (e.g. @username). The GitHub people provide superb documentation on `forking <https://help.github.com/articles/fork-a-repo>`_ and how to keep your fork `up-to-date <https://help.github.com/articles/syncing-a-fork>`_. With your own fork you can follow the Gitflow development model directly, but instead of merging into "develop" in your own fork you can open a `pull request <https://help.github.com/articles/using-pull-requests>`_. Before opening the pull request, please check the `checklist <https://github.com/OpenMS/OpenMS/wiki/Pull-Request-Checklist>`_

Some more details and tips are collected `here <https://github.com/OpenMS/OpenMS/wiki/OpenMS-Git-Workflow>`_.

Coding Conventions
******************
See the manual for proper coding style: `Coding conventions <https://github.com/OpenMS/OpenMS/wiki/Coding-conventions>`_
also see: `C++ Guide <http://https://github.com/OpenMS/OpenMS/wiki/Cpp-Guide>`_.

See the `manual <https://github.com/OpenMS/OpenMS/wiki/NewBuildUnit>`_ for creating a new build unit (to be completed).

We automatically test for common coding convention violations using a modified version of cpplint.
Style testing can be enabled using CMake options. We also provide a configuration file for Uncrustify for automated style corrections (see "tools/uncrustify.cfg").

Commit Messages
***************
In order to ease the creation of a CHANGELOG we use a defined format for our commit messages.

See the manual for proper commit messages: `How to write commit messages <http://https://github.com/OpenMS/OpenMS/wiki/HowTo---Write-Commit-Messages>`_.

Automated Unit Tests
********************
We perform nightly test runs on different platforms. Even if everything compiled well on your machine and all tests passed, please check if you broke another platform on the next day.

Nightly tests: `CDASH <http://cdash.openms.de/index.php?project=OpenMS>`_

Further developer resources
***************************

Guidelines for addition of new dependency libraries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
See `here <https://github.com/OpenMS/OpenMS/wiki/Developer-Guidelines-for-adding-new-dependent-libraries>`_.

Experimental Installers
^^^^^^^^^^^^^^^^^^^^^^^
We automatically build installers for different platforms. These usually contain unstable or partially untested code - so use them at your own risk.

The nightly (unstable) installers are available `here <https://abibuilder.informatik.uni-tuebingen.de/archive/openms/OpenMSInstaller/nightly/>`_.

Developer FAQ (formerly Internal FAQ)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The `FAQ <https://github.com/OpenMS/OpenMS/wiki/Developer-FAQ>`_ for developers is currently expanded and might contain answers to your questions.
`FAQ <developer-faq.rst>`
