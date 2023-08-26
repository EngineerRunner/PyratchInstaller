# Pyratch Installer

An installer for Pyratch.

# Usuage

It is recommended to add this to your bash profile or zsh profile before you try installing Pyratch: `alias python=python3`

Note that this installer only works for Unix based devices, and won't work on Windows. You'll need to install the GitHub repo via [one of the other two methods mentioned here](https://github.com/GenericProgrammer1234/Pyratch).

1. Launch the terminal, download this repo through `git clone https://www.github.com/GenericProgrammer1234/PyratchInstaller` then navigate into PyratchInstaller and type `python install.py` to launch the installer

2. It will prompt you for your type of installation, enter `1` for system-wide installation (requires root or admin) or enter `2` for user installation

3. It will ask you for which version, enter `1` for the latest stable version or enter `2` for the latest development version (not recommended but has the latest of latest features even if there are bugs and is recommended for contributors)

4. After the dependencies are installed, navigate to the folder where Pyratch was installed and type `python interface.py` to run
