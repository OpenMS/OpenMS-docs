OpenMS Applications
===================

OpenMS provides a suite of graphical applications, designed for users who want easy access to TOPP tools. These applications include:

- **INIFileEditor**

  A GUI application used to edit INI files. INI files are used to configure TOPP tool parameters. INI files are files with the extension `.ini`. For more information, read our [INIFile Editor](openms-applications/ini-file-editor.md) section.

- **TOPPView**

  A GUI application used to inspect, visualize and compare mass spectrometry data. Read more in-depth documentation about TOPPView. For more information, read our [TOPPView: Visualize with OpenMS](visualize-with-openms.md) section.

- **TOPPAS (deprecated)**

  A GUI application used to apply multiple tools sequentially on mass spectrometry data. Applying multiple tools in a sequence is referred to as a workflow or a pipeline. OpenMS no longer supports TOPPAS and instead recommends the use of [KNIME](https://www.knime.com/), for which we provide a community plugin.

- **SwathWizard**
  An application for SWATH analysis. SwathWizard is used to analyze DIA swath data. For mor information, read our [SwathWizard](openms-applications/swathwizard.md)


A typical workflow would consist of the following steps:

1. Edit the INI file in the INIFile Editor.
2. Import data into TOPPView.
3. Apply TOPP tool to data in TOPPView. You will need to load the INI file edited in step 1.
