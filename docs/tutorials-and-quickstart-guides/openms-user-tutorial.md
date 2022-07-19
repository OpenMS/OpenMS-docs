OpenMS User Tutorial
====================

## General Remarks

- This handout will guide you through an introductory tutorial for the OpenMS/TOPP software package[^1].

- OpenMS[^2]<sup>,</sup>[^3] is a versatile open-source library for mass spectrometry data analysis. Based on this library, we offer a collection of command-line tools ready to be used by end users. These so-called TOPP tools (short for ”The OpenMS Pipeline”)[^4] can be understood as small building blocks of arbitrarily complex data analysis workflows.

- In order to facilitate workflow construction, OpenMS was integrated into KNIME[^5], the Konstanz Information Miner, an open-source integration platform providing a powerful and flexible workflow system combined with advanced data analytics, visualization, and report capabilities. Raw MS data as well as the results of data processing using TOPP can be visualized using TOPPView[^6].

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
On Linux, you can extract KNIME to a folder of your choice and for TOPPView you need to install OpenMS via your package manager or build it on your own with the instructions under the [API reference](www.openms.de/documentation) website.

```{note}
If you have installed OpenMS on Linux or macOS via your package
manager (for instance by installing the `OpenMS-2.7.0-Linux.deb` package),
then you need to set the `OPENMS_DATA_PATH` variable to the directory containing the shared data (normally `/usr/share/OpenMS`). This must be done prior to running any TOPP tool.
```
#### Installation from the internet

If you are working through this tutorial at home, you can get the installers under the following links:

- [OpenMS](https://www.openms.de/download/openms-binaries)
- [KNIME](https://www.knime.org/downloads/overview)
- OpenMS prerequisites (Windows-only): After installation, before your first use
of the OpenMS plugin in KNIME you will be asked to download it automatically
if certain requirements are not found in your Windows registry. Alternatively,
you can get a bundled version here.

Choose the installers for the platform you are working on.

### Data conversion

Each MS instrument vendor has one or more formats for storing the acquired data.
Converting these data into an open format (preferably mzML) is the very first step
when you want to work with open-source mass spectrometry software. A freely available conversion tool is MSConvert, which is part of a `ProteoWizard` installation. All files
used in this tutorial have already been converted to mzML by us, so you do not need
to perform the data conversion yourself. However, we provide a small raw file so you
can try the important step of raw data conversion for yourself.

Go to <a href="#Figure_1">Figure 1</a>

```{note}
The OpenMS installation package for Windows automatically installs
ProteoWizard, so you do not need to download and install it separately. Due
to restrictions from the instrument vendors, file format conversion for most
formats is only possible on Windows systems. In practice, performing the
conversion to mzML on the acquisition PC connected to the instrument is
usually the most convenient option.
```
To convert raw data to mzML using `ProteoWizard` you can either use MSConvertGUI (a
graphical user interface) or `msconvert` (a simple command line tool).

(Figure_1)=
|![msconvertgui](../images/openms-user-tutorial/introduction/proteowizard.png)|
|:--:|
|Figure 1: `MSConvertGUI` (part of `ProteoWizard`), allows converting raw files to mzML. Select the raw files you want to convert by clicking on the browse button and then on Add. Default parameters can usually be kept as-is. To reduce the initial data size, make sure that the `peakPicking` filter (converts profile data to centroided data (see Fig. 2)) is listed, enabled (true) and applied to all MS levels (parameter ”1-”). Start the conversion process by clicking on the Start button.|

Both tools are
available in: `C: / Program Files / OpenMS-2.7.0 / share / OpenMS / THIRDPARTY / pwiz-bin`.

You can find a small RAW file on the USB stick `C: / Example_Data Introduction
datasets/raw`.

#### MSConvertGUI

`MSConvertGUI` (see Fig. 1) exposes the main parameters for data conversion in a convenient graphical user interface.

#### msconvert

The `msconvert` command line tool has no user interface but offers more options than the application `MSConvertGUI`. Additionally, since it can be used within a batch script, it allows converting large numbers of files and can be much more easily automatized.
To convert and pick the file `raw_data_file.RAW` you may write:

```bash
msconvert raw_data_file.RAW --filter ”peakPicking true 1-”
```

in your command line.

|![profile centroided](../images/openms-user-tutorial/introduction/profilecentroided.png)|
|:--:|
|Figure 2: The amount of data in a spectra is reduced by peak picking. Here a profile spectrum (blue) is converted to centroided data (green). Most algorithms from this point on will work with centroided data.|

To convert all RAW files in a folder may write:

```bash
msconvert *.RAW -o my_output_dir
```

```{note}
To display all options you may type `msconvert --help` . Additional information is available on the `ProteoWizard` web page.
```

#### ThermoRawFileParser

Recently the open-source platform independent ThermoRawFileParser tool has been developed. While Proteowizard and MSConvert are only available for Windows systems this new tool allows to also convert raw data on Mac or Linux.

```{note}
To learn more about the ThermoRawFileParser and how to use it in
KNIME see Section 2.4.7
```
### Data visualization using TOPPView

Visualizing the data is the first step in quality control, an essential tool in understanding the data, and of course an essential step in pipeline development. OpenMS provides a convenient viewer for some of the data: TOPPView. We will guide you through some of the basic features of TOPPView. Please familiarize yourself with the key controls and visualization methods. We will make use of these later throughout the tutorial. Let’s start with a first look at one of the files of
our tutorial data set. Note that conceptually, there are no differences in visualizing metabolomic or proteomic data. Here, we inspect a simple proteomic measurement:

|![TOPPView](../images/openms-user-tutorial/introduction/TOPPView.png)|
|:--:|
|Figure 3: TOPPView, the graphical application for viewing mass spectra and analysis results. Top window shows a small region of a peak map. In this 2D representation of the measured spectra, signals of eluting peptides are colored according to the raw peak intensities. The lower window displays an extracted spectrum (=scan) from the peak map. On the right side, the list of spectra can be browsed.|

|![TOPPView](../images/openms-user-tutorial/introduction/3dview.png)|
|:--:|
|Figure 4: 3D representation of the measured spectra, signals of eluting peptides arecolored according to the raw peak intensities.|

- Start TOPPView (see Windows' Start-Menu or **Applications** > **OpenMS-2.7.0** on macOS)

- Go to **File** > **Open File**, navigate to the directory where you copied the contents
of the USB stick to, and select **Example_Data** > **Introduction** > **datasets** > **small** > **velos005614.mzML**. This file contains only a reduced LC-MS map of a label-free proteomic platelet measurement recorded on an Orbitrap velos. The other two mzML files contain technical replicates of this experiment. First, we want to
obtain a global view on the whole LC-MS map - the default option Map view 2D
is the correct one and we can click the <kbd>Ok</kbd> button.

- Play around.

- Three basic modes allow you to interact with the displayed data: scrolling, zooming and measuring:
  - **Scroll mode**
    - Is activated by default (though each loaded spectra file is displayed
zoomed out first, so you do not need to scroll).
    - Allows you to browse your data by moving around in RT and m/z range.
    - When zoomed in, you can scroll through the spectra. Click-drag on the current view.
    - Arrow keys can be used to scroll the view as well.
  - **Zoom mode**
    - Zooming into the data; either mark an area in the current view with
your mouse while holding the left mouse button plus the <kbd>Ctrl</kbd> key to
zoom to this area or use your mouse wheel to zoom in and out.
    - All previous zoom levels are stored in a zoom history. The zoom history
can be traversed using <kbd>Ctrl</kbd> + <kbd>+</kbd> or <kbd>Ctrl</kbd> + <kbd>-</kbd> or the mouse wheel (scroll up and down).
    - Pressing backspace <kbd>←</kbd> zooms out to show the full LC-MS map (and
also resets the zoom history).
  - **Measure mode**
    - It is activated using the <kbd>⇧</kbd>(shift) key.
    - Press the left mouse button down while a peak is selected and drag
the mouse to another peak to measure the distance between peaks.
    - This mode is implemented in the 1D and 2D mode only.
- Right click on your 2D map and select **Switch to 3D mode** and examine your data in 3D mode (see Fig. 4).
- Go back to the 2D view. In 2D mode, visualize your data in different intensity normalization modes, use linear , percentage, snap and log-view (icons on
the upper left tool bar). You can hover over the icons for additional information.

  ```{note}
  On macOS, due to a bug in one of the external libraries used by
  OpenMS, you will see a small window of the 3D mode when switching
  to 2D. Close the 3D tab in order to get rid of it.
  ```
- In TOPPView you can also execute TOPP tools. Go to **Tools** > **Apply tool (whole layer)**
and choose a TOPP tool (e.g., `FileInfo`) and inspect the results.

Dependent on your data MS/MS spectra can be visualized as well (see Fig.5) . You can
do so, by double-click on the MS/MS spectrum shown in scan view

|![ms2 spectrum](../images/openms-user-tutorial/introduction/ms2_introduction.png)|
|:--:|
|Figure 5: MS/MS spectrum|

### Introduction to KNIME/OpenMS

Using OpenMS in combination with KNIME, you can create, edit, open, save, and run workflows that combine TOPP tools with
the powerful data analysis capabilities of KNIME. Workflows can be created conveniently in a graphical user interface.
The parameters of all involved tools can be edited within the application and are also saved as part of the workflow.
Furthermore, KNIME interactively performs validity checks during the workflow editing process, to make it more
difficult to create an invalid workflow. Throughout most parts of this tutorial, you will use KNIME to create and execute
workflows. The first step is to become familiar with KNIME. Additional information on the basic usage of KNIME can be
found on the KNIME [Getting Started page](https://www.knime.com/getting-started-guide). However, the most important
concepts will also be reviewed in this tutorial.

#### Plugin and dependency installation

Before we can start with the tutorial, we need to install all the required extensions for KNIME. Since KNIME 3.2.1, the
program automatically detects missing plugins when you open a workflow but to make sure that the right source for the
OpenMS plugin is chosen, please follow the instructions here. First, we install some additional extensions that are
required by our OpenMS nodes or used in the Tutorials e.g. for visualization and file handling.

1. Click on **Help** > **Install New Software**.
2. From the **Work with**: drop-down list select http://update.knime.com/analytics- platform/4.4.
3. Now select the following plugins from the KNIME & Extensions category
   - KNIME Base Chemistry Types & Nodes
   - KNIME Chemistry Add-Ons
   - KNIME File Handling Nodes (required for OpenMS nodes in general)
   - KNIME Interactive R Statistics Integration
   - KNIME Report Designer
   - KNIME SVG Support
4. Click on **Next** and follow the instructions (you may but don’t need to restart KNIME now).
5. Click again on **Help** > **Install New Software**
6. From the **Work with**: drop-down list select http://update.knime.com/community -contributions/trusted/4.4
7. Now select the following plugin from the ”KNIME Community Contributions - Cheminformatics” category
   - RDKit KNIME integration
8. Click on **Next**  and follow the instructions and after a restart of KNIME the dependencies will be installed.

In addition, we need to install R for the statistical downstream analysis. Choose the directory that matches your
operating system, double-click the R installer and follow the instructions. We recommend to use the default settings
whenever possible. On macOS you also need to install XQuartz from the same directory.

Afterwards open your R installation. If you use Windows, you will find an ”R x64 3.6.X” icon on your desktop. If you use
macOS, you will find R in your Applications folder. In R type the following lines (you might also copy them from the file
**R** > **install_R_packages.R** folder on the USB stick):

```r
install.packages('Rserve',,"http://rforge.net/",type="source")
install.packages("Cairo")

install.packages("devtools")
install.packages("ggplot2")
install.packages("ggfortify")

if (!requireNamespace("BiocManager", quietly = TRUE))
  install.packages("BiocManager")

BiocManager::install()
BiocManager::install(c("MSstats"))
```
In KNIME, click on **KNIME** > **Preferences**, select the category **KNIME** > **R** and set the ”Path to R Home” to
your installation path. You can use the following settings, if you installed R as described above:

- Windows: `C: \Program Files \R \R-3.6.X (where X is the version you used to install the above libraries)`
- macOS: `/Library/Frameworks/R.framework/Versions/3.6/Resources`

You are now ready to install the OpenMS nodes.
- Open KNIME.
- Click on **Help** > **Install New Software**

We included a custom KNIME update site to install the OpenMS KNIME plugins from the USB stick. If you do not have a stick
available, please see below.

- In the now open dialog choose **Add** (in the upper right corner of the dialog) to define a new update site. In the
  opening dialog enter the following details.

  Name: OpenMS 2.7 UpdateSite
  Location: `file:/KNIMEUpdateSite/2.7.0/`
- After pressing **OK** KNIME will show you all the contents of the added Update Site.

```{note}
From now on, you can use this repository for plugins in the **Work with**: drop-down list.
```

- Select the OpenMS nodes in the ”Uncategorized” category and click **Next**.
- Follow the instructions and after a restart of KNIME the OpenMS nodes will be available in the Node repository under
  “Community Nodes”.

Alternatively, you can try these steps that will install the OpenMS KNIME plugins from the internet. Note that download
can be slow.

- In the now open dialog, choose **Add** (in the upper right corner of the dialog) to define a new update site. In the
  opening dialog enter the following details.

  Name: OpenMS 2.5 UpdateSite
  Location: https://abibuilder.informatik.uni- tuebingen.de/archive/openms/knime-plugin/updateSite/nightly/
- After pressing **OK** KNIME will show you all the contents of the added Update Site.

```{note}
From now on, you can use this repository for plugins in the **Work with:** drop-drown list.
```
- Select the OpenMS nodes in the ”Uncategorized” category and click **Next**.
- Follow the instructions and after a restart of KNIME the OpenMS nodes will be available in the Node repository under
  "Community Nodes".

#### KNIME concepts

A workflow is a sequence of computational steps applied to a single or multiple input data to process and analyze the
data. In KNIME such workflows are implemented graphically by connecting so-called nodes. A node represents a single
analysis step in a workflow. Nodes have input and output ports where the data enters the node or the results are provided
for other nodes after processing, respectively. KNIME distinguishes between different port types, representing different
types of data. The most common representation of data in KNIME are tables (similar to an excel sheet). Ports that accept
tables are marked with a small triangle. For OpenMS nodes, we use a different port type, so called file ports, representing
complete files. Those ports are marked by a small blue box. Filled blue boxes represent mandatory inputs and empty blue
boxes optional inputs. The same holds for output ports, despite you can deactivate them in the configuration dialog
(double-click on node) under the **OutputTypes** tab. After execution, deactivated ports will be marked with a red cross and
downstream nodes will be inactive (not configurable).

A typical OpenMS workflow in KNIME can be divided in two conceptually different parts:

- Nodes for signal and data processing, filtering and data reduction. Here, files are passed between nodes. Execution
  times of the individual steps are typically longer for these types of nodes as they perform the main computations.
- Downstream statistical analysis and visualization. Here, tables are passed between nodes and mostly internal KNIME
  nodes or nodes from third-party statistics plugins are used. The transfer from files (produced by OpenMS) and tables
  usually happens with our provided Exporter and Reader nodes (e.g. MzTabExporter followed by MzTabReader).

Nodes can have three different states, indicated by the small traffic light below the node.
- Inactive, failed, and not yet fully configured nodes are marked red.
- Configured but not yet executed nodes are marked yellow.
- Successfully executed nodes are marked green.

If the node execution fails, the node will switch to the red state. Other anomalies and warnings like missing information
or empty results will be presented with a yellow exclamation mark above the traffic light. Most nodes will be configured
as soon as all input ports are connected. Some nodes need to know about the output of the predecessor and may stay red
until the predecessor was executed. If nodes still remain in a red state, probably additional parameters have to be
provided in the configuration dialog that can neither be guessed from the data nor filled with sensible defaults. In
this case, or if you want to customize the default configuration in general, you can open the configuration dialog of a
node with a double-click on the node. For all OpenMS nodes you will see a configuration dialog like the one shown in
below figure.

|![Node configuration dialog of an OpenMS node](../images/openms-user-tutorial/knime-setup/knime_configure_dialog.png)|
|:--:|
|Figure 6: Node configuration dialog of an OpenMS node|

```{tip}
OpenMS distinguishes between normal parameters and advanced parameters. Advanced parameters are by default hidden from
the users since they should only rarely be customized. In case you want to have a look at the parameters or need to
customize them in one of the tutorials you can show them by clicking on the checkbox **Show advanced parameter**
in the lower part of the dialog. Afterwards the parameters are shown in a light gray color.
```

The dialog shows the individual parameters, their current value and type, and, in the lower part of the dialog, the
documentation for the currently selected parameter. Please also note the tabs on the top of the configuration dialog.
In the case of OpenMS nodes, there will be another tab called OutputTypes. It contains dropdown menus for every output
port that let you select the output filetype that you want the node to return (if the tool supports it). For optional
output ports you can select Inactive such that the port is crossed out after execution and the associated generation of
the file and possible additional computations are not performed. Note that this will deactivate potential downstream
nodes connected to this port.

#### Overview of the graphical user interface

|![The KNIME workbench](../images/openms-user-tutorial/knime-setup/knime_workbench_marked.png)|
|:--:|
|Figure 7: The KNIME workbench|

The graphical user interface (GUI) of KNIME consists of different components or so-called panels that are shown in
above image. We will briefly introduce the individual panels and their purposes below.

##### Workflow Editor

The workflow editor is the central part of the KNIME GUI. Here you assemble the workflow by adding nodes from the Node
Repository via ”drag & drop”. For quick creation of a workflow, note that double-clicking on a node in the repository
automatically connects it to the selected node in the workbench (connecting all the inputs with as many fitting outputs
of the last node). Manually, nodes can be connected by clicking on the output port of one node and dragging the edge
until releasing the mouse at the desired input port of the next node. Deletions are possible by selecting nodes and/or
edges and pressing <kbd>DEL</kbd> or <kbd>Fn</kbd> + <kbd>Backspace</kbd> depending on your OS and settings. Multiselection
happens via dragging rectangles with the mouse or adding elements to the selection by clicking them while holding down
<kbd>Ctrl</kbd>.

##### KNIME Explorer

Shows a list of available workflows (also called workflow projects). You can open a workflow by double-clicking it. A
new workflow can be created with a right-click in the Workflow Explorer followed by choosing **New KNIME Workflow**
from the appearing context menu. Remember to save your workflow often with the <kbd>Ctrl</kbd> + <kbd>S</kbd> shortcut.

##### Workflow Coach (since KNIME 3.2.1)

Shows a list of suggested following nodes, based on the last added/clicked nodes. When you are not sure which node to
choose next, you have a reasonable suggestion based on other users behavior there. Connect them to the last node with a
double-click.

##### Node Repository

Shows all nodes that are available in your KNIME installation. Every plugin you install will provide new nodes that can
be found here. The OpenMS nodes can be found in **Community Node** > **OpenMS** Nodes for managing files (e.g., Input
Files or Output Folders) can be found in **Community Nodes** > **GenericKnimeNode**. You can search the node repository
by typing the node name into the small text box in the upper part of the node repository.

##### Outline

The Outline panel contains a small overview of the complete workflow. While of limited use when working on a small
workflow, this feature is very helpful as soon as the workflows get bigger. You can adjust the zoom level of the explorer
by adjusting the percentage in the toolbar at the top of KNIME.

##### Console

In the console panel, warning and error messages are shown. This panel will provide helpful information if one of the
nodes failed or shows a warning sign.

##### Node Description

As soon as a node is selected, the Node Description window will show the documentation of the node including
documentation for all its parameters and especially their in- and outputs, such that you know what types of data nodes
may produce or expect. For OpenMS nodes you will also find a link to the tool page of the online documentation.

#### Creating workflows

Workflows can easily be created by a right click in the Workflow Explorer followed by clicking on **New KNIME workflow**.

#### Sharing workflows

To be able to share a workflow with others, KNIME supports the import and export of complete workflows. To export a
workflow, select it in the Workflow Explorer and select **File** > **Export KNIME Workflow**. KNIME will export
workflows as a _knwf_ file containing all the information on nodes, their connections, and their parameter configuration.

Those *knwf* files can again be imported by selecting:

**File** > **Import KNIME Workflow**

```{note}
For your convenience we added all workflows discussed in this tutorial to the **Workflows** folder on the USB Stick.
 Additionally, the workflow files can be found on [workflow downloads](../downloads.md#workflows). If you want to check
 your own workflow by comparing it to the solution or got stuck, simply import the full workflow from the corresponding
 *knwf* file and after that double-click it in your KNIME Workflow repository to open it.
```

#### Duplicating workflows

In this tutorial, a lot of the workflows will be created based on the workflow from a previous task. To keep the
intermediate workflows, we suggest you create copies of your workflows so you can see the progress. To create a copy of
your workflow, save it, close it and follow the next steps.

- Right click on the workflow you want to create a copy of in the Workflow Explorer and select **Copy**.
- Right click again somewhere on the workflow explorer and select **Paste**.
- This will create a workflow with same name as the one you copied with a (2) appended.
- To distinguish them later on you can easily rename the workflows in the Workflow Explorer by right clicking on the
  workflow and selecting **Rename**.

```{note}
To rename a workflow it has to be closed, too.
```

#### A minimal workflow

Let us now start with the creation of a simple workflow. As a first step, we will gather some basic
information about the data set before starting the actual development of a data analysis workflow. This minimal workflow
can also be used to check if all requirements are met and that your system is compatible.

- Create a new workflow.
- Add an Input File node and an Output Folder node (to be found in **Community Nodes** > **GenericKnimeNodes** > **IO**
  and a FileInfo node (to be found in the category **Community Node** > **OpenMS** > **File Handling**)  to the workflow.
- Connect the Input File node to the FileInfo node, and the first output port of the FileInfo node to the Output Folder
  node.

```{tip}
In case you are unsure about which node port to use, hovering the cursor over the port in question will display the port
name and what kind of input it expects.
```
The complete workflow is shown in below image. `FileInfo` can produce two different kinds of output files.

|![A minimal workflow calling FileInfo on a single file.](../images/openms-user-tutorial/knime-setup/minimal_FileInfo.svg)|
|:--:|
|Figure 8: A minimal workflow calling `FileInfo` on a single file.|

- All nodes are still marked red, since we are missing an actual input file. Double-click the Input File node and select
  **Browse**. In the file system browser select **Example_Data** > **Introduction** > **datasets** > **tiny** > **velos005614.mzML**
  and click **Open**. Afterwards close the dialog by clicking **Ok**.

```{note}
Make sure to use the “tiny” version this time, not “small”, for the sake of faster workflow execution.
```
- The **Input File** node and the **FileInfo** node should now have switched to yellow, but the **Output Folder** node is still red.
  Double-click on the **Output Folder** node and click on **Browse** to select an output directory for the generated data.
- Great! Your first workflow is now ready to be run. Press <kbd>&uarr;</kbd> + <kbd>F7</kbd> (shift key + F7; or the
  button with multiple green triangles in the KNIME Toolbar) to execute the complete workflow. You can also right click
  on any node of your workflow and select <kbd>Execute</kbd> from the context menu.
- The traffic lights tell you about the current status of all nodes in your workflow. Currently running tools show either
  a progress in percent or a moving blue bar, nodes waiting for data show the small word “queued”, and successfully
  executed ones become green. If something goes wrong (e.g., a tool crashes), the light will become red.
- In order to inspect the results, you can just right-click the Output Folder node and select **View: Open the output folder**
  You can then open the text file and inspect its contents.  You will find some basic information of the data contained
  in the mzML file, e.g., the total number of spectra and peaks, the RT and m/z range, and how many MS1 and MS2 spectra
  the file contains.

Workflows are typically constructed to process a large number of files automatically. As a simple example, consider you
would like to convert multiple Thermo Raw files into the mzML format. We will now modify the workflow to compute the
same information on three different files and then write the output files to a folder.

- We start from the previous workflow.
- First we need to replace our single input file with multiple files. Therefore we add the Input Files node from the
  category **Community Nodes** > **GenericKnimeNodes** > **IO**.
- To select the files we double-click on the Input Files node and click on **Add**. In the filesystem browser we select
  all three files from the directory **Example_Data** > **Introduction** > **datasets** > **tiny**. And close the dialog
  with **Ok**.
- We now add two more nodes: the **ZipLoopStart** and the **ZipLoopEnd** node from the category
  **Community Nodes** > **GenericKnimeNodFlow** > **Flow**.
- Afterwards we connect the **Input Files** node to the first port of the **ZipLoopStart** node, the first port of the **ZipLoopStart**
  node to the **FileConverter** node, the first output port of the **FileConverter** node to the first input port of the
  **ZipLoopEnd** node, and the first output port of the **ZipLoopEnd** node to the **Output Folder** node (NOT to the Output File).

The complete workflow is shown in below figure.

|![A minimal workflow calling the FileConverter on multiple Thermo Raw files in a loop](../images/openms-user-tutorial/knime-setup/Minimal_RawFileConverter_Loop.png)|
|:--:|
|Figure 9: A minimal workflow calling the FileConverter on multiple Thermo Raw files in a loop|

Execute the workflow and inspect the output as before.

In case you had trouble to understand what **ZipLoopStart** and **ZipLoopEnd** do, here is a brief explanation:

- The **Input Files** node passes a list of files to the ZipLoopStart node.
- The ZipLoopStart node takes the files as input, but passes the single files sequentially (that is: one after the other)
  to the next node.
- The ZipLoopEnd collects the single files that arrive at its input port. After all files have been processed, the collected
  files are passed again as file list to the next node that follows.

#### Digression: Working with chemical structures

Metabolomics analyses often involve working with chemical structures. Popular cheminformatic toolkits such as RDKit[7]
or CDK[^8] are available as KNIME plugins and allow us to work with chemical structures directly from within KNIME.
In particular, we will use KNIME and RDKit to visualize a list of compounds and filter them by predefined substructures.
Chemical structures are often represented as SMILES (**S**implified **m**olecular **i**nput **l**ine **e**ntry **s**pecification), a simple and compact way to describe complex chemical structures as text. For example, the chemical structure of L-alanine can be written as the SMILES string C[C@H](N)C(O)=O. As we will discuss later, all OpenMS tools that perform metabolite
identification will report SMILES as part of their result, which can then be further processed and visualized using RDKit
and KNIME.

|![ Workflow to visualize a list of SMILES strings and filter them by predefined substructures](../images/openms-user-tutorial/metabo/structures_filter_workflow.png)|
|:--:|
|Figure 10: Workflow to visualize a list of SMILES strings and filter them by predefined substructures|

Perform the following steps to build the workflow shown in the above figure. You will use this workflow to visualize a
list of SMILES strings and filter them by predefined substructures:

- Add the node File Reader, open the node configuration dialog and select the file `smiles.csv`. This file has been
  exported from the Human Metabolome Database (HMDB) and contains the portion of the human metabolome that has been
  detected and quantified. The file preview on the bottom of the dialog shows that each compound is given by its HMDB
  accession, compound name, and SMILES string. Click on the column header **SMILES** to change its properties. Change the
  column type from **string** to **smiles** and close the dialog with **Ok**. Afterwards the **SMILES** column will be
  visualized as chemical structures instead of text directly within all **KNIME** tables.
- Add the node `RDKit From Molecule` and connect it to the `File Reader`. This node will use the provided `SMILES`
  strings to add an additional column that is required by RDKit.
- Add the node `RDKit Functional Group Filter` and open the node configuration dialog. You can use this dialog to filter
  the compounds by any combination of functional groups. In this case we want to find all compounds that contain at
  least one aromatic carboxylic acid group. To do this, set this group as active and choose ’¿=’ and ’1’.
- Connect the first output port (Molecules passing the filter) to a `CSV Writer` node to save the filtered metabolites
  to a file. Right click **RDKit Functional Group Filter** and select the view ’Molecules passing the filter’ to inspect
  the selected compounds in KNIME. How many compounds pass the chosen filter, see below figure.


The following figure shows resulting list of compounds that contains at least one aromatic carboxylic acid group.

|![Resulting list of compounds that contains at least one aromatic carboxylic acid group](../images/openms-user-tutorial/metabo/structures_filter_results.png)|
|:--:|
|Figure 11:  Resulting list of compounds that contains at least one aromatic carboxylic acid group.|

#### Advanced topic: Metanodes

Workflows can get rather complex and may contain dozens or even hundreds of nodes. KNIME provides a simple way to
improve handling and clarity of large workflows:

**Metanodes** allow to bundle several nodes into a single **Metanode**.

<div class="admonition task" name="html-admonition">
<p class="admonition-title"><b>Task</b></p>
Select multiple nodes (e.g. all nodes of the ZipLoop including the start and end node). To select a set of nodes, draw a rectangle around them with the left mouse button or hold <kbd>Ctrl</kbd> to add/remove single nodes from the selection.
<div class="admonition tip" name="html-admonition">
<p class="admonition-title"><b>Tip</b></p>
There is a <b>Select Loop</b> option when you right-click a node in a loop, that does exactly that for you. Then, open the
context menu (right-click on a node in the selection) and select <b>Create Metanode</b>. Enter a caption for the <b>Metanode</b>.
The previously selected nodes are now contained in the <b>Metanode</b>. Double-clicking on the <b>Metanode</b> will display
the contained nodes in a new tab window.
</div>
</div>

<div class="admonition task" name="html-admonition">
<p class="admonition-title"><b>Task</b></p>
Create the Metanode to let it behave like an encapsulated single node. First select the <b>Metanode</b>, open the context
menu (right-click) and select <b>Metanode</b> > <b>Wrap</b>. The differences between Metanodes and their wrapped counterparts
are marginal (and only apply when exposing user inputs and workflow variables). Therefore we suggest to use standard
Metanodes to clean up your workflow and cluster common subparts until you actually notice their limits.
</div>

<div class="admonition task" name="html-admonition">
<p class="admonition-title"><b>Task</b></p>
Undo the packaging. First select the (<b>Wrapped</b>) <b>Metanode</b>, open the context menu (right-click) and select <b>(Wrapped) Metanode</b> > <b>Expand</b>.
</div>

#### Advanced topic: R integration

KNIME provides a large number of nodes for a wide range of statistical analysis, machine learning, data processing, and
visualization. Still, more recent statistical analysis methods, specialized visualizations or cutting edge algorithms
may not be covered in KNIME. In order to expand its capabilities beyond the readily available nodes, external scripting
languages can be integrated. In this tutorial, we primarily use scripts of the powerful statistical computing language R.
Note that this part is considered advanced and might be difficult to follow if you are not familiar with R. In this case
you might skip this part.

**R View (Table)** allows to seamlessly include R scripts into KNIME. We will demonstrate on a minimal. We will
demonstrate on a minimal example how such a script is integrated.

<div class="admonition task" name="html-admonition">
<p class="admonition-title"><b>Task</b></p>
First we need some example data in KNIME, which we will generate using the <b>Data Generator</b> node. You can keep the
default settings and execute the node. The table contains four columns, each containing random coordinates and one column
containing a cluster number (Cluster_0 to Cluster_3). Now place a <b>R View (Table)</b> node into the workflow and connect
the upper output port of the <b>Data Generator</b> node to the input of the <b>R View (Table)</b> node. Right-click and
configure the node. If you get an error message like ”Execute failed: R_HOME does not contain a folder with name ’bin’.”
or ”Execution failed: R Home is invalid.”: please change the R settings in the preferences. To do so open <b>File</b> >
<b>Preferences</b> > <b>KNIME</b> > <b>R</b> and enter the path to your R installation (the folder that contains the bin
directory. (e.g., <b>C:</b> > <b>Program Files</b> > <b>R</b> > <b>R-3.4.3</b>).

If you get an error message like: ”Execute failed: Could not find Rserve package. Please install it in your R
installation by running ”install.packages(’Rserve’)”.” You may need to run your R binary as administrator (In windows
explorer: right-click ”Run as administrator”) and enter install.packages(’Rserve’) to install the package.

If R is correctly recognized we can start writing an R script. Consider that we are interested in plotting the first and
second coordinates and color them according to their cluster number. In R this can be done in a single line. In the
<b>R view (Table)</b> text editor, enter the following code:

<code>plot(x=knime.in$Universe_0_0, y=knime.in$Universe_0_1, main="Plotting column Universe_0_0 vs. Universe_0_1", col=knime.in$"Cluster Membership")</code>

**Explanation:** The table provided as input to the **R View (Table)** node is available as R **data.frame** with name
<code>knime.in</code>. Columns (also listed on the left side of the R View window) can be accessed in the usual R way by first
specifying the <code>data.frame</code> name and then the column name (e.g <code>knime.in$Universe_0_0</code>). <code>plot</code> is the plotting function
we use to generate the image. We tell it to use the data in column <b>Universe_0_0</b> of the dataframe object <b>knime.in</b>
(denoted as <code>knime.in$Universe_0_0</code>) as x-coordinate and the other column <code>knime.in$Universe_0_1</code> as y-coordinate in the
plot. <code>main</code> is simply the main title of the plot and <code>col</code> the column that is used to determine the color (in this case
it is the <code>Cluster Membership</code> column).

Now press the <b>Eval script</b> and <b>Show plot</b> buttons.
</div>

```{note}
Note that we needed to put some extra quotes around `Cluster Membership`. If we omit those, R would interpret the column
name only up to the first space `(knime.in$Cluster)` which is not present in the table and leads to an error. Quotes are
regularly needed if column names contain spaces, tabs or other special characters like $ itself.
```

## Label-free quantification of peptides

### Introduction

In the following chapter, we will build a workflow with OpenMS / KNIME to quantify a label-free experiment. Label-free
quantification is a method aiming to compare the relative amounts of proteins or peptides in two or more samples. We will
start from the minimal workflow of the last chapter and, step-by-step, build a label-free quantification workflow.

### Peptide identification

As a start, we will extend the minimal workflow so that it performs a peptide identification using the OMSSA[^9] search
engine. Since OpenMS version 1.10, OMSSA is included in the OpenMS installation, so you do not need to  download and
install it yourself.

Let’s start by replacing the input files in our **Input Files** node by the three mzML files in
**Example Data** > **Labelfree** > **datasets** > **lfqxspikeinxdilutionx1-3.mzML**. This is a reduced toy dataset where
each of the three runs contains a constant background of S. `pyogenes` peptides as well as human spike-in peptides in
different concentrations. [^10]

- Instead of FileInfo, we want to perform OMSSA identification, so we simply replace the `FileInfo` node with the
  `OMSSAAdapter` node **Community Nodes** > **OpenMS** > **Identification**, and we are almost done. Just make sure you
  have connected the `ZipLoopStart` node with the `in` port of the `OMSSAAdapter` node.
- OMSSA, like most mass spectrometry identification engines, relies on searching the input spectra against sequence
  databases. Thus, we need to introduce a search database input. As we want to use the same search database for all of
  our input files, we can just add a single `Input File` node to the workflow and connect it directly with the
  `OMSSAAdapter database` port. KNIME will automatically reuse this Input node each time a new ZipLoop iteration is
  started. In order to specify the database,
  **Example_Data** > **Labelfree** > **databases** > select **s_pyo_sf370_potato_human_target_decoy_with_contaminants.fasta**,
  and we have a very basic peptide identification workflow.

  ```{note}
  You might also want to save your new identification workflow under a different name. Have a look at [duplicating workflows](#duplicating-workflows)
  for information on how to create copies of workflows.
  ```
- The result of a single OMSSA run is basically a number of peptide-spectrum-matches (PSM) with a score each, and these
  will be stored in an idXML file. Now we can run the pipeline and after execution is finished, we can have a first look
  at the the results: just open the input files folder with a file browser and from there open an mzML file in **TOPPView**.
- Here, annotate this spectrum data file with the peptide identification results. Choose **Tools** > **Annonate with identification**
  from the menu and select the idXML file that **OMSSAAdapter** generated (it is located within the output directory that
  you specified when starting the pipeline).
- On the right, select the tab **Identification view**. All identified peptides can be seen using this view. User can also
  browse the corresponding MS2 spectra.

  ```{note}
  Opening the output file of `OMSSAAdapter` (the idXML file) directly is also possible, but the direct visusalisation of
  an idXML files is less useful.
  ```
- The search results stored in the idXML file can also be read back into a KNIME table for inspection and subsequent
  analyses: Add a `TextExporter` node from **Community Nodes** > **OpenMS** > **File Handling** to your workflow and
  connect the output port of your `OMSSAAdapter` (the same port `ZipLoopEnd` is connected to) to its input port. This
  tool will convert the idXML file to a more human-readable text file which can also be read into a KNIME table using
  the `IDTextReader` node. Add an `IDTextReader` node(**Community Nodes** > **OpenMS** > **Conversion**) after
  **TextExporter** and execute it. Now you can right click `IDTextReader` and select **ID Table** to browse your peptide
  identifications.
- From here, you can use all the tools KNIME offers for analyzing the data in this table. As a simple example, add a
  `Histogram (local)` node (from category **Views - Local (Swing)**) node after `IDTextReader`, double-click it, select
  `peptide_charge` as Histogram column, hit **OK**, and execute it. Right-clicking and selecting
  **Interactive View: Histogram view** will open a plot showing the charge state distribution of your identifications.

In the next step, we will tweak the parameters of OMSSA to better reflect the instrument’s accuracy. Also, we will
extend our pipeline with a false discovery rate (FDR) filter to retain only those identifications that will yeild an
FDR of < 1 %.

- Open the configuration dialog of `OMSSAAdapter`. The dataset was recorded using an LTQ Orbitrap XL mass spectrometer,
  set the precursor mass tolerance to a smaller value, say 5 ppm. Set `precursor_mass_tolerance` to 5 and
  `precursor_error_units` to `ppm`.

  ```{note}
  Whenever you change the configuration of a node, the node as well as all its successors will be reset to the Configured
  state (all node results are discarded and need to be recalculated by executing the nodes again).
  ```

- Set `max_precursor_charge` to 5, in order to also search for peptides with charges up to 5.
- Add `Carbamidomethyl (C)` as fixed modification and `Oxidation(M)` as variable modification.

  ```{note}
  To add a modification click on the empty value field in the configuration dialog to open the list editor dialog. In the
  new dialog click **Add**. Then select the newly added modification to open the drop down list where you can select the
  the correct modification.
  ```
- A common step in analysis is to search not only against a regular protein database, but to also search against a decoy
  database for FDR estimation. The fasta file we used before already contains such a decoy database. For OpenMS to know
  which OMSSA PSM came from which part of the file (i.e. target versus decoy), we have tso index the results. To this end,
  extend the workflow with a `PeptideIndexer` node **Community Nodes** > **OpenMS** > **ID Processing**. This node needs
  the idXML as input as well as the database file (see below figure).

  ```{tip}
  You can direct the files of an `Input File` node to more than just one destination port.
  ```
- The decoys in the database are prefixed with “DECOY_”, so we have to set `decoy_string` to `DECOY_` and `decoy_string_position`
  to `prefix` in the configuration dialog of `PeptideIndexer`.
- Now we can go for the FDR estimation, which the `FalseDiscoveryRate` node will calculate for us (you will find it in
  **Community Nodes** > **OpenMS** > **ID Processing**).
- In order to set the FDR level to 1%, we need an `IDFilter` node from **Community Nodes** > **OpenMS** > **ID Processing**.
  Configuring its parameter score `→pep` to 0.01 will do the trick. The FDR calculations (embedded in the idXML) from
  the `FalseDiscoveryRate` node will go into the *in* port of the `IDFilter` node.
- Execute your workflow and inspect the results using `IDTextReader` like you did before. How many peptides did you
  identify at this FDR threshold?

  ```{note}
  The finished identification workflow is now sufficiently complex that we might want to encapsulate it in a Metanode.
  For this, select all nodes inside the ZipLoop (including the **Input File** node) and right-click to select
  **Collapse into Metanode** and name it ID. Metanodes are useful when you construct even larger workflows and want to
  keep an overview.

  ```

  The below images shows OMSSA ID pipeline including FDR filtering.

  |![OMSSA ID pipeline including FDR filtering](../images/openms-user-tutorial/labelfree/PepIdFDR.png)|
  |:--:|
  |Figure 12: OMSSA ID pipeline including FDR filtering|


#### Bonus task: Identification using several search engines

```{note}
If you are ahead of the tutorial or later on, you can further improve your FDR identification workflow by a so-called
consensus identification using several search engines. Otherwise, just continue with [quantification](#quantification).
```

It has become widely accepted that the parallel usage of different search engines can increase peptide identification
rates in shotgun proteomics experiments. The ConsensusID algorithm is based on the calculation of posterior error
probabilities (PEP) and a combination of the normalized scores by considering missing peptide sequences.

- Next to the `OMSSAAdapter` and a `XTandemAdapter` **Community Nodes** > **OpenMS** > **Identification** node and set
  its parameters and ports analogously to the `OMSSAAdapter`. In XTandem, to get more evenly distributed scores, we
  decrease the number of candidates a bit by setting the precursor mass tolerance to 5 ppm and the fragment mass
  tolerance to 0.1 Da.
- To calculate the PEP, introduce each a `IDPosteriorErrorProbability` **Community Nodes** > **OpenMS** > **ID Processing**
  node to the output of each ID engine adapter node. This will calculate the PEP to each hit and output an updated idXML.
- To create a consensus, we must first merge these two files with a `FileMerger` node **Community Nodes** >
  **GenericKnimeNode** > **Flow** so we can then merge the corresponding IDs with a `IDMerger` **Community Nodes** >
  **OpenMS** > **File Handling**.
- Now we can create a consensus identification with the `ConsensusID` **Community Nodes** > **OpenMS** > **ID Processing**
  node. We can connect this to the `PeptideIndexer` and go along with our existing FDR filtering.

  ```{note}
  By default, X!Tandem takes additional enzyme cutting rules into consideration (besides the specified tryptic digest).
  Thus for the tutorial files, you have to set PeptideIndexer’s `enzyme` →specificity parameter to `none` to accept
  X!Tandems non-tryptic identifications as well.
  ```

In the end, the ID processing part of the workflow can be collapsed into a Metanode to keep the structure clean (see below figure which shows complete consensus identification workflow).

|![Complete consensus identification workflow](../images/openms-user-tutorial/labelfree/PepConsensusId.png)|
|:--:|
|Figure 13: Complete consensus identification workflow|

### Quantification

Now that we have successfully constructed a peptide identification pipeline, we can
add quantification capabilities to our workflow.

- Add a **FeatureFinderCentroided** node from **Community Nodes** > **OpenMS** > **Quantitation**
which gets input from the first output port of the **ZipLoopStart** node. Also, add
an **IDMapper** node (from **Community Nodes** > **OpenMS** > **ID Processing** ) which receives
input from the **FeatureFinderCentroided** node (Port 1) and the ID Metanode (or **IDFilter** node (Port 0) if you haven’t used the Metanode). The output of the **IDMapper** node is then connected to an in port of the **ZipLoopEnd** node.
- `FeatureFinderCentroided` finds and quantifies peptide ion signals contained in
the MS1 data. It reduces the entire signal, i.e., all peaks explained by one and
the same peptide ion signal, to a single peak at the maximum of the chromatographic elution profile of the monoisotopic mass trace of this peptide ion and
assigns an overall intensity.
- `FeatureFinderCentroided` produces a featureXML file as output, containing only quantitative information of so-far unidentified peptide signals. In order to annotate these with the corresponding ID information, we need the **IDMapper** node.
-  Run your pipeline and inspect the results of the **IDMapper** node in TOPPView. Open the mzML file of your data to display the raw peak intensities.
- To assess how well the feature finding worked, you can project the features contained in the featureXML file on the raw data contained in the mzML file. To
this end, open the featureXML file in TOPPView by clicking on File Open file and add it to a new layer ( Open in New layer ). The features are now visualized on top of your raw data. If you zoom in on a small region, you should be able to see the individual boxes around features that have been detected (see Fig. 14). If you
hover over the the feature centroid (small circle indicating the chromatographic apex of monoisotopic trace) additional information of the feature is displayed.

  |![Visualization of detected features (boxes) in TOPPView](../images/openms-user-tutorial/labelfree/featureXML.png)|
  |:--:|
  |Figure 14: Visualization of detected features (boxes) in TOPPView|

  ```{note}
  The chromatographic RT range of a feature is about 30-60 s and
  its m/z range around 2.5 m/z in this dataset. If you have trouble zooming in on a feature, select the full RT range and zoom only into the
  m/z dimension by holding down <kb>Ctrl</kb> ( <kbd>cmd ⌘</kbd> on macOS) and repeatedly
  dragging a narrow box from the very left to the very right
  ```
- You can see which features were annotated with a peptide identification by first
selecting the featureXML file in the **Layers** window on the upper right side and then clicking on the icon with the letters A, B and C on the upper icon bar. Now,
click on the small triangle next to that icon and select **Peptide identification**.

The following image shows the final constructed workflow:

|![Extended workflow featuring peptide identification and quantification](../images/openms-user-tutorial/labelfree/PepQuantIdNoAlign.png)|
|:--:|
|Figure 15: Extended workflow featuring peptide identification and quantification|

### Combining quantitative information across several label-free experiments

So far, we successfully performed peptide identification as well as quantification on
individual LC-MS runs. For differential label-free analyses, however, we need to identify and quantify corresponding signals in different experiments and link them together to compare their intensities. Thus, we will now run our pipeline on all three
available input files and extend it a bit further, so that it is able to find and link features across several runs.

|![Complete identification and label-free quantification workflow](../images/openms-user-tutorial/labelfree/PepQuantId.png)|
|:--:|
|Figure 16: Complete identification and label-free quantification workflow|

- To find features across several maps, we first have to align them to correct for retention time shifts between the different label-free measurements. With the **MapAlignerPoseClustering** node in **Community Nodes** > **OpenMS** > **Map Alignment**, we can align corresponding peptide signals to each other as closely as possible by applying a transformation in the RT dimension.

  ```{note}
  `MapAlignerPoseClustering` consumes several featureXML files and its output should still be several featureXML files containing the same features, but with the transformed RT values. In its configuration dialog, make sure that **OutputTypes** is set to **featureXML**.
  ```
- With the **FeatureLinkerUnlabeledQT** node in **Community Nodes** > **OpenMS** > **Map Alignment**, we can then perform the actual linking of corresponding features. Its output is a consensusXML file containing linked groups of corresponding features across the different experiments.
- Since the overall intensities can vary a lot between different measurements (for example, because the amount of injected analytes was different), we apply the **ConsensusMapNormalizer** node in **Community Node** > **OpenMS** > **Map Alignment** as a last processing step. Configure its parameters with setting `algorithm_type` to `median`. It will then normalize the maps in such a way that the median intensity of all input maps is equal.
- Finally, export the resulting normalized consensusXML file to a csv format using the **TextExporter** node. Connect its out port to a new **Output Folder** node.

  ```{note}
  You can specify the desired column separation character in the parameter settings (by default, it is set to “ ” (a space)). The output file of `TextExporter` can also be opened with external tools, e.g., Microsoft Excel, for downstream statistical analyses.
  ```

#### Basic data analysis in KNIME

For downstream analysis of the quantification results within the KNIME environment, you can use the **ConsensusTextReader** node in **Community Nodes** > **OpenMS** > **Conversion** instead of the **Output Folder** node to convert the output into a KNIME table (indicated by a triangle as output port). After running the node you can view the KNIME table by right-clicking on the **ConsensusTextReader** node and selecting `Consensus Table`. Every row in this table corresponds to a so-called consensus feature, i.e., a peptide signal quantified across several runs. The first couple of columns describe the consensus feature as a whole (average RT and m/z across the maps, charge, etc.). The remaining columns describe the exact positions and intensities of the quantified features separately for all input samples (e.g., intensity_0 is the intensity of the feature in the first input file). The last 11 columns contain information on peptide identification.

- Now, let’s say we want to plot the log intensity distributions of the human spike-in peptides for all input files. In addition, we will plot the intensity distributions of the background peptides.
- As shown in Fig. 17, add a **Row Splitter** node (**Data Manipulation** > **Row** > **Filter**) after the **ConsensusTextReader** node. Double-click it to configure. The human spike-in peptides have accessions starting with “hum”. Thus, set the column to apply the test to: accessions, select pattern matching as matching criterion, enter `hum` into the corresponding text field, and check the contains wild cards box. Press **OK** and execute the node.
- **Row Splitter** produces two output tables: the first one contains all rows from the input table matching the filter criterion, and the second table contains all other rows. You can inspect the tables by right-clicking and selecting **Filtered** and **Filtered Out**. The former table should now only contain peptides with a human accession, whereas the latter should contain all remaining peptides (including unidentified ones).
- Now, since we only want to plot intensities, we can add a **Column Filter** node by going to **Data Manipulation** > **Column Filter**. Connect its input port to the **Filtered output** port of the **Row Filter** node, and open its configuration dialog. We could either manually select the columns we want to keep, or, more elegantly, select **Wildcard/Regex Selection** and enter `intensity_?` as the pattern. KNIME will interactively show you which columns your pattern applies to while you’re typing.
- Since we want to plot log intensities, we will now compute the log of all intensity values in our table. The easiest way to do this in KNIME is a small piece of R code. Add an **R Snippet** node `R` after **Column Filter** and double-click to configure. In the R Script text editor, enter the following code:

  ```r
  x <- knime.in       # store copy of input table in x

  x[x == 0] <- NA     # replace all zeros by NA (= missing value)

  x <- log10(x)       # compute log of all values
  knime.out <- x      # write result to output table
  ```
- Now we are ready to plot! Add a **Box Plot (local)** node `Views -Swing (local)` after the **R Snippet** node, execute it, and open its view. If everything went well, you should see a significant fold change of your human peptide intensities across the three runs.
- To verify that the concentration of background peptides is constant in all three runs, copy and paste the three nodes after **Row Splitter** and connect the duplicated **Column Filter** to the second output port (Filtered Out) of **Row Splitter**, as shown in Fig. 17. Execute and open the view of your second **Box Plot**.

You have now constructed an entire identification and label-free quantification workflow including a simple data analysis using KNIME. The final workflow should like the workflow shown in the following image:

|![Simple KNIME data analysis example for LFQ](../images/openms-user-tutorial/labelfree/data_analysis.png)|
|:--:|
|Figure 17: Simple KNIME data analysis example for LFQ|

### Identification and quantification of the iPRG2015 data with subsequent MSstats analysis

Advanced downstream data analysis of quantitative mass spectrometry-based proteomics data can be performed using MSstats [^11]. This tool can be combined with
an OpenMS preprocessing pipeline (e.g. in KNIME). The OpenMS experimental design is used to present the data in an MSstats-conformant way for the analysis. Here,
we give an example how to utilize these resources when working with quantitative label-free data. We describe how to use OpenMS and MSstats for the analysis of the
ABRF iPRG2015 dataset [^12].

```{note}
Reanalysing the full dataset from scratch would take too long. In the following tutorial, we will focus on just the conversion process and the downstream analysis.
```

#### Excursion MSstats

The R package `MSstats` can be used for statistical relative quantification of proteins and peptides in mass spectrometry-based proteomics. Supported are label-free as well as labeled experiments in combination with data-dependent, targeted and data independent acquisition. Inputs can be identified and quantified entities (peptides or proteins) and the output is a list of differentially abundant entities, or summaries of their relative abundance. It depends on accurate feature detection, identification
and quantification which can be performed e.g. by an OpenMS workflow. MSstats can be used for data processing & visualization, as well as statistical modeling & inference. Please see [^11] and the [MSstats](http://msstats.org) website for further
information.

#### Dataset

The iPRG (Proteome Informatics Research Group) dataset from the study in 2015, as
described in [^12], aims at evaluating the effect of statistical analysis software on the
accuracy of results on a proteomics label-free quantification experiment. The data is
based on four artificial samples with known composition (background: 200 ng *S. cerevisiae*). These were spiked with different quantities of individual digested proteins,
whose identifiers were masked for the competition as yeast proteins in the provided
database (see Table 1).

<div class="table">

<!-- l. 1198 --><p class="indent">   </p><figure class="float">

<a id="x1-32001r1"></a>
<a id="x1-32002"></a>
<figcaption class="caption"><span class="id">Table&nbsp;1: Samples (background: 200 ng <i>S.&nbsp;cerevisiae</i>) with spiked-in proteins in different
quantities [fmols]</span></figcaption><!-- tex4ht:label?: x1-32001r3  -->
<div class="tabular">
 <table class="tabular" id="TBL-1"><colgroup id="TBL-1-1g"><col id="TBL-1-1"><col id="TBL-1-2"><col id="TBL-1-3"><col id="TBL-1-4"><col id="TBL-1-5"><col id="TBL-1-6"><col id="TBL-1-7"><col id="TBL-1-8"></colgroup><tbody><tr id="TBL-1-1-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-1-1-1">   </td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-1-1-2">                      </td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-1-1-3">                   </td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-1-1-4">                 </td><td class="td11" style="white-space:nowrap; text-align:right;" colspan="4" id="TBL-1-1-5">         <div class="multicolumn" style="white-space:nowrap; text-align:center;"><span class="rm-lmr-10x-x-109">Samples</span></div>
</td></tr><tr id="TBL-1-2-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-1-2-1">    </td><td class="td11" style="white-space:nowrap; text-align:center;" id="TBL-1-2-2">        <div class="multicolumn" style="white-space:nowrap; text-align:center;"><span class="rm-lmr-10x-x-109">Name</span></div>         </td><td class="td11" style="white-space:nowrap; text-align:center;" id="TBL-1-2-3">       <div class="multicolumn" style="white-space:nowrap; text-align:center;"><span class="rm-lmr-10x-x-109">Origin</span></div>       </td><td class="td11" style="white-space:nowrap; text-align:center;" id="TBL-1-2-4"> <div class="multicolumn" style="white-space:nowrap; text-align:center;"><span class="rm-lmr-10x-x-109">Molecular Weight</span></div> </td><td class="td11" style="white-space:nowrap; text-align:center;" id="TBL-1-2-5">  <div class="multicolumn" style="white-space:nowrap; text-align:center;"><span class="rm-lmr-10x-x-109">1</span></div>  </td><td class="td11" style="white-space:nowrap; text-align:right;" id="TBL-1-2-6">   <span class="rm-lmr-10x-x-109">2  </span></td><td class="td11" style="white-space:nowrap; text-align:right;" id="TBL-1-2-7">  <span class="rm-lmr-10x-x-109">3  </span></td><td class="td11" style="white-space:nowrap; text-align:right;" id="TBL-1-2-8">   <span class="rm-lmr-10x-x-109">4  </span></td>
</tr><tr id="TBL-1-3-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-1-3-1"> <span class="rm-lmr-10x-x-109">A  </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-1-3-2"> <span class="rm-lmr-10x-x-109">Ovalbumin                  </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-1-3-3"> <i>Egg White</i>             </td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-1-3-4"> <span class="rm-lmr-10x-x-109">45 KD                </span></td><td class="td11" style="white-space:nowrap; text-align:right;" id="TBL-1-3-5"> <span class="rm-lmr-10x-x-109">65  </span></td><td class="td11" style="white-space:nowrap; text-align:right;" id="TBL-1-3-6">  <span class="rm-lmr-10x-x-109">55  </span></td><td class="td11" style="white-space:nowrap; text-align:right;" id="TBL-1-3-7"> <span class="rm-lmr-10x-x-109">15  </span></td><td class="td11" style="white-space:nowrap; text-align:right;" id="TBL-1-3-8">   <span class="rm-lmr-10x-x-109">2  </span></td>
</tr><tr id="TBL-1-4-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-1-4-1"> <span class="rm-lmr-10x-x-109">B  </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-1-4-2"> <span class="rm-lmr-10x-x-109">Myoglobin                   </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-1-4-3"> <i>Equine Heart</i>          </td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-1-4-4"> <span class="rm-lmr-10x-x-109">17 KD                </span></td><td class="td11" style="white-space:nowrap; text-align:right;" id="TBL-1-4-5"> <span class="rm-lmr-10x-x-109">55  </span></td><td class="td11" style="white-space:nowrap; text-align:right;" id="TBL-1-4-6">  <span class="rm-lmr-10x-x-109">15  </span></td><td class="td11" style="white-space:nowrap; text-align:right;" id="TBL-1-4-7">  <span class="rm-lmr-10x-x-109">2  </span></td><td class="td11" style="white-space:nowrap; text-align:right;" id="TBL-1-4-8">  <span class="rm-lmr-10x-x-109">65  </span></td>
</tr><tr id="TBL-1-5-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-1-5-1"> <span class="rm-lmr-10x-x-109">C  </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-1-5-2"> <span class="rm-lmr-10x-x-109">Phosphorylase b           </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-1-5-3"> <i>Rabbit Muscle</i>         </td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-1-5-4"> <span class="rm-lmr-10x-x-109">97 KD                </span></td><td class="td11" style="white-space:nowrap; text-align:right;" id="TBL-1-5-5"> <span class="rm-lmr-10x-x-109">15  </span></td><td class="td11" style="white-space:nowrap; text-align:right;" id="TBL-1-5-6">   <span class="rm-lmr-10x-x-109">2  </span></td><td class="td11" style="white-space:nowrap; text-align:right;" id="TBL-1-5-7"> <span class="rm-lmr-10x-x-109">65  </span></td><td class="td11" style="white-space:nowrap; text-align:right;" id="TBL-1-5-8">  <span class="rm-lmr-10x-x-109">55  </span></td>
</tr><tr id="TBL-1-6-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-1-6-1"> <span class="rm-lmr-10x-x-109">D  </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-1-6-2"> <span class="rm-lmr-10x-x-109">Beta-Glactosidase         </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-1-6-3"> <i>Escherichia Coli</i>      </td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-1-6-4"> <span class="rm-lmr-10x-x-109">116 KD               </span></td><td class="td11" style="white-space:nowrap; text-align:right;" id="TBL-1-6-5">  <span class="rm-lmr-10x-x-109">2  </span></td><td class="td11" style="white-space:nowrap; text-align:right;" id="TBL-1-6-6">  <span class="rm-lmr-10x-x-109">65  </span></td><td class="td11" style="white-space:nowrap; text-align:right;" id="TBL-1-6-7"> <span class="rm-lmr-10x-x-109">55  </span></td><td class="td11" style="white-space:nowrap; text-align:right;" id="TBL-1-6-8">  <span class="rm-lmr-10x-x-109">15  </span></td>
</tr><tr id="TBL-1-7-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-1-7-1"> <span class="rm-lmr-10x-x-109">E  </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-1-7-2"> <span class="rm-lmr-10x-x-109">Bovine Serum Albumin  </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-1-7-3"> <i>Bovine Serum</i>         </td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-1-7-4"> <span class="rm-lmr-10x-x-109">66 KD                </span></td><td class="td11" style="white-space:nowrap; text-align:right;" id="TBL-1-7-5"> <span class="rm-lmr-10x-x-109">11  </span></td><td class="td11" style="white-space:nowrap; text-align:right;" id="TBL-1-7-6"> <span class="rm-lmr-10x-x-109">0.6  </span></td><td class="td11" style="white-space:nowrap; text-align:right;" id="TBL-1-7-7"> <span class="rm-lmr-10x-x-109">10  </span></td><td class="td11" style="white-space:nowrap; text-align:right;" id="TBL-1-7-8"> <span class="rm-lmr-10x-x-109">500  </span></td>
</tr><tr id="TBL-1-8-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-1-8-1"> <span class="rm-lmr-10x-x-109">F  </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-1-8-2"> <span class="rm-lmr-10x-x-109">Carbonic Anhydrase     </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-1-8-3"> <i>Bovine Erythrocytes</i>  </td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-1-8-4"> <span class="rm-lmr-10x-x-109">29 KD                </span></td><td class="td11" style="white-space:nowrap; text-align:right;" id="TBL-1-8-5"> <span class="rm-lmr-10x-x-109">10  </span></td><td class="td11" style="white-space:nowrap; text-align:right;" id="TBL-1-8-6"> <span class="rm-lmr-10x-x-109">500  </span></td><td class="td11" style="white-space:nowrap; text-align:right;" id="TBL-1-8-7"> <span class="rm-lmr-10x-x-109">11  </span></td><td class="td11" style="white-space:nowrap; text-align:right;" id="TBL-1-8-8"> <span class="rm-lmr-10x-x-109">0.6  </span></td>

</tr></tbody></table></div>


  </figure>
   </div>

#### Identification and quantification

|![KNIME data analysis of iPRG LFQ data](../images/openms-user-tutorial/labelfree/iPRG_lfq.png)|
|:--:|
|Figure 18: KNIME data analysis of iPRG LFQ data.|

The iPRG LFQ workflow (Fig. 18) consists of an identification and a quantification part. The identification is achieved by searching the computationally calculated MS2 spectra from a sequence database (**Input File** node, here with the given database from iPRG:
`ExamplexData` ► `iPRG2015` ► `database` ► `iPRG2015xtargetxdecoyxnocontaminants.fasta`
against the MS2 from the original data (**Input Files** node with all mzMLs following `ExamplexData` ► `iPRG2015` ► `datasets` ► `JDx06232014xsample*.mzML` using the `OMSSAAdapter`.

```{note}
If you want to reproduce the results at home, you have to download the iPRG data in mzML format and perform peak picking on it or convert and pick the raw data with `msconvert`.
```

Afterwards, the results are scored using the **FalseDiscoveryRate** node and filtered to obtain only unique peptides (**IDFilter**) since `MSstats` does not support shared peptides, yet. The quantification is achieved by using the **FeatureFinderCentroided** node, which performs the feature detection on the samples (maps). In the end the quantification results are combined with the filtered identification results (**IDMapper**). In addition, a linear retention time alignment is performed (**MapAlignerPoseClustering**), followed by the feature linking process (**FeatureLinkerUnlabledQT**). The **ConsensusMapNormalizer**s is used to normalize the intensities via robust regression over a set of maps and the **IDConflictResolver** assures that only one identification (best score) is associated with a feature. The output of this workflow is a consensusXML file, which can now be converted using the **MSstatsConverter** (see [Conversion and downstream analysis](openms-user-tutorial.md#conversion-and-downstream-analysis) section).

#### Experimental design

As mentioned before, the downstream analysis can be performed using `MSstats`. In this case, an experimental design has to be specified for the OpenMS workflow. The structure of the experimental design used in OpenMS in case of the iPRG dataset is specified in Table 2.

<div class="table">


<!-- l. 1238 --><p class="indent">   </p><figure class="float">


<a id="x1-34001r2"></a>
<a id="x1-34002"></a>
<figcaption class="caption"><span class="id">Table&nbsp;2: OpenMS Experimental design for the iPRG2015 dataset.</span></figcaption><!-- tex4ht:label?: x1-34001r3  -->
<div class="tabular"> <table class="tabular" id="TBL-2"><colgroup id="TBL-2-1g"><col id="TBL-2-1"><col id="TBL-2-2"><col id="TBL-2-3"><col id="TBL-2-4"><col id="TBL-2-5"></colgroup><tbody><tr id="TBL-2-1-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-1-1"> <span class="rm-lmr-10x-x-109">Fraction_Group  </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-1-2"> <span class="rm-lmr-10x-x-109">Fraction                </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-1-3"> <span class="rm-lmr-10x-x-109">Spectra_Filepath        </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-1-4"> <span class="rm-lmr-10x-x-109">Label  </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-1-5"> <span class="rm-lmr-10x-x-109">Sample  </span></td>
</tr><tr id="TBL-2-2-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-2-1"> <span class="rm-lmr-10x-x-109">1                      </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-2-2"> <span class="rm-lmr-10x-x-109">1                         </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-2-3"> <span class="rm-lmr-10x-x-109">Sample1-A                </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-2-4"> <span class="rm-lmr-10x-x-109">1       </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-2-5"> <span class="rm-lmr-10x-x-109">1          </span></td>
</tr><tr id="TBL-2-3-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-3-1"> <span class="rm-lmr-10x-x-109">2                      </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-3-2"> <span class="rm-lmr-10x-x-109">1                         </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-3-3"> <span class="rm-lmr-10x-x-109">Sample1-B                </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-3-4"> <span class="rm-lmr-10x-x-109">1       </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-3-5"> <span class="rm-lmr-10x-x-109">2          </span></td>
</tr><tr id="TBL-2-4-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-4-1"> <span class="rm-lmr-10x-x-109">3                      </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-4-2"> <span class="rm-lmr-10x-x-109">1                         </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-4-3"> <span class="rm-lmr-10x-x-109">Sample1-C                </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-4-4"> <span class="rm-lmr-10x-x-109">1       </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-4-5"> <span class="rm-lmr-10x-x-109">3          </span></td>
</tr><tr id="TBL-2-5-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-5-1"> <span class="rm-lmr-10x-x-109">4                      </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-5-2"> <span class="rm-lmr-10x-x-109">1                         </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-5-3"> <span class="rm-lmr-10x-x-109">Sample2-A                </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-5-4"> <span class="rm-lmr-10x-x-109">1       </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-5-5"> <span class="rm-lmr-10x-x-109">4          </span></td>
</tr><tr id="TBL-2-6-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-6-1"> <span class="rm-lmr-10x-x-109">5                      </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-6-2"> <span class="rm-lmr-10x-x-109">1                         </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-6-3"> <span class="rm-lmr-10x-x-109">Sample2-B                </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-6-4"> <span class="rm-lmr-10x-x-109">1       </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-6-5"> <span class="rm-lmr-10x-x-109">5          </span></td>
</tr><tr id="TBL-2-7-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-7-1"> <span class="rm-lmr-10x-x-109">6                      </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-7-2"> <span class="rm-lmr-10x-x-109">1                         </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-7-3"> <span class="rm-lmr-10x-x-109">Sample2-C                </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-7-4"> <span class="rm-lmr-10x-x-109">1       </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-7-5"> <span class="rm-lmr-10x-x-109">6          </span></td>
</tr><tr id="TBL-2-8-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-8-1"> <span class="rm-lmr-10x-x-109">7                      </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-8-2"> <span class="rm-lmr-10x-x-109">1                         </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-8-3"> <span class="rm-lmr-10x-x-109">Sample3-A                </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-8-4"> <span class="rm-lmr-10x-x-109">1       </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-8-5"> <span class="rm-lmr-10x-x-109">7          </span></td>
</tr><tr id="TBL-2-9-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-9-1"> <span class="rm-lmr-10x-x-109">8                      </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-9-2"> <span class="rm-lmr-10x-x-109">1                         </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-9-3"> <span class="rm-lmr-10x-x-109">Sample3-B                </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-9-4"> <span class="rm-lmr-10x-x-109">1       </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-9-5"> <span class="rm-lmr-10x-x-109">8          </span></td>
</tr><tr id="TBL-2-10-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-10-1"> <span class="rm-lmr-10x-x-109">9                      </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-10-2"> <span class="rm-lmr-10x-x-109">1                         </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-10-3"> <span class="rm-lmr-10x-x-109">Sample3-C                </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-10-4"> <span class="rm-lmr-10x-x-109">1       </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-10-5"> <span class="rm-lmr-10x-x-109">9          </span></td>
</tr><tr id="TBL-2-11-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-11-1"> <span class="rm-lmr-10x-x-109">10                    </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-11-2"> <span class="rm-lmr-10x-x-109">1                         </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-11-3"> <span class="rm-lmr-10x-x-109">Sample4-A                </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-11-4"> <span class="rm-lmr-10x-x-109">1       </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-11-5"> <span class="rm-lmr-10x-x-109">10        </span></td>
</tr><tr id="TBL-2-12-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-12-1"> <span class="rm-lmr-10x-x-109">11                    </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-12-2"> <span class="rm-lmr-10x-x-109">1                         </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-12-3"> <span class="rm-lmr-10x-x-109">Sample4-B                </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-12-4"> <span class="rm-lmr-10x-x-109">1       </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-12-5"> <span class="rm-lmr-10x-x-109">11        </span></td>
</tr><tr id="TBL-2-13-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-13-1"> <span class="rm-lmr-10x-x-109">12                    </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-13-2"> <span class="rm-lmr-10x-x-109">1                         </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-13-3"> <span class="rm-lmr-10x-x-109">Sample4-C                </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-13-4"> <span class="rm-lmr-10x-x-109">1       </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-13-5"> <span class="rm-lmr-10x-x-109">12        </span></td>
</tr><tr id="TBL-2-14-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-14-1">                </td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-14-2">                  </td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-14-3">                    </td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-14-4">       </td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-14-5">        </td>
</tr><tr id="TBL-2-15-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-15-1">                </td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-15-2">                  </td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-15-3">                    </td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-15-4">       </td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-15-5">        </td>
</tr><tr id="TBL-2-16-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-16-1"> <span class="rm-lmr-10x-x-109">Sample              </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-16-2"> <span class="rm-lmr-10x-x-109">MSstats_Condition  </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-16-3"> <span class="rm-lmr-10x-x-109">MSstats_BioReplicate  </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-16-4">       </td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-16-5">        </td>
</tr><tr id="TBL-2-17-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-17-1"> <span class="rm-lmr-10x-x-109">1                      </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-17-2"> <span class="rm-lmr-10x-x-109">1                         </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-17-3"> <span class="rm-lmr-10x-x-109">1                             </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-17-4">       </td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-17-5">        </td>
</tr><tr id="TBL-2-18-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-18-1"> <span class="rm-lmr-10x-x-109">2                      </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-18-2"> <span class="rm-lmr-10x-x-109">1                         </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-18-3"> <span class="rm-lmr-10x-x-109">2                             </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-18-4">       </td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-18-5">        </td>
</tr><tr id="TBL-2-19-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-19-1"> <span class="rm-lmr-10x-x-109">3                      </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-19-2"> <span class="rm-lmr-10x-x-109">1                         </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-19-3"> <span class="rm-lmr-10x-x-109">3                             </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-19-4">       </td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-19-5">        </td>
</tr><tr id="TBL-2-20-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-20-1"> <span class="rm-lmr-10x-x-109">4                      </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-20-2"> <span class="rm-lmr-10x-x-109">2                         </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-20-3"> <span class="rm-lmr-10x-x-109">4                             </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-20-4">       </td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-20-5">        </td>
</tr><tr id="TBL-2-21-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-21-1"> <span class="rm-lmr-10x-x-109">5                      </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-21-2"> <span class="rm-lmr-10x-x-109">2                         </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-21-3"> <span class="rm-lmr-10x-x-109">5                             </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-21-4">       </td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-21-5">        </td>
</tr><tr id="TBL-2-22-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-22-1"> <span class="rm-lmr-10x-x-109">6                      </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-22-2"> <span class="rm-lmr-10x-x-109">2                         </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-22-3"> <span class="rm-lmr-10x-x-109">6                             </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-22-4">       </td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-22-5">        </td>
</tr><tr id="TBL-2-23-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-23-1"> <span class="rm-lmr-10x-x-109">7                      </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-23-2"> <span class="rm-lmr-10x-x-109">3                         </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-23-3"> <span class="rm-lmr-10x-x-109">7                             </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-23-4">       </td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-23-5">        </td>
</tr><tr id="TBL-2-24-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-24-1"> <span class="rm-lmr-10x-x-109">8                      </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-24-2"> <span class="rm-lmr-10x-x-109">3                         </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-24-3"> <span class="rm-lmr-10x-x-109">8                             </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-24-4">       </td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-24-5">        </td>
</tr><tr id="TBL-2-25-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-25-1"> <span class="rm-lmr-10x-x-109">9                      </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-25-2"> <span class="rm-lmr-10x-x-109">3                         </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-25-3"> <span class="rm-lmr-10x-x-109">9                             </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-25-4">       </td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-25-5">        </td>
</tr><tr id="TBL-2-26-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-26-1"> <span class="rm-lmr-10x-x-109">10                    </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-26-2"> <span class="rm-lmr-10x-x-109">4                         </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-26-3"> <span class="rm-lmr-10x-x-109">10                            </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-26-4">       </td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-26-5">        </td>
</tr><tr id="TBL-2-27-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-27-1"> <span class="rm-lmr-10x-x-109">11                    </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-27-2"> <span class="rm-lmr-10x-x-109">4                         </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-27-3"> <span class="rm-lmr-10x-x-109">11                            </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-27-4">       </td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-27-5">        </td>
</tr><tr id="TBL-2-28-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-28-1"> <span class="rm-lmr-10x-x-109">12                    </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-28-2"> <span class="rm-lmr-10x-x-109">4                         </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-28-3"> <span class="rm-lmr-10x-x-109">12                            </span></td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-28-4">       </td><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-2-28-5">        </td></tr></tbody></table></div>


   </figure>
   </div>

An explanation of the variables can be found in Table 3.

<div class="table">


<!-- l. 1275 --><p class="indent">   </p><figure class="float">


<a id="x1-34003r3"></a>
<a id="x1-34004"></a>
<figcaption class="caption"><span class="id">Table&nbsp;3: Explanation of the column of the experimental design table</span></figcaption><!-- tex4ht:label?: x1-34003r3  -->

 <table class="tabular" id="TBL-5"><colgroup id="TBL-5-1g"><col id="TBL-5-1"><col id="TBL-5-2"></colgroup><tbody><tr id="TBL-5-1-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-5-1-1"> <strong>variables</strong>        </td><td class="td11" style="white-space:normal; text-align:left;" id="TBL-5-1-2"> <!-- l. 1293 --><p class="noindent"><strong>value</strong>                                                                         </p></td>
</tr><tr id="TBL-5-2-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-5-2-1"> <i>Fraction_Group</i>  </td><td class="td11" style="white-space:normal; text-align:left;" id="TBL-5-2-2"> <!-- l. 1293 --><p class="noindent"><span class="rm-lmr-10x-x-109">Index used to group fractions and source files.</span>                                </p></td>
</tr><tr id="TBL-5-3-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-5-3-1"> <i>Fraction</i>           </td><td class="td11" style="white-space:normal; text-align:left;" id="TBL-5-3-2"> <!-- l. 1293 --><p class="noindent"><span class="rm-lmr-10x-x-109">1st, 2nd, .., fraction. Note: All runs must have the same number of
  </span><span class="rm-lmr-10x-x-109">fractions.</span>                                                                                </p></td>
</tr><tr id="TBL-5-4-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-5-4-1"> <i>Spectra_Filepath</i>  </td><td class="td11" style="white-space:normal; text-align:left;" id="TBL-5-4-2"> <!-- l. 1293 --><p class="noindent"><span class="rm-lmr-10x-x-109">Path to mzML files</span>                                                                   </p></td>
</tr><tr id="TBL-5-5-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-5-5-1"> <i>Label</i>               </td><td class="td11" style="white-space:normal; text-align:left;" id="TBL-5-5-2"> <!-- l. 1293 --><p class="noindent"><span class="rm-lmr-10x-x-109">label-free: always 1</span>                                                                   </p></td>
</tr><tr id="TBL-5-6-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-5-6-1"> <i></i>               </td><td class="td11" style="white-space:normal; text-align:left;" id="TBL-5-6-2"> <!-- l. 1293 --><p class="noindent"><span class="rm-lmr-10x-x-109">TMT6Plex: 1...6</span>                                                                      </p></td>
</tr><tr id="TBL-5-7-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-5-7-1"> <i></i>               </td><td class="td11" style="white-space:normal; text-align:left;" id="TBL-5-7-2"> <!-- l. 1293 --><p class="noindent"><span class="rm-lmr-10x-x-109">SILAC with light and heavy: 1..2</span>                                                 </p></td>
</tr><tr id="TBL-5-8-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-5-8-1"> <i>Sample</i>             </td><td class="td11" style="white-space:normal; text-align:left;" id="TBL-5-8-2"> <!-- l. 1293 --><p class="noindent"><span class="rm-lmr-10x-x-109">Index of sample measured in the specified label X, in fraction Y of
  </span><span class="rm-lmr-10x-x-109">fraction group Z.</span>                                                                      </p></td>
</tr><tr id="TBL-5-9-"><td class="td11" style="white-space:nowrap; text-align:left;" id="TBL-5-9-1"> <i>Conditions</i>        </td><td class="td11" style="white-space:normal; text-align:left;" id="TBL-5-9-2"> <!-- l. 1293 --><p class="noindent"><span class="rm-lmr-10x-x-109">Further specification of different conditions (e.g. MSstats_Condition;
  </span><span class="rm-lmr-10x-x-109">MSstats_BioReplicate)</span>                                                              </p></td>

</tr></tbody></table>


   </figure>
   </div>

The conditions are highly dependent on the type of experiment and on which kind of analysis you want to perform. For the `MSstats` analysis the information which sample belongs to which condition and if there are biological replicates are mandatory. This can be specified in further condition columns as explained in Table 3. For a detailed description of the MSstats-specific terminology, see their documentation e.g. in the R vignette.

#### Conversion and downstream analysis

Conversion of the OpenMS-internal consensusXML format (which is an aggregation of quantified and possibly identified features across several MS-maps) to a table (in MSstats-conformant CSV format) is very easy. First, create a new KNIME workflow. Then, run the **MSstatsConverter** node with a consensusXML and the manually created (e.g. in Excel) experimental design as inputs (loaded via **Input File** nodes). The first input can be found in:

`ExamplexData` ► `iPRG2015` ► `openmsLFQResults` ► `iPRGxlfq.consensusXML`

This file was generated by using the `Workflows` ► `openmsLFQxiPRG2015.knwf` workflow (seen in Fig. 18). The second input is specified in:

`ExamplexData` ► `iPRG2015` ► `experimentalxdesign.tsv`

Adjust the parameters in the config dialog of the converter to match the given experimental design file and to use a simple summing for peptides that elute in multiple features (with the same charge state, i.e. m/z value).

|**parameter**|**value**|
|------------:|:--------|
|*msstats_bioreplicate*|MSstats_Bioreplicate|
|*msstats_condition*|MSstats_Condition|
|*labeled_reference_peptides*|false|
|*retention_time_summarization_method (advanced)*|sum|

The downstream analysis of the peptide ions with `MSstats` is performed in several steps. These steps are reflected by several KNIME R nodes, which consume the output of **MSstatsConverter**. The outline of the workflow is shown in Figure 19.

|![MSstats analysis using KNIME](../images/openms-user-tutorial/labelfree/MSstats.png)|
|:--:|
|Figure 19: MSstats analysis using KNIME. The individual steps (Preprocessing, Group Comparisons, Result Data Renaming, and Export) are split among several consecutive nodes.|

We load the file resulting from **MSStatsConverter** either by saving it with an **Output File** node and reloading it with the **File Reader**.  Alternatively, for advanced users, you can use a URI Port to Variable node and use the variable in the File Reader config dialog (**V** button - located on the right of the **Browse** button) to read from the temporary file.

##### Preprocessing

The first node (**Table to R**) loads `MSstats` as well as the data from the previous KNIME node and performs a preprocessing step on the input data. The following inline R script ( needs to be pasted into the config dialog of the node):

```r
library(MSstats)
data <- knime.in
quant <- OpenMStoMSstatsFormat(data, removeProtein_with1Feature = FALSE)
```

The inline R script allows further preparation of the data produced by **MSstatsConverter** before the actual analysis is performed. In this example, the lines with proteins, which were identified with only one feature, were retained. Alternatively they could be removed.
In the same node, most importantly, the following line transforms the data into a format that is understood by `MSstats`:

```r
processed.quant <- dataProcess(quant, censoredInt = 'NA')
```
Here, `dataProcess` is one of the most important functions that the R package provides. The function performs the following steps:

1. Logarithm transformation of the intensities
2. Normalization
3. Feature selection
4. Missing value imputation
5. Run-level summarization

In this example, we just state that missing intensity values are represented by the `NA` string.

##### Group Comparison

The goal of the analysis is the determination of differentially-expressed proteins among the different conditions C1-C4. We can specify the comparisons that we want to make in a *comparison* matrix. For this, let’s consider the following example:

![comparison matrix](../images/openms-user-tutorial/labelfree/handout-clean129x.svg)

This matrix has the following properties:

- The number of rows equals the number of comparisons that we want to perform, the number of columns equals the number of conditions (here, column 1 refers to C1, column 2 to C2 and so forth).
- The entries of each row consist of exactly one 1 and one -1, the others must be 0.
- The condition with the entry `1` constitutes the enumerator of the log2 fold-change. The one with entry `-1` denotes the denominator. Hence, the first row states that we want calculate:
```{math}
 \begin{equation} \log_2 \frac{C_{2}}{C_{1}} \end{equation}
 ```
We can generate such a matrix in R using the following code snippet in (for example) a new **R to R** node that takes over the R workspace from the previous node with all its variables:

```r
comparison1<-matrix(c(-1,1,0,0),nrow=1)   
comparison2<-matrix(c(-1,0,1,0),nrow=1)

comparison3<-matrix(c(-1,0,0,1),nrow=1)  
comparison4<-matrix(c(0,-1,1,0),nrow=1)

comparison5<-matrix(c(0,-1,0,1),nrow=1)  
comparison6<-matrix(c(0,0,-1,1),nrow=1)

comparison <- rbind(comparison1, comparison2, comparison3, comparison4, comparison5, comparison6)
row.names(comparison)<-c("C2-C1","C3-C1","C4-C1","C3-C2","C4-C2","C4-C3")
```

Here, we assemble each row in turn, concatenate them at the end, and provide row names for labeling the rows with the respective condition.
In MSstats, the group comparison is then performed with the following line:

```r
test.MSstats <- groupComparison(contrast.matrix=comparison, data=processed.quant)
```
No more parameters need to be set for performing the comparison.

##### Result processing

In a next R to R node, the results are being processed. The following code snippet will rename the spiked-in proteins to A,B,C,D,E, and F and remove the names of other proteins, which will be beneficial for the subsequent visualization, as for example performed in Figure 20:

```r
  test.MSstats.cr <- test.MSstats$ComparisonResult   


  # Rename spiked ins to A,B,C....  
  pnames <- c("A", "B", "C", "D", "E", "F")

  names(pnames) <- c(  
  "sp|P44015|VAC2_YEAST",  
  "sp|P55752|ISCB_YEAST",

  "sp|P44374|SFG2_YEAST",  
  "sp|P44983|UTR6_YEAST",  
  "sp|P44683|PGA4_YEAST",

  "sp|P55249|ZRT4_YEAST"  
  )  

  test.MSstats.cr.spikedins <- bind_rows(

  test.MSstats.cr[grep("P44015", test.MSstats.cr$Protein),],

  test.MSstats.cr[grep("P55752", test.MSstats.cr$Protein),],

  test.MSstats.cr[grep("P44374", test.MSstats.cr$Protein),],

  test.MSstats.cr[grep("P44683", test.MSstats.cr$Protein),],

  test.MSstats.cr[grep("P44983", test.MSstats.cr$Protein),],

  test.MSstats.cr[grep("P55249", test.MSstats.cr$Protein),]  
  )  
  # Rename Proteins

  test.MSstats.cr.spikedins$Protein <- sapply(test.MSstats.cr.spikedins$Protein, function(x) {pnames[as.character(x)]})



  test.MSstats.cr$Protein <- sapply(test.MSstats.cr$Protein, function(x) {


    x <- as.character(x)  

    if (x %in% names(pnames)) {


      return(pnames[as.character(x)])  
      } else {  
      return("")

    }
  })

```

##### Export

The last four nodes, each connected and making use of the same workspace from the last node, will export the results to a textual representation and volcano plots for further inspection. Firstly, quality control can be performed with the following snippet:

```r
qcplot <- dataProcessPlots(processed.quant, type="QCplot",   
        ylimDown=0,

which.Protein = 'allonly',
width=7, height=7, address=F)
```

The code for this snippet is embedded in the first output node of the workflow. The resulting boxplots show the log2 intensity distribution across the MS runs.
The second node is an **R View (Workspace)** node that returns a Volcano plot which displays differentially expressed proteins between conditions C2 vs. C1. The plot is described in more detail in the following Result section. This is how you generate it:

```r
groupComparisonPlots(data=test.MSstats.cr, type="VolcanoPlot",

                    width=12, height=12,dot.size = 2,ylimUp = 7,

                    which.Comparison = "C2-C1",
                    address=F)
```
The last two nodes export the `MSstats` results as a KNIME table for potential further analysis or for writing it to a (e.g. csv) file. Note that you could also write output inside the Rscript if you are familiar with it. Use the following for an **R to Table** node exporting all results:

```r
knime.out <- test.MSstats.cr
```
And this for an **R to Table** node exporting only results for the spike-ins:

```r
knime.out <- test.MSstats.cr.spikedins
```

#### Result

An excerpt of the main result of the group comparison can be seen in Figure 20.

|![Volcano plots c2_c1](../images/openms-user-tutorial/labelfree/c2_c1-.png)|
|:--:|
|![Volcano plots c3_c2](../images/openms-user-tutorial/labelfree/c3_c2-.png)|
|Figure 20: Volcano plots produced by the Group Comparison in MSstats The dotted line indicates an adjusted p-value threshold|

The Volcano plots show differently expressed spiked-in proteins. In the left plot, which shows the fold-change C2-C1, we can see the proteins D and F (`sp|P44983|UTR6_YEAST` and `sp|P55249|ZRT4_YEAST`) are significantly over-expressed in C2, while the proteins B,C, and E (`sp|P55752|ISCB_YEAST`, `sp|P55752|ISCB_YEAST`, and `sp|P44683|PGA4_YEAST`) are under-expressed. In the right plot, which shows the fold-change ratio of C3 vs. C2, we can see the proteins E and C (`sp|P44683|PGA4_YEAST` and `sp|P44374|SFG2_YEAST`) over-expressed and the proteins A and F (`sp|P44015|VAC2_YEAST` and `sp|P55249|ZRT4_YEAST`) under-expressed. The plots also show further differentially-expressed proteins, which do not belong to the spiked-in proteins.

The full analysis workflow can be found under:
`Workflows` ► `MSstatsxstatPostProcessingxiPRG2015.knwf`

## Protein inference

In the last chapter, we have successfully quantified peptides in a label-free experiment. As a next step, we will further extend this label-free quantification workflow by protein inference and protein quantification capabilities. This workflow uses some of the more advanced concepts of KNIME, as well as a few more nodes containing R code. For these reasons, you will not have to build it yourself. Instead, we have already prepared and copied this workflow to the USB sticks. Just import `Workflows` ► `labelfree_with_protein_quantification.knwf` into KNIME via the menu entry **File** > **Import KNIME workflow** > **Select file** and double-click the imported workflow in order to open it.

Before you can execute the workflow, you again have to correct the locations of
the files in the Input Files nodes (don’t forget the one for the FASTA database inside the “ID” meta node). Try and run your workflow by executing all nodes at once.

### Extending the LFQ workflow by protein inference and quantification

We have made the following changes compared to the original label-free quantification workflow from the last chapter:

- First, we have added a **ProteinQuantifier** node and connected its input port to the output port of the **ConsensusMapNormalizer** node.
- This already enables protein quantification. **ProteinQuantifier** quantifies peptides by summarizing over all observed charge states and proteins by summarizing over their quantified peptides. It stores two output files, one for the quantified peptides and one for the proteins.
- In this example, we consider only the protein quantification output file, which is written to the first output port of **ProteinQuantifier**.
-  Because there is no dedicated node in KNIME to read back the **ProteinQuantifier** output file format into a KNIME table, we have to use a workaround. Here, we have added an additional URI Port to Variable node which converts the name of the output file to a so-called “flow variable” in KNIME. This variable is passed on to the next node **CSV Reader**, where it is used to specify the name of the input file to be read. If you double-click on **CSV Reader**, you will see that the text field, where you usually enter the location of the CSV file to be read, is greyed out. Instead, the flow variable is used to specify the location, as indicated by the small green button with the “v=?” label on the right.
- The table containing the **ProteinQuantifier** results is filtered one more time in order to remove decoy proteins. You can have a look at the final list of quantified protein groups by right-clicking the **Row Filter** and selecting **Filtered**.
- By default, i.e., when the second input port `protein_groups` is not used, **ProteinQuantifier** quantifies proteins using only the unique peptides, which usually results in rather low numbers of quantified proteins.
- In this example, however, we have performed protein inference using Fido and
used the resulting protein grouping information to also quantify indistinguishable proteins. In fact, we also used a greedy method in **FidoAdapter** (parameter `greedy_group_resolution`) to uniquely assign the peptides of a group to the most probable protein(s) in the respective group. This boosts the number of quantifications but slightly raises the chances to yield distorted protein quantities.
- As a prerequisite for using **FidoAdapter**, we have added an **IDPosteriorErrorProbability** node within the ID meta node, between the **XTandemAdapter** (note the replacement of OMSSA because of ill-calibrated scores) and **PeptideIndexer**. We have
set its parameter `prob_correct` to `true`, so it computes posterior probabilities instead of posterior error probabilities (1 - PEP). These are stored in the resulting idXML file and later on used by the Fido algorithm. Also note that we excluded FDR filtering from the standard meta node. Harsh filtering before inference impacts the calibration of the results. Since we filter peptides before quantification though, no potentially random peptides will be included in the results anyway.
- Next, we have added a third outgoing connection to our ID meta node and connected it to the second input port of **ZipLoopEnd**. Thus, KNIME will wait until all input files have been processed by the loop and then pass on the resulting list of idXML files to the subsequent IDMerger node, which merges all identifications from all idXML files into a single idXML file. This is done to get a unique assignment of peptides to proteins over all samples.
- Instead of the meta node **Protein inference** with **FidoAdapter**, we could have just used a **FidoAdapter** node ( **Community Nodes** > **OpenMS** > **ID Processing**). However, the meta node contains an additional subworkflow which, besides calling **FidoAdapter**, performs a statistical validation (e.g. (pseudo) receiver operating curves; ROCs) of the protein inference results using some of the more advanced KNIME and R nodes. The meta node also shows how to use **MzTabExporter** and **MzTabReader**.

### Statistical validation of protein inference results

In the following section, we will explain the subworkflow contained in the **Protein inference with FidoAdapter** meta node.

#### Data preparation

For downstream analysis on the protein ID level in KNIME, it is again necessary to convert the idXML-file-format result generated from **FidoAdapter** into a KNIME table.

- We use the **MzTabExporter** to convert the inference results from **FidoAdapter** to a human readable, tab-separated mzTab file. mzTab contains multiple sections,
that are all exported by default, if applicable. This file, with its different sections can again be read by the **MzTabReader** that produces one output in KNIME table
format (triangle ports) for each section. Some ports might be empty if a section did not exist. Of course, we continue by connecting the downstream nodes with the protein section output (second port).
- Since the protein section contains single proteins as well as protein groups, we filter them for single proteins with the standard **Row Filter**.

#### ROC curve of protein ID

ROC Curves (Receiver Operating Characteristic curves) are graphical plots that visualize sensitivity (true-positive rate) against fall-out (false positive rate). They are often used to judge the quality of a discrimination method like e.g., peptide or protein identification engines. ROC Curve already provides the functionality of drawing ROC curves for binary classification problems. When configuring this node, select the `opt_global_target_decoy` column as the class (i.e. target outcome) column. We want to find out, how good our inferred protein probability discriminates between them,
therefore add `best_search_engine_score[1]` (the inference engine score is treated like a peptide search engine score) to the list of *”Columns containing positive class probabilities”*. View the plot by right-clicking and selecting **View: ROC Curves**. A perfect classifier has
an area under the curve (AUC) of 1.0 and its curve touches the upper left of the plot. However, in protein or peptide identification, the ground-truth (i.e., which target
identifications are true, which are false) is usually not known. Instead, so called pseudoROC Curves are regularly used to plot the number of target proteins against the false
discovery rate (FDR) or its protein-centric counterpart, the q-value. The FDR is approximated by using the target-decoy estimate in order to distinguish true IDs from
false IDs by separating target IDs from decoy IDs.

#### Posterior probability and FDR of protein IDs

ROC curves illustrate the discriminative capability of the scores of IDs. In the case of protein identifications, Fido produces the posterior probability of each protein as
the output score. However, a perfect score should not only be highly discriminative (distinguishing true from false IDs), it should also be “calibrated” (for probability indicating that all IDs with reported posterior probability scores of 95% should roughly have a 5% probability of being false. This implies that the estimated number of false
positives can be computed as the sum of posterior error probabilities ( = 1 - posterior probability) in a set, divided by the number of proteins in the set. Thereby a
posterior-probability-estimated FDR is computed which can be compared to the actual target-decoy FDR. We can plot calibration curves to help us visualize the quality of
the score (when the score is interpreted as a probability as Fido does), by comparing how similar the target-decoy estimated FDR and the posterior probability estimated
FDR are. Good results should show a close correspondence between these two measurements, although a non-correspondence does not necessarily indicate wrong results.

The calculation is done by using a simple R script in R snippet. First, the target decoy protein FDR is computed as the proportion of decoy proteins among all significant protein IDs. Then posterior probabilistic-driven FDR is estimated by the average of the posterior error probability of all significant protein IDs. Since FDR is the property for a group of protein IDs, we can also calculate a local property for each protein: the q-value of a certain protein ID is the minimum FDR of any groups of protein IDs
that contain this protein ID. We plot the protein ID results versus two different kinds of FDR estimates in R View(Table) (see Fig. 22).

|![The workflow of statistical analysis of protein inference results](../images/openms-user-tutorial/protein-inference/inference_metanode.png)|
|:--:|
|Figure 21: The workflow of statistical analysis of protein inference results|
|![The pseudo-ROC Curve of protein IDs](../images/openms-user-tutorial/protein-inference/proteinFDR.png)|
|:--:|
|Figure 22: The pseudo-ROC Curve of protein IDs. The accumulated number of protein IDs is plotted on two kinds of scales: target-decoy protein FDR and Fido posterior probability estimated FDR. The largest value of posterior probability estimated FDR is already smaller than 0.04, this is because the posterior probability output from Fido is generally very high|

## Isobaric analysis

In the last chapters, we identified and quantified peptides in a label-free experiment.

In this section, we would like to introduce a possible workflow for the analysis of isobaric data.

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

[^1]: OpenMS, [OpenMS home page]((http://www.openms.de/)) [online].

[^2]: M. Sturm, A. Bertsch, C. Gröpl, A. Hildebrandt, R. Hussong, E. Lange, N. Pfeifer,
O. Schulz-Trieglaff, A. Zerck, K. Reinert, and O. Kohlbacher, OpenMS - an opensource software framework for mass spectrometry., BMC bioinformatics 9(1)
(2008), doi:10.1186/1471-2105-9-163. 7, 83

[^3]: H. L. Röst, T. Sachsenberg, S. Aiche, C. Bielow, H. Weisser, F. Aicheler, S. Andreotti,
H.-C. Ehrlich, P. Gutenbrunner, E. Kenar, et al., OpenMS: a flexible open-source
software platform for mass spectrometry data analysis, Nature Methods 13(9),
741–748 (2016). 7

[^4]: O. Kohlbacher, K. Reinert, C. Gröpl, E. Lange, N. Pfeifer, O. Schulz-Trieglaff, and
M. Sturm, TOPP–the OpenMS proteomics pipeline., Bioinformatics 23(2) (Jan.
2007). 7, 83
