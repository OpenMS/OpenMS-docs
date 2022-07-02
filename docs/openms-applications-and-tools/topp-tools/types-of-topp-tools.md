Types of TOPP Tools
===================

The following tools are offered:

- **File conversion**

  TOPP file conversion tools can be used to convert files into a supported format. Supported formats include:
  - mzML
  - featureXML
  - consensusXML
  - idXML

- **File handling**

  TOPP file handling tools are largely used to extract or merge data.

- **Centroiding**

  The conversion of the "raw" ion count data acquired by the machine into peak lists for further processing is usually called peak picking or centroiding. The choice of the algorithm should mainly depend on the resolution of the data. OpenMS provides different algorithms for centroiding depending on the resolution of the data.
- **Spectrum processing**

  A number of spectrum processing tools are available. These include peak filtering and peak normalization tools, as well as other miscellaneous tools.

- **Mass correction and calibration**

  To ensure that your data is sound, OpenMS have provided a number of mass correction and calibration tools. The types of tools used will depend on the type of equipment you have employed.
- **Spectrum clustering**
- **Map alignment**

  When looking to identify molecules, it is common to run multiple experiments, where each experiment produces a set of data. In OpenMS, every set of data is represented by a feature map. Before combining feature maps to create a consensus map, it is advised to use OpenMS’s map alignment tools so that all your datasets are comparable and based on a common retention time axis.
- **Feature linking**

  OpenMS provides a number of algorithms for feature grouping or linking.
- **Quantitation**

  A number of tools are available that allow for the identification and quantification of features. The tools you use will depend on the type of mass spectrometry experiment you have set up, and the type of molecules you wish to identify.
- **Protein/Peptide identification**
- **Protein/Peptide processing**
- **Targeted experiments and OpenSWATH**
- **Peptide property prediction**

  A number of deep learning tools are available that can train a model using a number of data sets. These can be used to predict peptide properties such as…..
- **Cross-linking**
- **Quality control**

For the full list of TOPP tools, visit the [API website](https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/release/2.8.0/html/TOPP_documentation.html).
