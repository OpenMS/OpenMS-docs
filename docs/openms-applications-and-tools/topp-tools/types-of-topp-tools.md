Types of TOPP Tools
===================

The following tools are offered:

- **File conversion**

  TOPP file conversion tools can be used to convert files into a supported format.

- **File handling**

  TOPP file handling tools are largely used to extract or merge data. For more information, view the [File handling](types-of-topp-tools/file-handling.md).

- **Centroiding**

  The conversion of the "raw" ion count data acquired by the machine into peak lists for further processing is usually called peak picking or centroiding. The choice of the algorithm should mainly depend on the resolution of the data. OpenMS provides different algorithms for centroiding depending on the resolution of the data. For more information, view the [Picking peaks](types-of-topp-tools/picking-peaks.md) section.

- **Spectrum processing**

  A number of spectrum processing tools are available. These include peak filtering and peak normalization tools, as well as other miscellaneous tools.

- **Mass correction and calibration**

  To ensure that your data is sound, OpenMS have provided a number of mass correction and calibration tools. The types of tools used will depend on the type of equipment you have employed. For more information, view the [Calibration](types-of-topp-tools/calibration.md) section.

- **Spectrum clustering**

  Spectrum clustering is the grouping of spectra that have many peaks in common. OpenMS provides tools for spectrum clustering to identify molecules in large datasets more efficiently.

- **Map alignment**

  When looking to identify molecules, it is common to run multiple experiments, where each experiment produces a set of data. In OpenMS, every set of data is represented by a feature map. Before combining feature maps to create a consensus map, it is advised to use OpenMS’s map alignment tools so that all your datasets are comparable and based on a common retention time axis. For more information, view the [Map alignment](types-of-topp-tools/map-alignment.md) section.

- **Feature linking**

  OpenMS provides a number of algorithms for feature grouping or linking. For more information, view the [Feature grouping](types-of-topp-tools/feature-grouping.md) section.
- **Quantitation**

  A number of tools are available that allow for the identification and quantification of features. The tools you use will depend on the type of mass spectrometry experiment you have set up, and the type of molecules you wish to identify. For more information, view the [Feature detection](types-of-topp-tools/feature-detection.md) and [Feature detection on centroided data](types-of-topp-tools/feature-detection-on-centroided-data.md) sections.

- **Protein/Peptide identification**
- **Protein/Peptide processing**
- **Targeted experiments and OpenSWATH**
- **Peptide property prediction**

  For more information, view the [Peptide property prediction](types-of-topp-tools/peptide-property-prediction.md) section.
- **Cross-linking**

  Cross-linking is a technique where substances are chemically treated to create covalent bonds between different molecules. The strength of the covalent bonds can be quantified to indicate the proximity of certain molecules within a 3D structure.
- **Quality control**

  OpenMS provides tools to measure the quality of LC-MS data. For more information, view the [Quality control](types-of-topp-tools/quality-control.md) section.

For the full list of TOPP tools, visit the [API reference](https://abibuilder.cs.uni-tuebingen.de/archive/openms/Documentation/nightly/html/index.html) website.
