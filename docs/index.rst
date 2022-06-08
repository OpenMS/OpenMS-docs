About OpenMS
============

`OpenMS <http://www.openms.org/>`_
is an open-source software C++ library for :term:`LC-MS` data management and
analyses. It offers an infrastructure for rapid development of mass
spectrometry related software. OpenMS is free software available under the
three clause BSD license and runs under Windows, macOS, and Linux.

It comes with a vast variety of pre-built and ready-to-use tools for proteomics
and metabolomics data analysis (:term:`TOPP Tools`) as well as powerful 1D, 2D and 3D
visualization (:term:`TOPPView`).

OpenMS offers analyses for various quantitation protocols, including label-free
quantitation, :term:`SILAC`, :term:`iTRAQ`, :term:`TMT`, :term:`SRM`, :term:`SWATH`, etc.

It provides built-in algorithms for de-novo identification and database search,
as well as adapters to other state-of-the art tools like X!Tandem, :term:`Mascot`,
OMSSA, etc. It supports easy integration of OpenMS built tools into workflow
engines like :term:`KNIME`, Galaxy, WS-Pgrade, and :term:`TOPPAS` via the TOPPtools concept and
a unified parameter handling via a 'common tool description' (CTD) scheme.

With :term:`pyOpenMS`, OpenMS offers Python bindings to a large part of the :term:`OpenMS API`
to enable rapid algorithm development. OpenMS supports the Proteomics Standard
Initiative (PSI) formats for MS data. The main contributors of OpenMS are
currently the Eberhard-Karls-Universität in Tübingen, the Freie Universität
Berlin, and the ETH Zürich.

Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: Introduction
   :titlesonly:

   introduction

.. toctree::
   :maxdepth: 2
   :caption: Getting Started
   :titlesonly:

   installations/installation-on-gnu-linux
   installations/installation-on-windows
   installations/installation-on-macos
   installations/build-openms-from-source

.. toctree::
   :maxdepth: 2
   :caption: Quick Start Guides
   :titlesonly:

   guides/user-guides/user-quickstart-guide
   guides/contributors-quickstart-guide.md

.. toctree::
   :maxdepth: 2
   :caption: Tutorials
   :titlesonly:

   tutorials/TOPP/TOPP-tutorial
   tutorials/TOPPAS/TOPPAS-tutorial

.. toctree::
   :maxdepth: 2
   :caption: OpenMS TOPP Tools
   :titlesonly:

   topp/topp.md
   topp/adding-new-tool-to-topp.md

.. toctree::
   :maxdepth: 2
   :caption: Developer Resources
   :titlesonly:

   additional-resources/developer-guidelines-for-addding-new-dependent-libraries.md
   additional-resources/external-code-using-openms.md
   advanced-resources/custom-compilation.md
   advanced-resources/build-custom-openms-knime-package.md

.. toctree::
   :maxdepth: 2
   :caption: OpenMS GitHub Workflow
   :titlesonly:

   additional-resources/openms-git-workflow.md
   additional-resources/reporting-bugs-and-issues.md
   additional-resources/write-and-label-github-issues.md
   additional-resources/pull-request-checklist.md

.. toctree::
   :maxdepth: 2
   :caption: Frequently Asked Questions
   :titlesonly:

   faqs/developer-faq.md
   faqs/contributor-faq.md


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
