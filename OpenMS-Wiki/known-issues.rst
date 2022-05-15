============
Known Issues
============

Have a look at the Internal FAQ, if you cannot find your answer here. Write to the OpenMS mailing list, if the problem persists.

.. contents:: Contents

Known issues on Windows
#######################
* **Starting a (GUI) TOPP executable (like TOPPView or FeatureFinderCentroided) gives "The application was unable to start correctly (0xc0000005). Click OK to close the application"**

  When you run the tool in Debug mode and look where it crashes, you might actually find it to be a very weird place - e.g. when creating a perfectly legal String from a QString:
  .. code:: c++

    QFileInfo fi(file.toQString());

    return fi.path()
*


Known issues on Linux
#######################
