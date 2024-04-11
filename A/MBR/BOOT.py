import os

# Run main file in drive
path = "SYSTEM" # Path to Script
script = "CMD"  # Script name
os.chdir(f"../STORAGE/{path}/") # Go to path
os.system(f"python3 {script}.py")   # Go to script