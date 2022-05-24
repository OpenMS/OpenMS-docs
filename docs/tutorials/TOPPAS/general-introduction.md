General Introduction
====================

**TOPPAS**  allows you to create, edit, open, save, and run TOPP workflows. Pipelines can be created conveniently in a
GUI. The parameters of all involved tools can be edited within TOPPAS and are also saved as part of the pipeline
definition in the `.toppas` file. Furthermore, **TOPPAS** interactively performs validity checks during the pipeline
editing process and before execution (i.e., a dry run of the entire pipeline), in order to prevent the creation of
invalid workflows. Once set up and saved, a workflow can also be run without the GUI using `ExecutePipeline -in <file>.`

The following figure shows a simple example pipeline that has just been created and executed successfully:

![](../../images/tutorials/toppas/TOPPAS_simple_example.png)

To create a new TOPPAS file, do any of the following:

- Open TOPPAS without providing any existing workflow - an empty workflow will be opened automatically.
- In a running TOPPAS program, choose: **File** > **New**
- Create an empty file in your file browser (explorer) with the suffix `.toppas` and double-click it (on Windows systems
  all `.toppas` files are associated with TOPPAS automatically during installation of OpenMS, on Linux, and macOS you
  might need to manually associate the extension).
