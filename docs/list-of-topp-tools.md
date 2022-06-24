List of TOPP and UTILS Tools
==================

The following TOPP tools are available:

- **File conversion**

  OpenMS file handling tools can be used to convert files into a supported format.
- **File handling**
- **Centroiding**

  The conversion of the "raw" ion count data acquired by the machine into peak lists for further processing is usually called peak picking or centroiding. The choice of the algorithm should mainly depend on the resolution of the data. OpenMS provides different algorithms for centroiding depending on the resolution of the data.

- **Spectrum processing**

  A number of spectrum processing tools are available. These include peak filtering and peak normalization tools, as well as other miscellaneous tools.

- **Mass correction and calibration**
- **Spectrum clustering**
- **Map alignment**

  When looking to identify molecules, it is common to run multiple experiments, where each experiment produces a set of data. In OpenMS, every set of data is represented by a feature map. Before combining feature maps to create a consensus map, it is advised to use OpenMS’s map alignment tools so that all your datasets are comparable and based on a common retention time axis. 

There are also a number of tools in the beta stage called UTILS. They include but are not limited to:
- **Signal processing and preprocessing**
- **File handling**
- **Algorithm evaluation**
- **Protein/peptide identification**
- **Cross-linking**
- **Quantitation**
- **Metabolite identification**
- **Targeted experiments and OpenSWATH**
- **RNA**
- **Quality control**

For the full list of UTILS tools, visit the [API Reference website](https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/nightly/html/UTILS_documentation.html).
