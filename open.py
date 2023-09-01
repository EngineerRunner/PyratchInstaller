import os
os.system("alias python=python3")
os.system("echo 'alias python=python3' >> ~/.bash_profile")
os.system("echo 'alias python=python3' >> ~/.zshrc")
print("did you choose a systemwide installation or a user installation?")
print("1. System-wide Install")
print("2. User Install")
t = int(input())
os.system("cd " + ("~/Pyratch" if t == 2 else "/Pyratch") + " && python interface.py")

print("Done! Now go to https://localhost:5000 to use Pyratch!")