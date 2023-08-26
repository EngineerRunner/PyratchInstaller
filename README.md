# Pyratch Installer

This guide provides step-by-step instructions for installing Pyratch using the provided code snippet. Pyratch is a light-weight Scratch reader developed by AH (@GenericProgrammer1234 on GitHub) made using Flask and ScratchAttach.

## Installation Steps

1. **Open a Terminal:**
    Open a terminal window on your system. This will be used to run the installation script and commands.

2. **Clone the Repository:**
    Decide whether you want to perform a system-wide or user-specific installation. The installation process will differ based on your choice.

    a. **System-wide Install:**
        To perform a system-wide installation, enter `1` and press Enter:
        ```
        1
        ```

    b. **User Install:**
        To perform a user-specific installation, enter `2` and press Enter:
        ```
        2
        ```

3. **Select Version:**
    Choose between installing the latest stable version or the latest development version (not recommended for most users).

    a. **Stable Version:**
        Enter `1` for the stable version and press Enter:
        ```
        1
        ```

    b. **Development Version:**
        Enter `2` for the development version (not recommended for most users) and press Enter:
        ```
        2
        ```

4. **Installation Process:**
    Based on your selections in steps 2 and 3, the appropriate installation command will be executed.

    a. If you chose a system-wide install and stable version (option 1), the following command will be executed:
        ```
        cd / && git clone https://github.com/GenericProgrammer1234/Pyratch.git -b stable
        ```

    b. If you chose a system-wide install and development version (option 2), the following command will be executed:
        ```
        cd / && git clone https://github.com/GenericProgrammer1234/Pyratch.git -b dev
        ```

    c. If you chose a user install and stable version (option 1), the following command will be executed:
        ```
        cd ~ && git clone https://github.com/GenericProgrammer1234/Pyratch.git -b stable
        ```

    d. If you chose a user install and development version (option 2), the following command will be executed:
        ```
        cd ~ && git clone https://github.com/GenericProgrammer1234/Pyratch.git -b dev
        ```

5. **Download Dependencies:**
    Once the repository is cloned, the installer will download the required dependencies using the following command:
    ```
    python3 -m pip install scratchattach flask
    ```

6. **Installation Complete:**
    Once the dependencies are installed, the Pyratch installation is complete.

7. **Run Pyratch:**
    Depending on your installation type, navigate to the appropriate directory:

    a. For system-wide install:
        ```
        cd /Pyratch
        ```

    b. For user install:
        ```
        cd ~/Pyratch
        ```

    Run Pyratch using the appropriate command for your system.

Congratulations! You have successfully installed Pyratch. You can now use Pyratch for Scratch attachment and Flask integration.

For more information or support, you can visit the [Pyratch GitHub repository](https://github.com/GenericProgrammer1234/Pyratch).