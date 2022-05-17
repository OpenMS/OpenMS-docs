# For Developers

## Developing With OpenMS

To contribute to OpenMS, you should:

* Familiarize yourself with our [online documentation] (https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/release/latest/html/index.html).

* Learn how to [build OpenMS] (building-openms.md).

* Start reading the [OpenMS tutorial for developers] (https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/release/latest/html/OpenMS_tutorial.html).

* Direct any questions to the mailing list.

## OpenMS Tutorial For Developers

Please read the [OpenMS tutorial for developers] (https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/release/latest/html/OpenMS_tutorial.html)
that contains general information about the structure of OpenMS, the concepts
behind it and example code.

## Technical Documentation

See the documentation for the nightly snapshot of [develop] (https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/nightly/html/index.html) ([doxygen log] (https://abibuilder.informatik.uni-tuebingen.de/jenkins/job/openms_nightly_packaging/lastBuild/compiler=appleclang-7.3.0,os_label=elcapitan/artifact/build/doc/doxygen/doxygen-error.log)).

See the documentation for the latest [release] (https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/release/latest/html/index.html) ([doxygen log] (https://abibuilder.informatik.uni-tuebingen.de/jenkins/job/openms_release_packaging/lastBuild/compiler=appleclang-7.3.0,os_label=elcapitan/artifact/build/doc/doxygen/doxygen-error.log)).

## Development Model

OpenMS follows the Gitflow development workflow that [this post] (http://nvie.com/posts/a-successful-git-branching-model) excellently describes. We encourage every developer (even if they are eligible to push directly to OpenMS) to create their fork (e.g. @username). The GitHub people provide excellent documentation on [forking] (https://help.github.com/articles/fork-a-repo) and how to keep your [fork up-to-date] (https://help.github.com/articles/syncing-a-fork). With your fork, follow the Gitflow development model directly, but instead of merging into "develop" in your fork, open a [pull request ](https://help.github.com/articles/using-pull-requests). Before opening the pull request, please check the [checklist](https://github.com/OpenMS/OpenMS/wiki/Pull-Request-Checklist).

Some more details and tips are collected [here] (https://github.com/OpenMS/OpenMS/wiki/OpenMS-Git-Workflow).

## Coding Conventions

See the manual for proper coding style: [Coding conventions] (https://github.com/OpenMS/OpenMS/wiki/Coding-conventions).
Also see: [C++ Guide](http://https://github.com/OpenMS/OpenMS/wiki/Cpp-Guide).

See the [manual] (https://github.com/OpenMS/OpenMS/wiki/NewBuildUnit) for creating a new build unit (to be completed).

We automatically test for common coding convention violations using a modified version of `cpplint`.
Style testing can be enabled using CMake options. We also provide a configuration file for Uncrustify for automated style corrections (see `tools/uncrustify.cfg`).

## Commit Messages

To ease the creation of a CHANGELOG, we use a defined format for our commit messages.

See the manual for writing `commit` messages: [How to write `commit` messages] (http://https://github.com/OpenMS/OpenMS/wiki/HowTo---Write-Commit-Messages).

## Automated Unit Tests

We perform nightly test runs on different platforms. Even if everything compiled well on your machine and all tests have passed, please check if you broke another platform.

Nightly tests: [CDASH] (http://cdash.openms.de/index.php?project=OpenMS)

## Further Developer Resources

### Guidelines for the Addition of New Dependency Libraries

See [here] (https://github.com/OpenMS/OpenMS/wiki/Developer-Guidelines-for-adding-new-dependent-libraries).

### Experimental Installers

We automatically build installers for different platforms. These usually contain unstable or partially untested code, so use them at your own risk.

The nightly (unstable) installers are available [here] (https://abibuilder.informatik.uni-tuebingen.de/archive/openms/OpenMSInstaller/nightly/).

### Developer FAQ (Formerly Internal FAQ)

The [FAQ] (requires link) for developers is currently expanded and might contain answers to your questions.


