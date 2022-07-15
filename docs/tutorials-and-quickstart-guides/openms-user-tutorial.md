OpenMS User Tutorial
====================

## General Remarks

- This handout will guide you through an introductory tutorial for the OpenMS/TOPP software package [1].

- OpenMS [2, 3] is a versatile open-source library for mass spectrometry data analysis. Based on this library, we offer a collection of command-line tools ready to be used by end users. These so-called TOPP tools (short for ”The OpenMS Pipeline”) [4] can be understood as small building blocks of arbitrarily complex data analysis workflows.

- In order to facilitate workflow construction, OpenMS was integrated into KNIME [5], the Konstanz Information Miner, an open-source integration platform providing a powerful and flexible workflow system combined with advanced data analytics, visualization, and report capabilities. Raw MS data as well as the results of data processing using TOPP can be visualized using TOPPView [6].

- This tutorial was designed for use in a hands-on tutorial session but can also be worked through at home using the online resources. You will become familiar with some of the basic functionalities of OpenMS/TOPP, TOPPView, as well as KNIME and learn how to use a selection of TOPP tools used in the tutorial workflows.

- All sample data referenced in this tutorial can be found in the
`C: / Example_Data` folder, on the USB stick that came with this tutorial, or released online on our GitHub repository `OpenMS/Tutorials`.

## Getting Started

### Installation

Before we get started, we will install OpenMS and KNIME. If you take part in a training session you will have likely received an USB stick from us that contains the required data and software. If we provide laptops with the software you may of course skip the installation process and continue reading the next section.

#### Installation from the OpenMS USB stick

Please choose the directory that matches your operating system and execute the installer.

For Windows, you call:

- The OpenMS installer: `Windows / OpenMS-2.7.0-Win64.exe`
- The KNIME installer: `Windows / KNIME-4.4.1-Installer-64bit.exe`
- OpenMS prerequisites (Windows-only): After installation, before your first use of the OpenMS plugin in KNIME, you will be asked to download it automatically if certain requirements are not found in your Windows registry. Alternatively, you can get a bundled version here or on the OpenMS USB stick (`Windows / OpenMS-2.7-prerequisites-installer.exe`).

On macOS, you call:

- The OpenMS installer: `Mac / OpenMS-2.7.0-macOS.dmg`
- The KNIME installer: `Mac / knime_4.4.1.app.macosx.cocoa.x86_64.dmg`

Afterwards, follow the instructions. For the OpenMS installation on macOS, accept the license and drag and drop  the OpenMS folder into your Applications folder.

```{note}
Due to increasing security measures for downloaded apps (e.g. path
randomization) on macOS you might need to open `TOPPView.app` and `TOPPAS.app` while holding <kbd>ctrl</kbd> and accept the warning. If the app still does not
open, you might need to move them from **Applications** > **OpenMS-2.7.0** to e.g. your Desktop and back.
```

#### Installation from the internet

### Data conversion

#### MSConvertGUI

#### msconvert

#### ThermoRawFileParser

### Data visualization using TOPPView

### Introduction to KNIME/OpenMS

#### Plugin and dependency installation

#### KNIME concepts

#### Overview of the graphical user interface

#### Creating workflows

#### Sharing workflows

#### Duplicating workflows

#### A minimal workflow

#### Digression: Working with chemical structures

#### Advanced topic: Metanodes

#### Advanced topic: R integration

## Label-free quantification of peptides

### Introduction

### Peptide identification

#### Bonus task: Identification using several search engines

### Quantification

### Combining quantitative information across several label-free experiments

#### Basic data analysis in KNIME

### Identification and quantification of the iPRG2015 data with subsequent MSstats analysis

#### Excursion MSstats

#### Dataset

#### Identification and quantification

#### Experimental design

#### Conversion and downstream analysis

#### Result

## Protein inference

### Extending the LFQ workflow by protein inference and quantification

### Statistical validation of protein inference results

#### Data preparation

#### ROC curve of protein ID

#### Posterior probability and FDR of protein IDs

## Isobaric analysis

### Isobaric analysis workflow

### Excursion MSstatsTMT

### Dataset and experimental design

#### MSstatsTMT analysis

### Note

## Label-free quantification of metabolites

### Introduction

### Basics of non-targeted metabolomics data analysis

### Basic metabolite identification

#### Convert your data into a KNIME table

#### Adduct grouping

#### Visualizing data

#### Spectral library search

#### Manual validation

#### De novo identification

### Downstream data analysis and reporting

#### Signal processing and data preparation for identification

#### Data preparation for quantification

#### Statistical analysis

#### Interactive visualization

#### Advanced visualization

#### Data preparation for reporting

## OpenSWATH

### Introduction

### Installation of OpenSWATH

### Installation of mProphet

### Generating the Assay Library

#### Generating TraML from transition lists

#### Appending decoys to a TraML file

### OpenSWATH KNIME

### From the example dataset to real-life applications

## OpenSWATH for Metabolomics

### Introduction

### Workflow

### Prerequisites

#### Windows

#### macOS

#### Linux

### Benchmark data

### Example workflow

### Run the workflow

### Important parameters

## An introduction to pyOpenMS

### Introduction

### Installation

#### Windows

#### macOS

#### Linux

#### IDE with Anaconda integration

### Build instructions

### Scripting with pyOpenMS

### Tool development with pyOpenMS

#### Basics

#### Loading data structures with pyOpenMS

#### Putting things together

#### Bonus task

## Quality control

### Introduction

### Building a qcML file per run

### Adding brand new QC metrics

### Set QC metrics

## Troubleshooting guide

### FAQ

#### How to debug KNIME and/or the OpenMS nodes?

#### General

#### Platform-specific problems

#### Nodes

### Sources of support

## References
