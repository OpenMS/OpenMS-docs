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
engines like :term:`KNIME`, Galaxy, WS-Pgrade, and :term:`TOPPAS` via the :term:`TOPP tools` concept and
a unified parameter handling via a 'common tool description' (CTD) scheme.

.. important::
As part of the **Center for Integrative Bioinformatics** (CiBi) in the **German Network for Bioinformatics**
`deNBI <https://www.denbi.de/>`_,
OpenMS is currently focusing the development efforts on the integration of OpenMS into KNIME. KNIME is a well-established
data analysis framework that supports the generation of workflows for data analysis. Using a Common Tool Description
(CTD) file which is writeable by every TOPP tool and a node generator program (`Generic KNIME Nodes <https://github.com/genericworkflownodes/GenericKnimeNodes>`_), all :term:`TOPP tools` can be made available to run in KNIME.


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
   tutorials/KNIME/KNIME-tutorial

.. toctree::
   :maxdepth: 2
   :caption: OpenMS TOPP Tools

   topp/topp.md
   topp/adding-new-tool-to-topp.md

.. toctree::
   :maxdepth: 2
   :caption: Developer Resources

   additional-resources/developer-guidelines-for-addding-new-dependent-libraries.md
   additional-resources/external-code-using-openms.md
   advanced-resources/custom-compilation.md
   advanced-resources/build-custom-openms-knime-package.md

.. toctree::
   :maxdepth: 2
   :caption: OpenMS GitHub Workflow

   additional-resources/openms-git-workflow.md
   additional-resources/reporting-bugs-and-issues.md
   additional-resources/write-and-label-github-issues.md
   additional-resources/pull-request-checklist.md

.. toctree::
   :maxdepth: 2
   :caption: Frequently Asked Questions

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
