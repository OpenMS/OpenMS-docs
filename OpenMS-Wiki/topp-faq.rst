==========================
TOPP Frequently Asked Questions
==========================

.. contents:: Some of our most frequently asked questions regarding TOPP are:

I'm getting the error message "Unexpected internal error (unable to allocate enough memory (size = 0 bytes)".
############################################################################################################

Call "OpenMSInfo" and look at "OS Information".

If you are using the 32bit version of OpenMS, the data you are processing is probably too big (e.g. using RAW data files bigger than 1.5 GB as input, or many featureXML files etc). You can now either:

* Switch to the 64bit Version of OpenMS. Be aware though that your Operating System also needs to have 64bit. Furthermore your PC should have sufficient RAM, to hold the data. Otherwise your hard drive will be used extensively for swapping and processing will take longer.
* On 32bit Windows systems you can try the increase the allowed amount of memory from 2GB to 3GB by using the "/3GB" boot switch (boot.ini). This might already do the trick. However, if your data again gets bigger, this solution will only help temporarily. Google "3GB windows". This trick does not depend on the amount of memory installed on your system! You can use it even if you have only 1GB or 2GB of RAM, although you hard drive will be used for swapping then.
* On 32bit Linux systems: sorry, we cannot do anything. Use a 64bit system or reduce the amount of data.

If you already have the 64bit version, you probably encountered a bug in our software. Please contact the mailing list (see OpenMS.de).

How to disable the OpenMS update check.
######################################

Starting with OpenMS 2.1 all TOPP tools will check for updated versions of the tools online and will print an information message if a newer version is available. This version check occurs only once per day and tool. Information on which tools are executed will be collected anonymously to identify which tools are no longer used and to optimally distribute development resources. If the feature causes problems or concerns, it can be disabled at build or runtime:

* Build time: disabling it in the build script (switch ENABLE_UPDATE_CHECK to "OFF" )
* Runtime: setting the environment variable (OPENMS_DISABLE_UPDATE_CHECK to "ON")

How can I change the temporary directory that OpenMS uses?
##########################################################

By default OpenMS will use the system wide temporary directory (defined either by TMPDIR, TEMP or TMP environmental variable). You can override this by setting the parameter "temp_dir" in the OpenMS.ini or setting the environmental variable OPENMS_TMPDIR.

Calling msConvert (of ProteoWizard) results in small mzML files with no peak data.


The Thermo interface expects an English locale setting. Otherwise it will silently forget to return peak data. Set your locale to English and it should work.

Some TOPP tools always crashes when executed. Other TOPP tools work properly.
#############################################################################

If a error message similar to

.. code:: console
 OpenMS::File::find(...) of File.cpp error message: the file 'CHEMISTRY/unimod.xml' could not be found

is shown, you have probably moved your OpenMS installation manually?! Then the TOPP tools cannot find some required data files anymore, e.g. XML schema files or chemical isotope data.

Either of the following actions should fix your problem:

* Set the environment variable OPENMS_DATA_PATH to your <OpenMS>/share/OpenMS/ folder.
* [developers only] Use the cmake option -D CMAKE_INSTALL_PREFIX=... to set the installation directory. Run 'make OpenMS TOPP UTILS' again.
* [developers only] Execute cmake in the new location and run 'make OpenMS TOPP UTILS' again.

A TOPP tool crashes when loading a certain input file. Other files work properly.
#################################################################################
If an XML input file is used, please check if the file is valid.

For most XML data formats, this can be done using the FileInfo tool:

.. code:: console
  FileInfo -v -in <file>

You can also check for corrupt data in peak files:

.. code:: console
  FileInfo -c -in <file>
