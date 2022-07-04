Introduction to TOPP
====================

**TOPP - The OpenMS Pipeline** is a set of tools for the analysis of HPLC-MS data. These tools can be either:

- [Executed from the command line](../openms-applications-and-tools/command-line-interface.md) or,
- Applied individually using OpenMS graphical applications.
- Applied in sequence as a workflow using a workflow editor such as KNIME, Nextflow or Galaxy.

Before you choose one of the above options, there are few concepts that need to be understood.

## File formats

OpenMS only accepts files in the following formats:

- **mzML**: The HUPO-PSI standard format for mass spectrometry data.
- **featureXML**: The OpenMS format for quantitation results.
- **consensusXML**: The OpenMS format for grouping features in one map or across several maps.
- **idXML**: The OpenMS format for protein and peptide identification.

Documented schemas of the OpenMS formats can be found [here](https://github.com/OpenMS/OpenMS/tree/develop/share/OpenMS/SCHEMAS).

If your data is not in the above formats, you may need to use one of a file conversion TOPP tool.

## TOPP INI files

TOPP INI files are XML-based files with an `.ini` extension. OpenMS uses TOPP INI files to set parameters for one or more TOPP tools. Alternatively, the command line can be used to set TOPP tool parameters.
Here is an example of a TOPP INI file:

  ```xml
  <PARAMETERS>

  <NODE name="FileFilter">
    <NODE name="1">
      <ITEM name="rt" value="0:1200" type="string"/>
    </NODE>
    <NODE name="2">
      <ITEM name="mz" value="700:1000" type="string"/>
    </NODE>
  </NODE>

  <NODE name="common">
    <NODE name="FileFilter">
      <ITEM name="rt" value=":" type="string"/>
      <ITEM name="mz" value=":" type="string"/>
    </NODE>
    <ITEM name="debug" value="2" type="int"/>
  </NODE>

  </PARAMETERS>
  ```
## Features, feature maps and featureXML files

An LC-MS feature is a construct in OpenMS that is used to describe a 2D peak caused by an analyte interacting with the stationary phase. Each feature contains the following metadata: an id, retention time, mass-to-charge ratio, intensity, overall quality and one or more convex hulls.   

A feature map is a container for features. One feature map can contain many features.

A featureXML file is an XML based file which contains one feature map.

FeatureXML files can be created from mzML files using OpenMS’s feature detection algorithms.

## Consensus feature, consensus maps, consensusXML files

A consensus feature is a special type of LC-MS feature that is quantified across multiple experiments. A consensus feature is formed by linking or grouping features with similar mass-to-charge ratios and intensities from various experiment runs. Each consensus feature references the features used to form the consensus feature.

Similar to a feature map, a consensus map is a container for consensus features. One consensus map can contain many consensus features.
