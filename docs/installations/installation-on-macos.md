macOS
====================

## Install via macOS installer

To install OpenMS on macOS, run the following steps:

1. Download and install the macOS drag-and-drop installer from the [archive](https://abibuilder.informatik.uni-tuebingen.de/archive/openms/OpenMSInstaller/release/latest/).
2. Double click on the dowloaded file. It will start to open the download `openms-<version>-macos.dmg` file

<img src="https://raw.githubusercontent.com/OpenMS/OpenMS-docs/staging/docs/images/installations/macos/opening-openms%3Cversion%3E-macos.png" alt="Verifying OpenMS-<version>-macOS.dmg" width="500" float: left/>

3. Verify the download.

<img src="https://raw.githubusercontent.com/OpenMS/OpenMS-docs/staging/docs/images/installations/macos/verifying-OpenMS%3Cversion%3E.png" alt="Verifying OpenMS-<version>-macOS.dmg" width="500" float: left/>

4. Agree the license agreements.

<img src="https://raw.githubusercontent.com/OpenMS/OpenMS-docs/staging/docs/images/installations/macos/license-agreements.png" alt="License Agreement" width="500" float: left/>

5. Drag openms to applications.

<img src="https://raw.githubusercontent.com/OpenMS/OpenMS-docs/staging/docs/images/installations/macos/move-openms-to-applications.png" alt="License Agreement" width="500" float: left/>

6. It will start copying to applications.

<img src="https://raw.githubusercontent.com/OpenMS/OpenMS-docs/staging/docs/images/installations/macos/preparing-to-copy-to-applications.png" alt="Preparing to Copy to Applications" width="500" float: left/>

<img src="https://raw.githubusercontent.com/OpenMS/OpenMS-docs/staging/docs/images/installations/macos/copying-to-applications.png" alt="Copying to Applications" width="500" float: left/>

To use {term}`TOPP` as regular app in the shell, add the following lines to the `~/.profile` file.

```bash
export OPENMS_TOPP_PATH=<OpenMS-PATH>
source ${OPENMS_TOPP_PATH}/.TOPP_bash_profile
```

Make sure `<OpenMS-PATH>` points to the folder where OpenMS is installed locally (e.g., `/Applications/OpenMS-<version>`)

## Install via Conda or Bioconda

Follow the <a href="installation-on-gnu-linux.html#install-via-conda">instructions</a> .

## Known Issues

1. OpenMS software landing in quarantine since macOS Catalina after installation of the `.dmg`.

   Since macOS Catalina (maybe also Mojave) notarized apps and executables are mandatory.

   ```{important}
   Although there is a lot of effort in signing and notarizing everything, it seems like openms software
   still lands in quarantine on the above mentioned systems, after installation of the DMG (when downloading it from a
   browser).
   ```

   To have a streamlined experience without blocking popups, it is recommended to remove the quarantine flag manually,
   using the following steps:

   Open the Terminal.app and type the following (replace the first line with the actual installation directory):
   ```bash
   cd /Applications/OpenMS-<version>
   sudo xattr -r -d com.apple.quarantine *
   ```
2. Bug with running Java based thirdparty tools like {term}`MSGFPlusAdapter` and {term}`LuciphorAdapter` from within **TOPPAS.app**

   If you face issues while running Java based thirdparty tools from within {term}`TOPPAS.app`, run the {term}`TOPPAS.app`
   from within the Terminal.app (e.g. with the `open` command) to get access to the path where Java is located.
   Java is usually present in the `PATH` of the terminal. Advanced users can set this path in the `Info.plist` of/inside
   the TOPPAS.app.
