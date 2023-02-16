macOS
====================

## Install via macOS installer

To install OpenMS on macOS, run the following steps:

1. Download and install the macOS drag-and-drop installer from the [archive](https://abibuilder.cs.uni-tuebingen.de/archive/openms/OpenMSInstaller/release/latest/).
2. Double click on the downloaded file. It will start to open the `OpenMS-<version>-macOS.dmg` disk image file.

```{image} ../images/installations/macos/opening-openms2-8-macos.png
:alt: Opening OpenMS-<version>-macOS.dmg
:width: 500px
```

3. Verify the download.

```{image} ../images/installations/macos/verifying-openms2-8-macos.png
:alt: Verifying OpenMS-<version>-macOS.dmg
:width: 500px
```

4. Agree to the license agreements.

```{image} ../images/installations/macos/license-agreements.png
:alt: License agreement
:width: 500px
```

5. Drag OpenMS to the Applications folder.

```{image} ../images/installations/macos/move-openms-to-applications.png
:alt: Move to Applications
:width: 500px
```

6. It will start copying to applications.

```{image} ../images/installations/macos/preparing-to-copy-to-applications.png
:alt: Preparing to copy to Applications
:width: 500px
```

```{image} ../images/installations/macos/copying-to-applications.png
:alt: Copying to Applications
:width: 500px
```


To use {term}`TOPP` as regular app in the shell, add the following lines to the `~/.profile` file.

```bash
export OPENMS_TOPP_PATH=<OpenMS-PATH>
source ${OPENMS_TOPP_PATH}/.TOPP_bash_profile
```

Make sure `<OpenMS-PATH>` points to the folder where OpenMS is installed locally (e.g., `/Applications/OpenMS-<version>`)

## Install via Conda or Bioconda

Follow the equivalent <a href="installation-on-gnu-linux.html#install-via-conda">instructions for GNU/Linux</a>.

## Known Issues

1. Nothing happens when you click OpenMS apps or the validity of the developer could not be confirmed.
   
   This usually means the OpenMS software lands in quarantine after installation of the `.dmg`.
   Since macOS Catalina (maybe also Mojave) all apps and executables have to be officially notarized by Apple but we
   currently do not have the resources for a streamlined notarization workflow.

   To have a streamlined experience without blocking popups, it is recommended to remove the quarantine flag manually,
   using the following steps:

   Open the Terminal.app and type the following (replace the first line with the actual installation directory):
   ```bash
   cd /Applications/OpenMS-<version>
   sudo xattr -r -d com.apple.quarantine *
   ```
   
2. Bug with running Java based thirdparty tools like {term}`MSGFPlusAdapter` and {term}`LuciphorAdapter` from within **TOPPAS.app**

   If you face issues while running Java based thirdparty tools from within {term}`TOPPAS.app <TOPPAS>`, run the {term}`TOPPAS.app <TOPPAS>`
   from within the Terminal.app (e.g. with the `open` command) to get access to the path where Java is located.
   Java is usually present in the `PATH` of the terminal. Advanced users can set this path in the `Info.plist` of/inside
   the TOPPAS.app.
