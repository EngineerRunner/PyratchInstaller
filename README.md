# Pyratch Installer

An installer for Pyratch.

# Usage

It is recommended to add this to your bash profile or zsh profile before you try installing Pyratch: `alias python=python3`


1. Launch the terminal, download this repo through `git clone https://github.com/GenericProgrammer1234/PyratchInstaller` then navigate into PyratchInstaller and type `python install.py` to launch the installer, Note that you have to use `python3 wininstall.py` for Windows.

2. It will prompt you for your type of installation, enter `1` for system-wide installation (requires root or admin) or enter `2` for user installation

3. It will ask you for which version, enter `1` for the latest stable version or enter `2` for the latest development version (not recommended but has the latest of latest features even if there are bugs and is recommended for contributors)

4. After the dependencies are installed, navigate to the folder where Pyratch was installed and type `python interface.py` to run, and if you're too lazy to navigate just use the opener in the Installer folder with `python open.py`, it will ask you for your type of installation, enter `1` for system-wide installation or enter `2` for user installation, make sure to tell the installation that you have and want to open, and then go ahead and go to `https://localhost:5000` to use Pyratch.

5. To update navigate to the installer and then run `python updater.py`,
it will ask you for your type of installation, enter `1` for system-wide installation or enter `2` for user installation, make sure to tell the installation that you have and want to update, and then go ahead and go to `https://localhost:5000` to use Pyratch, but this time with the latest futures.

   (idea of the opener was so stupid, also this README file is so repetitive and stupid)
