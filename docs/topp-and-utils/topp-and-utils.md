TOPP
====

**TOPP - The OpenMS Proteomics Pipeline** is a pipeline for the analysis of HPLC-MS data. It consists of several small
applications that can be chained to create analysis pipelines tailored for a specific problem.

The TOPP tools are divided into several subgroups, like graphical tools, file handling, signal processing and
preprocessing, quantitation, map alignment, protein/peptide identification, protein/peptide processing, targeted
experiments and OpenSWATH, peptide property prediction, cross-linking, quality-control, among a few.

Few of the graphical tools are explained below:

```{toctree}
:maxdepth: 1

toppview
toppas
ini-file-editor
swathwizard
```

For advanced documentation on every TOPP tool, see the [OpenMS TOPP API Reference](https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/nightly/html/TOPP_documentation.html).

UTILS
=====

Besides {term}`TOPP`, OpenMS offers range of other tools. They are not included in {term}`TOPP` as they are not part of
typical analysis pipelines. A set of command line utilities, similar to {term}`TOPP tools`, mostly used during pipeline
construction or parameter optimization.


```{seealso}

[UTILS documentation](https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/nightly/html/UTILS_documentation.html)

```

Let's explore one such utitliy tool:

```{toctree}
:maxdepth: 1

proteomicslfq
```
