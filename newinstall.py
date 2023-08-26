import os
import platform
import subprocess

class PyratchInstaller:
	def __init__(self):
		print("Pyratch Installer")
		print("Made by AH (@GenericProgrammer1234 on GitHub)")
		print("Do you want to do a system-wide install or user install?")
		print("1. System-wide Install")
		print("2. User Install")
		self.t = int(input())
		self.branch = self.get_branch()

	def get_branch(self):
		print("Do you want to go with the latest stable version or install the latest development version (NOT RECOMMENDED)")
		print("1. Stable")
		print("2. Dev")
		x = int(input())
		return "stable" if x == 1 else "dev"

	def install(self):
		{
			1: self.system_wide_install,
			2: self.user_install
		}[self.t]()

	def system_wide_install(self):
			command = f"git clone https://github.com/GenericProgrammer1234/Pyratch.git -b {self.branch}"
			subprocess.run(command, shell=True, check=True, cwd="/")

	def user_install(self):
		user = os.getlogin()
		git_url = f"https://github.com/GenericProgrammer1234/Pyratch.git -b {self.branch}"
		
		if platform.system() == "Windows":
			os.system(f"cd C:\\Users\\{user} && git clone {git_url}")
		else:
			os.system(f"cd ~ && git clone {git_url}")

	def download_dependencies(self):
		print("Downloading dependencies")
		os.system("python3 -m pip install scratchattach flask")

	def run(self):
		self.install()
		self.download_dependencies()
	
		if self.t == 2:
			if platform.system() == "Windows":
				print("Done! Go to C:\\Users\\<username>\\Pyratch and then run it!")
			else:
				print("Done! Go to ~/Pyratch and then run it!")
		else:
			if platform.system() == "Windows":
				print("Done! Go to C:\\Pyratch and then run it!")
			else:
				print("Done! Go to /Pyratch and then run it!")

installer = PyratchInstaller()
installer.run()
