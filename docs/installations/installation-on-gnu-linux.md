GNU/Linux
=========================

## Install via Conda

You can use conda to install the OpenMS library and tools without user interface. Depending on the conda channel, you can
obtain release versions (`bioconda` channel) and nightly versions (`openms` channel).

1. Follow the instructions to [install conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html).

2. Add channels for dependencies:
   ```bash
    conda config --add channels defaults
    conda config --add channels bioconda
    conda config --add channels conda-forge
   ```
3. Install any of the following packages related to OpenMS

::::{tab-set}

:::{tab-item} openms
:sync: openms

openms contains all OpenMS C++ command-line tools.
:::

:::{tab-item} libopenms
:sync: libopenms

libopenms is the C++ library required for the OpenMS C++ Tools to work. This is also an auto-installed dependency of openms.
:::

:::{tab-item} pyopenms
:sync: pyopenms

pyopenms is the python package that allows to use algorithms from libopenms in Python.
:::

:::{tab-item} openms-thirdparty
:sync: openms-thirdparty

openms-thirdparty are external tools that are wrapped in OpenMS with adapters. This is required to use the adapters in
the openms package.
:::

::::

via `bioconda` for release versions


::::{tab-set}

:::{tab-item} openms
:sync: openms

```{code-block} bash 
conda install openms
```
:::

:::{tab-item} libopenms
:sync: libopenms

```{code-block} bash
conda install libopenms
```
:::

:::{tab-item} pyopenms
:sync: pyopenms

```{code-block} bash
conda install pyopenms
```
:::

:::{tab-item} openms-thirdparty
:sync: openms-thirdparty

```{code-block} bash
conda install openms-thirdparty
```
:::

::::

or our own `openms` channel for nightly snapshots (which are build based on the same bioconda dependencies)

::::{tab-set}

:::{tab-item} openms
:sync: openms

```{code-block} bash 
conda install -c openms openms
```
:::

:::{tab-item} libopenms
:sync: libopenms

```{code-block} bash
conda install -c openms libopenms
```
:::

:::{tab-item} pyopenms
:sync: pyopenms

```{code-block} bash
conda install -c openms pyopenms
```
:::

:::{tab-item} openms-thirdparty
:sync: openms-thirdparty

```{code-block} bash
conda install -c openms  openms-thirdparty
```
:::

::::

## Install via package managers

Packaged versions of **OpenMS** are provided for Fedora, OpenSUSE, Debian, and Ubuntu. You can find them to download
[here](https://pkgs.org/download/openms). For other GNU/Linux distributions or to obtain the most recent version of the
library, installation should be done via building from the source code.

```{important}
These packages are not directly maintained by the OpenMS team and they can not be guaranteed to have the
same behaviour as when building it from source code. Also, their availability and version is subject to change and
support might be limited (due to unforeseen or untested behaviour). It is suggested not to install them parallel to our
Debian package.
```

```{note}
Some thirdparty software used via adapter tools in OpenMS might also require an installed JavaVM.
```

## Install via the provided Debian package

For Debian-based Linux users, it is suggested to  use the [deb-package](https://abibuilder.cs.uni-tuebingen.de/archive/openms/OpenMSInstaller/release/latest/) provided. It is most easily installed with **[gdebi](https://launchpad.net/gdebi)**
which automatically resolves the dependencies available in the PPA Repositories.

```bash
sudo apt-get install gdebi
sudo gdebi /PATH/TO/OpenMS.deb
```
If you encounter errors with unavailable packages, troubleshoot using the following steps.

1. Qt5 (or one of its packages, e.g. `qt5xbase`) is missing.
   It might be because your Debian is too old to have a recent enough version in its official repositories. It is
   suggested to use the same packages that are used while building (make sure to adapt the Qt version and your
   Debian/Ubuntu version, here Xenial):
   ```bash
   sudo add-apt-repository ppa:beineri/opt-qt59-xenial
   sudo apt-get update
   ```
   Run the installation again.

2. ICU with its `libicu` is missing.
   You can find the missing version on [pkgs.org](https://pkgs.org) and install it with `gdebi`, too. You can have
   multiple versions of ICU installed.

3. Error while executing a tool
   To ensure the tool functionality, make sure you add the `OPENMS_DATA_PATH` variable to your environment as follow
   `export OPENMS_DATA_PATH=/usr/share/OpenMS`

4. Thirdparty installation of Qt5 in step 1
   Make sure you source the provided environment file using:
   `source /opt/qt59/bin/qt59-env.sh`

5. Adapters are not finding thirdparty applications
   Executables for thirdparty applications can be found in:
   `/usr/share/OpenMS/THIRDPARTY`
   Add the folders in your `PATH` for a convenient use of the adapters.

## Run via a (Bio)Container

Install a containerization software (e.g., [Docker](https://docs.docker.com/engine/install/) or [Singularity](https://sylabs.io/guides/3.0/user-guide/quick_start.html#quick-installation-steps))

Our container support is constantly updated. Docker images provided by us can be obtained via [ghcr.io](https://ghcr.io).

1. [openms-library](https://ghcr.io/openms/openms-library)
2. [openms-executables](https://ghcr.io/openms/openms-executables)

Docker images from our own continuous integration can be installed via the following commands:

```bash
docker pull ghcr.io/openms/openms-library
docker pull ghcr.io/openms/openms-executables
```

per default this results in the download of the latest nightly snapshot. Specify a release version (e.g.,
`docker pull ghcr.io/openms/openms-library:2.7.0` to receive a stable version.

Otherwise, the [BioContainers Registries](https://biocontainers.pro/registry) and the associated Galaxy
project provide native containers from our bioconda packages for both Docker and Singularity.

1. [BioContainers libopenms](https://biocontainers.pro/tools/libopenms)
2. [BioContainers openms](https://biocontainers.pro/tools/openms)
3. [BioContainers openms-thirdparty](https://biocontainers.pro/tools/openms-thirdparty)
4. [BioContainers pyOpenMS](https://biocontainers.pro/tools/pyopenms)

Images of the containers can be pulled via or one of the following commands:

::::{tab-set}

:::{tab-item} Docker

```{code-block} bash
docker pull quay.io/biocontainers/libopenms
docker pull quay.io/biocontainers/openms
docker pull quay.io/biocontainers/pyopenms
docker pull quay.io/biocontainers/openms-thirdparty
```

:::

:::{tab-item} Singularity

```{code-block} bash
docker pull https://depot.galaxyproject.org/singularity/libopenms
docker pull https://depot.galaxyproject.org/singularity/openms
docker pull https://depot.galaxyproject.org/singularity/pyopenms
docker pull https://depot.galaxyproject.org/singularity/openms-thirdparty
```

:::

::::

If Singularity images fail to download or run, try to use the Docker images as Singularity will automatically convert them.

Dockerfiles to build different kind of images (corresponding to build instructions, e.g. on ArchLinux) yourself can be found on
GitHub in our [OpenMS/dockerfiles](https://github.com/OpenMS/dockerfiles) repository.

## Build OpenMS from source

To build OpenMS from source, follow the build instructions for [Linux](https://abibuilder.informatik.uni-tuebingen.de/archive/openms/Documentation/release/latest/html/install_linux.html).
