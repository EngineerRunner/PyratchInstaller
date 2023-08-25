import os
print("Pyratch Installer")
print("Made by AH (@GenericProgrammer1234 on GitHub)")
print("Do you want to do a system-wide install or user install?")
print("1. System-wide Install")
print("2. User Install")
t = int(input())
print("Do you want to go with the latest stable version or install the latest development version (NOT RECOMMENDED)")
print("1. Stable")
print("2. Dev")
x = int(input())
branch = "stabe" if x == 1 else "dev"
if t == 1:
	os.system(f"cd / && git clone https://github.com/GenericProgrammer1234/Pyratch.git -b {branch}")
elif t == 2:
	os.system(f"cd ~ && git clone https://github.com/GenericProgrammer1234/Pyratch.git -b {branch}")
print("Downloading dependicies")
os.system("python3 -m pip install scratchattach flask")
print("Done! Go to " + ("~/Pyratch" if t == 2 else "/Pyratch") + " and then run it!")
