import os
os.system("alias python=python3")
os.system("echo 'alias python=python3' >> ~/.bash_profile")
os.system("echo 'alias python=python3' >> ~/.zshrc")
print("Pyratch Updater")

os.system("cd " + ("~/Pyratch" or "/Pyratch") + " && git pull")
print("you are successfully updated to the latest version of Pyratch")
os.system("cd " + ("~/Pyratch" or "/Pyratch") + " && python interface.py")
print("Now go to https://localhost:5000 to use the latest version with all the updates")
