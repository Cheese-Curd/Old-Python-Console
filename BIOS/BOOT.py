import math
import SYSTEM as system
import DRAW as draw
import json

biosSet = json.load(open('BIOS/BIOS.json'))

def PostTest():
	global biosSet

	sysInfo = system.getSystemInfo()
	system.beep(900, 200)

	draw.text("EBIOS(C)2023 Eliana")
	draw.text(f"ELIANA BIOS REVISION {biosSet['revision']} VERSION {biosSet['version']}")
	draw.text(f"CPU : {sysInfo[1]} @ {sysInfo[2] / 1000}GHz")
	draw.text(f"Speed : {sysInfo[2] / 1000} GHz    Count: {sysInfo[4]}")
	draw.blank(1)

	system.pause(2)
	draw.text("Initializing USB Controllers ... ", end="")
	system.pause(1)
	draw.text("Done.")
	memTime = system.time.perf_counter()
	for mem in range(0, math.floor(sysInfo[0] / 1000000) + 1):
		draw.text(f"\rMemory: {mem}MB", end="")
		system.pause(0.0001)
	system.pause(0.2)
	draw.text(" OK")
	draw.text(f"Memory test took {math.floor(memTime / 1000)} Seconds")
	system.pause(0.5)
	system.wipeScreen()

def transferControl():
	global biosSet

	system.changeDir(f"{biosSet['bootOrder'][0]}/MBR") # Change DIR to top boot order MBR
	system.os.system("python3 BOOT.py") # Run Boot Script

if __name__ == "__main__":
	if system.platform.system() == "Windows":
		system.os.system('color 0f')
	else:
		# This is weird bruh
		system.os.system('tput setaf 0')
	if biosSet["doPOST"]:
		PostTest()
	else:
		system.pause(1)
	system.beep(900, 200)
	transferControl()