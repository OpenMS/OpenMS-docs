Contributor's Quick Start Guide
===============================

To contribute to OpenMS:

- Familiarise yourself with the [OpenMS online documentation](../index.rst).
- Learn how to [build OpenMS](../installations/build-openms-from-source.md).
- Check out the [OpenMS tutorial for developers](https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/release/latest/html/OpenMS_tutorial.html).

For any questions, please [contact us](../contact-us.md).

## Technical documentation

```{note}
Untested installers and containers are known as the {term}`nightly snapshot`, are released every night. They generally pass
automated continuous integration tests but no manual tests.
```

View the documentation for the nightly snapshot of [OpenMS develop branch](https://github.com/OpenMS/OpenMS/tree/develop)
at the [build archive](https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/nightly/html/index.html).

See the documentation for the [latest release](https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/release/latest/html/index.html).

## Contribution guidelines

Before contributing to OpenMS, read information on the development model and conventions followed to maintain a coherent
code base.

### Development model

OpenMS follows the [Gitflow development workflow](http://nvie.com/posts/a-successful-git-branching-model/).

Every contributor is encouraged to create their own fork (even if they are eligible to push directly to OpenMS).
To create a fork:

1. Follow the documentation on [forking](https://help.github.com/articles/fork-a-repo).
2. Keep your fork [up-to-date](https://help.github.com/articles/syncing-a-fork).
3. Create a [pull request](https://help.github.com/articles/using-pull-requests). Before opening the pull request, please
   view the [pull request guidelines](../additional-resources/pull-request-checklist.md).

### Coding conventions

See the manual for coding style recommended by OpenMS: [Coding conventions](https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/nightly/html/coding_conventions.html).

```{seealso}
[C++ Guide](https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/nightly/html/developer_faq.html).
```

OpenMS automatically tests for common coding convention violations using a modified version of `cpplint`.
Style testing can be enabled using `cmake` options. [clang-format](https://github.com/OpenMS/OpenMS/blob/develop/.clang-format) is used for formatting the cpp code.

### Commit messages

View the guidelines for commit messages: [How to write commit messages](https://github.com/OpenMS/OpenMS/wiki/HowTo---Write-Commit-Messages).

### Automated unit tests

Nightly tests run on different platforms. It is recommended to test on different platforms.

```{tip}
This saves time and increases productivity during continuous integration tests.
```

Nightly tests: [CDASH](http://cdash.openms.de/index.php?project=OpenMS).

## Further contributor resources

Consider the following resources for further information:

- **Guidelines for adding new dependency libraries**: View the guidelines for [adding new dependency libraries](../additional-resources/developer-guidelines-for-addding-new-dependent-libraries.md).
-  **Experimental installers**: We automatically build installers for different platforms. These usually contain
   unstable or partially untested code.
   The nightly (unstable) installers are available at the [build archive](https://abibuilder.informatik.uni-tuebingen.de/archive/openms/OpenMSInstaller/nightly/).
- **Developer FAQ**: Visit the [Developer FAQ](../faqs/developer-faq.md) to get answers to frequently asked questions.
