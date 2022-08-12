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
as well as adapters to other state-of-the art tools like X!Tandem, :term:`Mascot`, etc. It supports easy integration of OpenMS built tools into workflow
engines like :term:`KNIME`, Galaxy, WS-Pgrade, and :term:`TOPPAS` via the :term:`TOPP tools` concept and
a unified parameter handling via a 'common tool description' (CTD) scheme.

.. important::
  As part of the **Center for Integrative Bioinformatics** (CiBi) in the **German Network for Bioinformatics**
  `deNBI <https://www.denbi.de/>`_,
  OpenMS is currently focusing the development efforts on the integration of OpenMS into KNIME. KNIME is a well-established
  data analysis framework that supports the generation of workflows for data analysis. Using a Common Tool Description
  (CTD) file which is writeable by every TOPP tool and a node generator program (`Generic KNIME Nodes <https://github.com/genericworkflownodes/GenericKnimeNodes>`_), all   :term:`TOPP tools` can be made available to run in KNIME.

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

   introduction/about-open-ms.md
   introduction/background.md
   introduction/how-openms-works.md

.. toctree::
   :maxdepth: 2
   :caption: Installation Guides

   installations/installation-on-gnu-linux.md
   installations/installation-on-macos.md
   installations/installation-on-windows.md

.. toctree::
   :maxdepth: 2
   :caption: OpenMS Applications and Tools

   openms-applications-and-tools/openms-graphical-user-interfaces.md
   openms-applications-and-tools/topp-tools.md
   openms-applications-and-tools/utils-tools.md
   openms-applications-and-tools/command-line-interface.md
   openms-applications-and-tools/visualize-with-openms.md

.. toctree::
   :maxdepth: 2
   :caption: Run Workflows with OpenMS Tools

   run-workflows-with-openms-tools/openms-in-knime.md
   run-workflows-with-openms-tools/openms-in-nextflow.md
   run-workflows-with-openms-tools/openms-on-galaxy.md

.. toctree::
   :maxdepth: 2
   :caption: Tutorials and Quick Start Guides

   tutorials-and-quickstart-guides/openms-user-tutorial.md
   tutorials-and-quickstart-guides/tutorials.md
   tutorials-and-quickstart-guides/untargeted_metabolomics_preprocessing.md
   tutorials-and-quickstart-guides/quickstart-guides.md

.. toctree::
   :maxdepth: 2
   :caption: Develop with OpenMS

   develop-with-openms/openms-core-cplusplus-library.md
   OpenMS API Reference <https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/nightly/html/index.html>
   pyOpenMS <https://pyopenms.readthedocs.io/en/latest/>
   develop-with-openms/build-openms-from-source.md
   develop-with-openms/link-external-code-to-openms.md
   develop-with-openms/developer-tutorial.md

.. toctree::
   :maxdepth: 2
   :caption: Contribute to OpenMS

   contribute-to-openms/openms-git-workflow.md
   contribute-to-openms/write-and-label-github-issues.md
   contribute-to-openms/adding-new-tool-to-topp.md
   contribute-to-openms/pull-request-checklist.md
   contribute-to-openms/reporting-bugs-and-issues.md
   contribute-to-openms/advanced.md

.. toctree::
   :maxdepth: 2
   :caption: Downloads

   downloads.md

.. toctree::
   :maxdepth: 2
   :caption: Quick Reference

   quick-reference/contributor-faq.md
   quick-reference/developer-faq.md
   quick-reference/contact-us.md
   quick-reference/glossary.md

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
