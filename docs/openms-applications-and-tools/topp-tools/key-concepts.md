Key Concepts
============

Before using TOPP tools, there are a number of concepts to understand. These include:
- **TOPP INI files**

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
- **Features, feature maps and featureXML files**

  An LC-MS feature is a construct in OpenMS that is used to describe a 2D peak caused by an analyte interacting with the stationary phase. Each feature contains the following metadata: an id, retention time, mass-to-charge ratio, intensity, overall quality and one or more convex hulls.   

  A feature map is a container for features. One feature map can contain many features.

  A featureXML file is an XML based file which contains one feature map.

  FeatureXML files can be created from mzML files using OpenMS’s feature detection algorithms.

- **Consensus feature, consensus maps, consensusXML files**

  A consensus feature is a special type of LC-MS feature that is quantified across multiple experiments. A consensus feature is formed by linking or grouping features with similar mass-to-charge ratios and intensities from various experiment runs. Each consensus feature references the features used to form the consensus feature.

  Similar to a feature map, a consensus map is a container for consensus features. One consensus map can contain many consensus features.
