import os
os.system("DOSKEY python=python3")
print("Pyratch Installer")
print("Made by AH (@GenericProgrammer1234 on GitHub)")
print("Do you want to open a system-wide install or user install?")
print("1. System-wide Install")
print("2. User Install")
t = int(input())
print("Running Pyratch")
print("Done! Now go to localhost:5000 to use Pyratch!")
os.system("cd " + ("C:\\Pyratch" if t == 2 else "%USERPROFILE\\Pyratch") + " && python install.py")

