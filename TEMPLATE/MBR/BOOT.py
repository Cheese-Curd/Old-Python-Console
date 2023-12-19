import os

# Run main file in drive
path = "" # Path to Script
script = "MAIN"  # Script name
os.chdir(f"../STORAGE/{path}/") # Go to path
os.system(f"py {script}.py")   # Go to script