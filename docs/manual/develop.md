Developers
==========

To contribute to OpenMS:

- Familiarise yourself with the OpenMS technical documentation.
- Check out the [OpenMS tutorial for developers](https://abibuilder.cs.uni-tuebingen.de/archive/openms/Documentation/nightly/html/tutorial.html#tutorial_developing).

For any questions, please [contact us](/about/communication.md).

**New to the project?** Start with our [Contributor Onboarding Guide](https://openms.de/contribute) to understand project structure and communication channels.

**Ready to contribute code?** See [CONTRIBUTING.md](https://github.com/OpenMS/OpenMS/blob/develop/CONTRIBUTING.md) for workflow and process guidelines.

This guide covers technical details for active developers.

## Technical documentation

```{note}
Untested installers and containers are known as the {term}`nightly snapshot`, are released every night. They generally pass
automated continuous integration tests but no manual tests.
```

View the documentation for the nightly snapshot of [OpenMS develop branch](https://github.com/OpenMS/OpenMS/tree/develop)
at the [build archive](https://abibuilder.cs.uni-tuebingen.de/archive/openms/Documentation/nightly/html/index.html).

See the documentation for the [latest release](https://abibuilder.cs.uni-tuebingen.de/archive/openms/Documentation/release/latest/html/index.html).

## Contribution guidelines

For detailed contribution workflows, pull request checklists, issue reporting guidelines, and OpenMS-specific development processes, see the canonical [CONTRIBUTING.md](https://github.com/OpenMS/OpenMS/blob/develop/CONTRIBUTING.md) in the main repository.

This developer guide focuses on technical implementation details below.

### Coding conventions

See the manual for coding style recommended by OpenMS: [Coding conventions](https://abibuilder.cs.uni-tuebingen.de/archive/openms/Documentation/nightly/html/coding_conventions.html).

```{seealso}
[C++ Guide](https://abibuilder.cs.uni-tuebingen.de/archive/openms/Documentation/nightly/html/developer_faq.html).
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

Nightly tests: [CDASH](https://cdash.seqan.de/index.php?project=OpenMS).

## Further contributor resources

Consider the following resources for further information:

- **Guidelines for adding new dependency libraries**: View the guidelines for [adding new dependency libraries](/manual/develop/developer-guidelines-for-adding-new-dependent-libraries.md).
-  **Experimental installers**: We automatically build installers for different platforms. These usually contain
   unstable or partially untested code.
   The nightly (unstable) installers are available at the [build archive](https://abibuilder.cs.uni-tuebingen.de/archive/openms/OpenMSInstaller/nightly/).
- **Developer FAQ**: Visit the [Developer FAQ](/manual/develop/developer-faq.md) to get answers to frequently asked questions.

```{toctree}
:maxdepth: 1

develop/adding-new-tool-to-topp.md
develop/custom-compilation.md
develop/developer-guidelines-for-adding-new-dependent-libraries.md
develop/link-external-code-to-openms.md
develop/developer-faq.md

```
