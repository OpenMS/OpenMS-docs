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

    return fi.path();

  The reason this happens is usually: you've mixed DLL's from multiple runtimes (e.g. compiled with VS10 and VS9). This can easily happen, if you use your Qt (build with VS9) to link against your OpenMS (build with VS10). The loader will load VS9 and VS10 runtimes and will NOT tell you that they conflict. Instead, very weird things are going to happen. You can identify if you are affected by looking at the DLL's that are loaded via daisy-chaining - see either DependencyWalker's output or the 'output' window in VS when running the app from inside VS. It might read:

  .. code::

   'MSSimulator.exe': Loaded 'C:\Windows\winsxs\amd64_microsoft.vc90.debugcrt_1fc8b3b9a1e18e3b_9.0.21022.8_none_4ec74c6b3093419c\msvcp90d.dll', Symbols loaded.
   'MSSimulator.exe': Loaded 'C:\Windows\winsxs\amd64_microsoft.vc90.debugcrt_1fc8b3b9a1e18e3b_9.0.21022.8_none_4ec74c6b3093419c\msvcr90d.dll', Symbols loaded.
   'MSSimulator.exe': Loaded 'C:\dev\qt-everywhere-opensource-src-4.7.1\bin\QtSqld4.dll', Symbols loaded.
*


Known issues on Linux
#######################
