User Interface
=============

## Introduction

The following figure shows the **TOPPAS** main window and a pipeline which is just being created. The user has added
some tools by drag and dropping them from the TOPP tool list on the left onto the central window. Additionally, the user
has added nodes for input and output files.

Next, the user has drawn some connections between the tools which determine the data flow of the pipeline. Connections
an be drawn by first *deselecting* the desired source node (by clicking anywhere but not on another node) and then
dragging the mouse from the source to the target node (if a *selected* node is dragged, it is moved on the canvas
instead). When a connection is created and the source (the target) has more than one output (input) parameter, an
input/output parameter mapping dialog shows up and lets the user select the output parameter of the source node and the
input parameter of the target node for this data flow, shown here for the connection between PeptideIndexer and
FalseDiscoveryRate. If the file types of the selected input and output parameters are not compatible with each other,
**TOPPAS** will refuse to add the connection. It will also refuse to add a connection if it would create a cycle in the
workflow, or if it just would not make sense, e.g. if its target is an input file node. The connection between the input
file node (#1) and the OMSSAAdapter (#5) tool is painted yellow which indicates it is not ready yet, because no input
files have been specified.

![](../../images/tutorials/TOPPAS_edges.png)

The input/output mapping of connections can be changed at any time during the editing process by double-clicking an
connections or by selecting `Edit I/O mapping` from the context menu which appears when a connection is right-clicked.
All visible items (i.e. connections and the different kinds of nodes) have such a context menu. For a detailed list of
the different menus and their entries, see [Menus](user-interface.md#menus).

The following figure shows a possible next step: the user has double-clicked one of the tool nodes in order to configure
its parameters. By default, the standard parameters are used for each tool. Again, this can also be done by selecting
`Edit parameters` from the context menu of the tool.

![](../../images/tutorials/TOPPAS_parameters.png)

Once the pipeline has been set up, the input files have to be specified before the pipeline can be executed. This is
done by double-clicking an input node and selecting the desired files in the dialog that appears. Input nodes have a
special mode named `recycling mode`, i.e., if the input node has fewer files than the following node has rounds
(as it might have two incoming connections) then the files are recycled until all rounds are satisfied. This might be
useful if one input node specifies a single database file (for a Search-Adapter like Mascot) and another input node has
the actual MS2 experiments (which is usually more than one). Then the database input node would be set to `recycle` the
database file, i.e. use it for every run of the MascotAdapter node. The input list can be recycled an arbitrary number
of times, but the recycling has to be `complete`, i.e. the number of rounds of the downstream node have to be a multiple
of the number of input files. Recycling mode can be activated by right-clicking the input node and selecting the according
entry from the context menu. Finally, if you have input and output nodes at every end of your pipeline and all
connections are green, select `Pipeline` > `Run` in the menu bar or just press `F5`.

![](../../images/tutorials/TOPPAS_run_options.png)

When asked for an output file directory where a sub-directory, `TOPPAS_out`, will be created. This directory will
contain the output files. Specify the number of jobs TOPPAS is allowed to run in parallel, if a number greater than 1 is
selected, TOPPAS will parallelize the pipeline execution in the following scenarios:

- A tool has to process more than one file. In this case, multiple files can be processed in parallel.
- The pipeline contains multiple branches that are independent of each other. In this case, multiple tools can run in
  parallel.

Be careful with this setting, however, as some of the TOPP tools require large amounts of RAM (depending on the size of
the dataset). Running too many parallel jobs on a machine with not enough memory will cause problems. Also, do not
confuse this setting with the `threads` parameter of the individual TOPP tools: every TOPP tool has this parameter
specifying the maximum number of threads the tool is allowed to use (although only a subset of the TOPP tools make use
of this parameter, since there are tasks that cannot be computed in parallel). Be especially careful with combinations
of both parameters! For a pipeline containing the `FeatureFinderCentroided`, as an example, and set its `threads`
parameter to 8, and additionally set the number of parallel jobs in **TOPPAS** to 8, then you end up using 64 threads.

In addition to `TOPPAS_out`, a `TOPPAS_tmp` directory will be created in the OpenMS temp path (call the `OpenMSInfo`
tool to see where exactly). It will contain all temporary files that are passed from tool to tool within the pipeline.
Both folders contain further sub-directories which are named after the number in the top-left corner of the node they
belong to (plus the name of the tool for temporary files). During pipeline execution, the status lights in the top-right
corner of every tool show how many files have already been processed and the overall number of files to be processed by
this tool. When the execution has finished, check the generated output files of every node quickly by selecting
`@a Open @a files @a in @a TOPPView` or `@a Open @a containing @a folder` from the context menu (right click on the node).

## Mouse and keyboard

Using the mouse:

- drag and drop tools from the TOPP tool list onto the workflow window (you can also double-click them instead)
- select items (by clicking)
- select multiple items (by holding down `CTRL` while clicking)
- select multiple items (by holding down `CTRL` and dragging the mouse in order to "catch" items with a selection
  rectangle)
- move all selected items (by dragging one of them)
- draw a new connection from one node to another (by dragging; source must be deselected first)
- specify input files (by double-clicking an input node)
- configure parameters of tools (by double-clicking a tool node)
- specify the input/output mapping of connections (by double-clicking a connection)
- translate the view (by dragging anywhere but on an item)
- zoom in and out (using the mouse wheel)
- make the context menu of an item appear (by right-clicking it)

Using the keyboard:

- delete all selected items (`DEL` or `BACKSPACE`)
- zoom in and out (`+`/`-`)
- run the pipeline (`F5`)
- open this tutorial (`F1`)

Using the mouse` + `keyboard:

- copy a node's parameters to another node (only parameters with identical names will be copied, e.g.,
  `fixed_modifications`) (`CTRL` while creating an edge) The edge will be colored as dark magenta to indicate parameter
  copying.

## Menus

### Menu bar

In the `File` menu:

- create a new, empty workflow (`New`)
- open an existing one (`Open`)
- open an example file (`Open example file`)
- include an existing workflow to the current workflow (`Include`)
- visit the online workflow repository (`Online repository)`
- save a workflow (`Save`/`Save as`)
- export the workflow as image (`Export as image`)
- refresh the parameter definitions of all tools contained in the workflow (`Refresh parameters`)
- close the current window (`Close`)
- load and save TOPPAS resource files (`.trf`) (`Load`/`Save OPPAS resource file`)

In the `Pipeline` menu:

- run a pipeline (`Run`)
- abort a currently running pipeline (`Abort`)

In the `Windows` menu:

- make the TOPP tool list window on the left, the description window on the right, and the log message at the bottom
  (in)visible.

In the `Help` menu:

- go to the OpenMS website (`OpenMS website`)
- open this tutorial (`TOPPAS tutorial`)

### Context menus

In the context menu of an `input node`:

- specify the input files
- open the specified files in TOPPView
- open the input files' folder in the window manager (explorer)
- toggle the `recycling` mode
- copy, cut, and remove the node

In the context menu of a `tool`:

- configure the parameters of the tool
- resume the pipeline at this node
- open its temporary output files in TOPPView
- open the temporary output folder in the file manager (explorer)
- toggle the `recycling` mode
- copy, cut, and remove the node

In the context menu of a `Merger` or `Collector`:

- toggle the `recycling` mode
- copy, cut, and remove the node

In the context menu of an `output node`:

- open the output files in TOPPView
- open the output files' folder in the window manager (explorer)
- copy, cut, and remove the node
