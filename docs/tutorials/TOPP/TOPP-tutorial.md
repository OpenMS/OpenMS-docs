TOPP Tutorial
============

The following tutorial is an introduction to {term}`TOPP` and {term}`TOPPView`. Let's start with understanding the intent and
concept of {term}`TOPP` compared to OpenMS. Later, we will move to the handling of {term}`TOPPView` which is our central
GUI. Apart from viewing data, {term}`TOPPView` can also be used to analyze it using selected {term}`TOPP tools`; how-to
is explained in the third part of the tutorial.

Finally, the tutorial lists the command line interfaces for all TOPP tools contained in the release.

# Concepts

Let's understand the intent of [TOPP and OpenMS](topp-and-openms-introduction.md).

```{toctree}
:maxdepth: 1

topp-and-openms-introduction
```

# TOPPView Main Interface

In the following section, we will learn about the main features of {term}`TOPPView` and its basic uses.

```{toctree}
:maxdepth: 1

toppview-introduction
views-in-toppview
display-modes-and-view-options
data-analysis-in-toppview
data-editing-in-toppview
hotkeys-table
```

# Calling TOPP tools from TOPPView

The following part of the tutorial illustrates how to interactively analyse {term}`proteomics` data using {term}`TOPP tools` from
within {term}`TOPPView`.

```{toctree}
:maxdepth: 1

smoothing-raw-data
subtracting-a-baseline-from-a-spectrum
picking-peaks
feature-detection-on-centroided-data
```

# Advanced Users: Tips & Tricks

Read [TOPP for Advanced Users](topp-for-advanced-users.md) to know more about how to use advanced functionalities,
increasing productivity.

```{toctree}
:maxdepth: 1

topp-for-advanced-users
```

# Scripting with TOPP

This part of the tutorial gives a detailed overview of the most important {term}`TOPP tools`. First, some basics needed
for every {term}`TOPP tool` are explained, then several example pipelines are shown.

```{toctree}
:maxdepth: 1

general-introduction
file-handling
profile-data-processing
calibration
map-alignment
feature-detection
feature-grouping
consensus-peptide-identification
peptide-property-prediction
quality-control
conversion-between-openms-xml-formats-and-text-formats
```
