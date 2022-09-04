OpenMS Graphical User Interfaces
================================

OpenMS provides a suite of graphical user interfaces, designed for users who want easy access to TOPP tools. These interfaces include:

- **INIFileEditor**

  A GUI application used to edit TOPP INI files. TOPP INI files are used to configure TOPP tool parameters. TOPP INI files are files with the extension `.ini`. For more information, read our [INIFile Editor](openms-applications/ini-file-editor.md) section.

- **TOPPView**

  A GUI application used to inspect, visualize and compare mass spectrometry data. For more information, read our [TOPPView: Visualize with OpenMS](visualize-with-openms.md) section.

- **TOPPAS (deprecated)**

  A GUI application used to apply multiple tools sequentially on mass spectrometry data. Applying multiple tools in a sequence is referred to as a workflow or a pipeline. OpenMS no longer supports TOPPAS and instead recommends the use of [KNIME](https://www.knime.com/), for which we provide a community plugin.

- **SwathWizard**
  An application for SWATH analysis. SwathWizard is used to analyze DIA swath data. For more information, read our [SwathWizard](openms-applications/swathwizard.md) section.


A possible workflow would consist of the following steps:

1. Generate a TOPP INI file from the [command line](command-line-interface.md).
2. Edit the TOPP INI file in the INIFile Editor.
3. Import data into TOPPView.
4. Apply TOPP tool to data in TOPPView. You will need to load the TOPP INI file edited in step 1.
