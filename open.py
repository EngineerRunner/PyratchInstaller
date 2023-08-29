import os
os.system("alias python=python3")
os.system("echo 'alias python=python3' >> ~/.bash_profile")
os.system("echo 'alias python=python3' >> ~/.zshrc")
print("Done! Now go to https://localhost:5000 to use Pyratch!")
os.system("cd " + ("~/Pyratch" or "/Pyratch") + " && python interface.py")
