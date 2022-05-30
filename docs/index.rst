About OpenMS
============

`OpenMS <http://www.openms.org/>`_
is an open-source software C++ library for LC-MS data management and
analyses. It offers an infrastructure for rapid development of mass
spectrometry related software. OpenMS is free software available under the
three clause BSD license and runs under Windows, macOS, and Linux.

It comes with a vast variety of pre-built and ready-to-use tools for proteomics
and metabolomics data analysis (TOPPTools) as well as powerful 1D, 2D and 3D
visualization (TOPPView).

OpenMS offers analyses for various quantitation protocols, including label-free
quantitation, SILAC, iTRAQ, TMT, SRM, SWATH, etc.

It provides built-in algorithms for de-novo identification and database search,
as well as adapters to other state-of-the art tools like X!Tandem, Mascot,
OMSSA, etc. It supports easy integration of OpenMS built tools into workflow
engines like KNIME, Galaxy, WS-Pgrade, and TOPPAS via the TOPPtools concept and
a unified parameter handling via a 'common tool description' (CTD) scheme.

With pyOpenMS, OpenMS offers Python bindings to a large part of the OpenMS API
to enable rapid algorithm development. OpenMS supports the Proteomics Standard
Initiative (PSI) formats for MS data. The main contributors of OpenMS are
currently the Eberhard-Karls-Universität in Tübingen, the Freie Universität
Berlin, and the ETH Zürich.

Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: Introduction

   introduction

.. toctree::
   :maxdepth: 2
   :caption: Getting Started

   installations/installation-on-gnu-linux
   installations/installation-on-windows
   installations/installation-on-macos
   installations/build-openms-from-source

.. toctree::
   :maxdepth: 2
   :caption: Quick Start Guides

   guides/user-guides/user-quickstart-guide
   guides/contributors-quickstart-guide.md

.. toctree::
   :maxdepth: 2
   :caption: Tutorials

   tutorials/TOPP/TOPP-tutorial
   tutorials/TOPPAS/TOPPAS-tutorial

.. toctree::
   :maxdepth: 2
   :caption: OpenMS TOPP Tools

   topp/topp.md
   topp/adding-new-tool-to-topp.md

.. toctree::
   :maxdepth: 2
   :caption: Frequently Asked Questions

   faqs/developer-faq.md
   faqs/contributor-faq.md

.. toctree::
   :maxdepth: 2
   :caption: Advanced Resources

   advanced-resources/custom-compilation.md
   advanced-resources/build-custom-openms-knime-package.md

.. toctree::
   :maxdepth: 2
   :caption: Additional Resources

   additional-resources/developer-guidelines-for-adding-new-dependent-libraries.md
   additional-resources/external-code-using-openms.md
   additional-resources/openms-git-workflow.md
   additional-resources/reporting-bugs-and-issues.md
   additional-resources/write-and-label-github-issues.md
   additional-resources/pull-request-checklist.md

.. toctree::
   :maxdepth: 2
   :caption: Downloads

   downloads.md

.. toctree::
   :maxdepth: 2
   :caption: Glossary

   glossary.md

.. toctree::
   :maxdepth: 2
   :caption: Contact Us

   contact-us


Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
