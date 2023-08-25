import os
print("Pyratch Installer")
print("Made by AH (@GenericProgrammer1234 on GitHub)")
print("Do you want to do a system-wide install or user install?")
print("1. System-wide Install")
print("2. User Install")
t = int(input())
if t == 1:
	os.system("cd / && git clone https://github.com/GenericProgrammer1234/Pyratch.git")
elif t == 2:
	os.system("cd ~ && git clone https://github.com/GenericProgrammer1234/Pyratch.git")
print("Downloading dependicies")
os.system("python3 -m pip install scratchattach flask")
print("Done! Go to " + ("~/Pyratch" if t == 2 else "/Pyratch") + " and then run it!")
