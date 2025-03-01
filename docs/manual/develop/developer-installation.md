# Developer Installation Instructions

## Overview

This document provides detailed instructions for developers to build OpenMS from source.

## Prerequisites

Before you begin, ensure you have the following prerequisites installed:

- **CMake**: Version 3.10 or higher. You can download it from [CMake's official website](https://cmake.org/download/).
- **Boost Libraries**: Ensure you have the latest version. Installation instructions can be found on the [Boost website](https://www.boost.org/).
- **Qt**: Version 5.9 or higher. Download it from the [Qt website](https://www.qt.io/download).
- **Python**: Version 3.6 or higher. You can download it from [Python's official website](https://www.python.org/downloads/).

## Building from Source

Follow these steps to build OpenMS from source:

1. **Clone the Repository**:
   Open a terminal and run the following commands to clone the OpenMS repository:
   ```bash
   git clone https://github.com/OpenMS/OpenMS.git
   cd OpenMS
   ```

2. **Create a Build Directory**:
   Create a separate directory for building the project to keep the source directory clean:
   ```bash
   mkdir build
   cd build
   ```

3. **Configure the Build**:
   Use CMake to configure the build. This step checks for all necessary dependencies:
   ```bash
   cmake ..
   ```

4. **Compile the Project**:
   Compile the project using the `make` command. This process may take some time depending on your system:
   ```bash
   make
   ```

5. **Run Tests** (optional):
   It's recommended to run tests to ensure everything is working correctly:
   ```bash
   make test
   ```

6. **Install OpenMS**:
   Finally, install OpenMS on your system. You may need superuser privileges for this step:
   ```bash
   sudo make install
   ```

## Troubleshooting

- **Dependency Issues**: If you encounter issues with dependencies, ensure all prerequisites are correctly installed and accessible in your PATH. You can verify this by running `cmake ..` and checking for any error messages.
- **Build Errors**: For detailed error messages, check the build logs located in the `build` directory. This can help diagnose issues related to missing files or incorrect configurations.
- **Further Assistance**: If you continue to experience issues, consider reaching out to the OpenMS community via their [GitHub Issues page](https://github.com/OpenMS/OpenMS/issues) for support. 