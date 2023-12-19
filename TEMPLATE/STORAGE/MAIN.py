# Get host imports to get BIOS imports
import os # Host OS
import sys as hostSys # Host System, BIOS System module is recommended to use instead of host's
hostSys.path.append('../../BIOS') # Go back to BIOS (If you make this go into deeper file paths, add more '../'s)
curDir = os.path.dirname(os.path.realpath(__file__)) # Return to file location
# Get BIOS imports
import DRAW as draw # BUIS Draw module
import SYSTEM as sys # BIOS System module
hostSys.path.append(curDir) # Return to directory

# Put Launch Code here
if __name__ == "__main__":
	sys.pause(0.5)
	sys.winsound.Beep(1000, 150)
	draw.text(f"Executed CMD.py inside of the drive 'TEMPLATE'", draw.COLOR.PURPLE)