Contribute to OpenMS
====================

If you would like to contribute to OpenMS:

* Familiarise yourself with our [online documentation](https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/release/latest/html/index.html).

* Learn how to [build OpenMS](build-openms-from-source.md).

* Check out the [OpenMS tutorial for developers](https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/release/latest/html/OpenMS_tutorial.html).

For any questions, please [contact us](contact-us.md) at [open-ms-general]((https://sourceforge.net/projects/open-ms/lists/open-ms-general) mailing list.

## Technical Documentation
Untested installers and containers are known as the nightly snapshot, are released every night. They generally pass automated continuous integration tests but no manual tests.  

View the documentation for the nightly snapshot of [OpenMS develop branch](https://github.com/OpenMS/OpenMS/tree/develop) at the [build archive](https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/nightly/html/index.html).

View the [doxygen log](https://abibuilder.informatik.uni-tuebingen.de/jenkins/job/openms/job/ntly/job/TstPkg/compiler=appleclang-11.0.0,os_label=catalina/lastBuild/artifact/build/doc/doxygen/doxygen-error.log).

See the documentation for the [latest release](https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/release/latest/html/index.html).

View the [doxygen log](https://abibuilder.informatik.uni-tuebingen.de/jenkins/job/openms_release_packaging/lastBuild/compiler=appleclang-7.3.0,os_label=elcapitan/artifact/build/doc/doxygen/doxygen-error.log).

## Contribution Guidelines

Before contributing to OpenMS, read information on the development model and conventions followed to maintain a coherent code base.

### Development model

OpenMS follows the [Gitflow development workflow](http://nvie.com/posts/a-successful-git-branching-model/).

Every contributor is encouraged to create their own fork (even if they are eligible to push directly to OpenMS). To create a fork:
1. Follow the documentation on [forking](https://help.github.com/articles/fork-a-repo).
2. Keep your fork [up-to-date](https://help.github.com/articles/syncing-a-fork).
3. Create a [pull request](https://help.github.com/articles/using-pull-requests). Before opening the pull request, please view the [checklist](pull-request-checklist.md).

### Coding conventions

See the manual for coding style recommended by OpenMS: [Coding conventions](https://github.com/OpenMS/OpenMS/wiki/Coding-conventions).
also see: [C++ Guide](https://github.com/OpenMS/OpenMS/wiki/Cpp-Guide).

View the [manual]() for creating a new build unit (to be completed).

OpenMS automatically tests for common coding convention violations using a modified version of `cpplint`.
Style testing can be enabled using `cmake` options. We also provide a configuration file for `Uncrustify` for automated style corrections (see `tools/uncrustify.cfg`).

### Commit messages

View the guidelines for commit messages: [How to write commit messages](https://github.com/OpenMS/OpenMS/wiki/HowTo---Write-Commit-Messages).

### Automated unit tests

Nightly tests run on different platforms. It is recommended to test on different platforms. This will save you time and surprises during continuous integration tests.

Nightly tests: [CDASH](http://cdash.openms.de/index.php?project=OpenMS)

## Further Contributor Resources

You may want to consider the following resources:
* **Guidelines for adding new dependency libraries**

  View the guidelines for [adding new dependency libraries]().
* **Experimental installers**

  We automatically build installers for different platforms. These usually contain unstable or partially untested code.

  The nightly (unstable) installers are available at the [build archive](https://abibuilder.informatik.uni-tuebingen.de/archive/openms/OpenMSInstaller/nightly/).
* **Developer FAQ**

  Visit the [Developer FAQ](developer-faq.md) to get answers to frequently asked questions.
