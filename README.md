Installing Pyratch: A Technical Walkthrough

Welcome to the installation guide for Pyratch, a lightweight Scratch reader developed by AH (@GenericProgrammer1234 on GitHub). This guide will take you through the step-by-step process of installing Pyratch using the provided code snippet. Pyratch is built using Flask and ScratchAttach, and this guide will ensure you have it up and running smoothly.

Installation Procedure

Launching the Terminal:
To begin the installation, open a terminal window on your operating system. The terminal will serve as the interface for running the installation script and executing commands.

Repository Cloning:
Determine whether you want to proceed with a system-wide installation or a user-specific installation. The installation process will differ depending on your choice.

a. System-wide Installation:
If you intend to perform a system-wide installation, input 1 and hit Enter:

1


b. User Installation:
For a user-specific installation, input 2 and hit Enter:

2


Version Selection:
You have the option to choose between installing the latest stable version or the latest development version (which is not recommended for general users).

a. Stable Version:
Input 1 for the stable version and hit Enter:

1


b. Development Version:
If you want the development version (not recommended for most users), input 2 and hit Enter:

2


Installation Execution:
Depending on the selections you made in steps 2 and 3, the appropriate installation command will be executed.

a. System-wide install with stable version (option 1) will execute:

cd / && git clone https://github.com/GenericProgrammer1234/Pyratch.git -b stable


b. System-wide install with development version (option 2) will execute:

cd / && git clone https://github.com/GenericProgrammer1234/Pyratch.git -b dev


c. User install with stable version (option 1) will execute:

cd ~ && git clone https://github.com/GenericProgrammer1234/Pyratch.git -b stable


d. User install with development version (option 2) will execute:

cd ~ && git clone https://github.com/GenericProgrammer1234/Pyratch.git -b dev


Dependency Download:
Once the repository is successfully cloned, the installer will proceed to download the necessary dependencies using this command:

python3 -m pip install scratchattach flask


Installation Completion:
After the dependencies are installed, the Pyratch installation process is considered complete.

Running Pyratch:
Depending on the type of installation you chose, navigate to the appropriate directory:

a. For system-wide installation:

cd /Pyratch


b. For user installation:

cd ~/Pyratch


Run Pyratch using the suitable command for your system.

Congratulations! You have successfully installed Pyratch. You are now equipped to utilize Pyratch for Scratch attachment and Flask integration.

For any additional information or support, feel free to visit the Pyratch GitHub repository. Happy coding! 🚀