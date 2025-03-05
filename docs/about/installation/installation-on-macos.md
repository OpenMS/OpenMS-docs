macOS
====================

```{include} installation-with-conda.md
:start-after: "% start-after"
```

## Install via macOS installer

To install OpenMS on macOS, run the following steps:

1. Download and install the macOS drag-and-drop installer from the [archive](https://abibuilder.cs.uni-tuebingen.de/archive/openms/OpenMSInstaller/release/latest/).
2. Double click on the downloaded file. It will start to open the `OpenMS-<version>-macOS.dmg` disk image file.

```{image} /_images/installations/macos/Warning-openMS-3.3.0-macOS-Silicon.pkg-Not-Opened.png
:alt: macOS warning message when opening OpenMS-<version>-macOS.pkg  
:width: 500px  
```

3. Bypassing Gatekeeper to Install OpenMS on macOS

```{image} /_images/installations/macos/Bypassing-Gatekeeper-to-Install-OpenMS-on-macOS.png
:alt: Bypassing Gatekeeper on macOS  
:width: 500px  
```

4. Install OpenMS 

```{image} /_images/installations/macos/Installation-successful-message.png
:alt: OpenMS installation started on macOS  
:width: 500px  
```

5. Agree to the license agreements.

```{image} /_images/installations/macos/license-agreements.png
:alt: License agreement
:width: 500px
```

6. Installation Confirmation

```{image} /_images/installations/macos/Installation-successful-message.png
:alt: OpenMS installation successful  
:width: 500px  
```

To use {term}`TOPP` as regular app in the shell, add the following lines to the `~/.profile` file.

:::{warning} Known Installer Issues

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

   ```bash
   export OPENMS_TOPP_PATH=<OpenMS-PATH>
   source ${OPENMS_TOPP_PATH}/.TOPP_bash_profile
   ```

   Make sure `<OpenMS-PATH>` points to the folder where OpenMS is installed locally (e.g., `/Applications/OpenMS-<version>`)

:::

```{include} run-in-container.md
:start-after: "% start-after"
```

## Build OpenMS from source

To build OpenMS from source, follow the build instructions for [macOS](https://abibuilder.cs.uni-tuebingen.de/archive/openms/Documentation/release/latest/html/install_mac.html).



