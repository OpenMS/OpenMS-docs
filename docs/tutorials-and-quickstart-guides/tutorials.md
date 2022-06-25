Tutorials
=========

The following tutorials provide the opportunity to complete a real-world example while also seeing the different methods OpenMS makes available to complete the same task.

There are four ways to use OpenMS to complete a task. For example, say you want to read a file and store the information in an output file. You can do this by:

- **Using TOPP shell** to run a shell script or execute a command directly.
- **Using pyOpenMS** and creating and running a python script.
- **Using TOPPView**, a graphical user interface provided by OpenMS.
- **Constructing a workflow in KNIME**, which can be saved and executed on multiple input files

The following sections explain how to read a file and store the information in an output file using these four different methods.

## Using TOPP shell

As explained in the command-line quick start guide, TOPP shell is available for those who are comfortable with executing command line tools and writing scripts.

To read the information of a file, you can just type the following in the command line and press <kbd>Enter</kbd>.

```bash
FileInfo -in <insert input file> -out <insert output file>
```

You can also copy and paste this into a shell script (file with an .sh extension), and then type bash <insert file> in the command line to execute the script.

## Using pyOpenMS

You can replicate the functionality of the `FileInfo` TOPP tool in pyOpenMS, using one of the following examples, depending on the type of file you want to get information about.

- Example for `mzML` file

  ```python
  from pyopenms import *

  exp = MSExperiment()
  MzMLFile().load("sample.mzML", exp)
  exp.updateRanges()

  ms_levels = exp.getMSLevels()
  num_spectra = {level: 0 for level in ms_levels}

  for spec in exp:
     num_spectra[spec.getMSLevel()] += 1

  print("Instrument:")
  for analyzer in exp.getInstrument().getMassAnalyzers():
     print(f"\tMass Analyzer: {analyzer.getType()} (resolution: {analyzer.getResolution()})")

  print("\nMS levels: "+", ".join([str(level) for level in ms_levels]))
  print(f"Total number of peaks: {sum([spec.size() for spec in exp])}")
  print(f"Total number of spectra: {exp.size()}")

  print("\nRanges:")
  print(f"\tretention time: {exp.getMinRT()} .. {exp.getMaxRT()} ({round((exp.getMaxRT()-exp.getMinRT())/60, 2)} min)")
  print(f"\tmass-to-charge: {exp.getMinMZ()} .. {exp.getMaxMZ()}")
  print(f"\tintensity: {exp.getMinIntensity()} .. {exp.getMaxIntensity()}")

  print("\nNumber of spectra per MS level:")
  for level, number in num_spectra.items():
     print(f"\tlevel {level}: {number}")
  ```
  - Example for `featureXML` file

  ```python
  feature_map = FeatureMap()
  FeatureXMLFile().load("sample.featureXML", feature_map)

  charges = {}
  number_of_ids = {}
  tic = 0

  for feature in feature_map:
     charge = feature.getCharge()
     if charge in charges.keys():
         charges[charge] += 1
     else:
         charges[charge] = 1
     num_ids = len(feature.getPeptideIdentifications())
     if num_ids in number_of_ids.keys():
         number_of_ids[num_ids] += 1
     else:
         number_of_ids[num_ids] = 1
     tic += feature.getIntensity()

  print(f"Number of features: {feature_map.size()}")

  print("\nRanges:")
  print(f"\tretention time: {feature_map.getMinRT()} .. {feature_map.getMaxRT()} ({round((feature_map.getMaxRT()-feature_map.getMinRT())/60, 2)} min)")
  print(f"\tmass-to-charge: {feature_map.getMinMZ()} .. {feature_map.getMaxMZ()}")
  print(f"\tintensity: {feature_map.getMinIntensity()} .. {feature_map.getMaxIntensity()}")

  print(f"\nTotal ion current in features: {int(tic)}")

  print("\nCharge distribution:")
  for charge, occurence in charges.items():
     print(f"\tcharge {charge}: {occurence}x")

  print("\nDistribution of peptide identifications (IDs) per feature:")
  for num_ids, occurence in number_of_ids.items():
     print(f"\t{num_ids} IDs: {occurence}")

  print(f"\nUnassigned peptide identifications: {len(feature_map.getUnassignedPeptideIdentifications())}")
  ```

## Using TOPPView

If you want a graphical interface to interact with, then use TOPPView. Follow these steps to read the file information using TOPPView:

1. Go to **File** > **Open file** and open a file by following the prompts.
2. Go to **Tools** > **Apply TOPP tool (whole layer)**.
3. Set **TOPP tool** to **FileInfo** and **output argument** to **out**.
4. Load an existing INI file by clicking **Load** and selecting an INI file from the file importer. If you don’t have an INI file, click **Store**, enter a file name and click **OK **to generate an INI file, then click **Load** and load the file.
5. Click **OK**.
6. Open the **Log** panel at the bottom of the screen to view the resulting file information.

## Constructing a workflow in KNIME

KNIME is available for those who want a graphical application to create and use workflows. Here is an example of how to report file information on an input file to an output file using KNIME.

1. Install OpenMS plugin.
   <ol type="a">
    <li>Go to **File** > **Install KNIME Extensions**.</li>
    <li>Search for **OpenMS**.</li>
    <li>Select the checkbox next to **OpenMS** and click **Next**.</li>
    <li>Click **Next**.</li>
    <li>Accept the terms of conditions.</li>
    <li>Restart KNIME</li>
   </ol>
2. Open a new file by going to **File** > **New file**.

![drag-and-drop-node](../images/tutorials/knime/add-node-to-workspace.gif)
