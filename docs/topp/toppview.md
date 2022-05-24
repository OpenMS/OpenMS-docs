TOPPView
=======

**TOPPView** is a viewer for MS and HPLC-MS data. It can be used to inspect files in mzML, mzData, mzXML and several other
file formats. It also supports viewing data from an OpenMS database. The following figure shows two instances of TOPPView
displaying a HPLC-MS map and a MS raw spectrum:

![](../../images/topp/TOPPView.png)

More information about TOPPView can be found in the [TOPP tutorial](../../tutorials/TOPP/TOPP-tutorial.md).

**The command line parameters of this tool are**:

```
TOPPView -- A viewer for mass spectrometry data.

Usage:
 TOPPView [options] [files]

Options are:
  --help           Shows this help
  -ini <File>      Sets the INI file (default: ~/.TOPPView.ini)
  --force          Forces scan for new tools/utils

Hints:
 - To open several files in one window put a '+' in between the files.
 - '@bw' after a map file displays the dots in a white to black gradient.
 - '@bg' after a map file displays the dots in a grey to black gradient.
 - '@b'  after a map file displays the dots in black.
 - '@r'  after a map file displays the dots in red.
 - '@g'  after a map file displays the dots in green.
 - '@m'  after a map file displays the dots in magenta.
 - Example: 'TOPPView 1.mzML + 2.mzML @bw + 3.mzML @bg'
```
