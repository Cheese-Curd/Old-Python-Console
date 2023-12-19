# Get BIOS imports
import os
import sys as hostSys
hostSys.path.append('../../../BIOS')
curDir = os.path.dirname(os.path.realpath(__file__)) # Return to file location
import DRAW as draw
import SYSTEM as sys
hostSys.path.append(curDir) # Return to directory
import json
osInfo = json.load(open('osinfo.json'))
curDir = os.chdir("../") # Go back a directory to get to main storage
hostSys.path.append(curDir)

import math

takingInput = True
curDrive = "A"
curPath = ""
safeExit = False

draw.text(f"{osInfo["shellName"]}2023", draw.COLOR.PURPLE)
draw.blank(1)
draw.text('Type "HELP" for a list of commands.', draw.COLOR.PURPLE)

def getDir(drive, path):
	global curDir
	if osInfo["debug"]:
		draw.text(f"Directory of {drive}:{path}/.")
		# type = "dir"
		# extention = ""
		# draw.text(f".              <{type}>", end="")
		draw.text(curDir, draw.COLOR.PURPLE)
		draw.text(os.listdir(curDir), draw.COLOR.PURPLE)
	else:
		draw.text("Illegal access of command: No permission", draw.COLOR.RED)

def setDir(path):
	global curPath
	global curDir
	if osInfo["debug"]:
		curPath = path
	else:
		draw.text("Illegal access of command: No permission", draw.COLOR.RED)

def setDrive(letter):
	global curDrive
	if osInfo["debug"]:
		curDrive = letter
	else:
		draw.text("Illegal access of command: No permission", draw.COLOR.RED)

commands = {}
maxCMDLength = 0
variables = {}
maxVARLength = 0

def register(name:str, description:str, overrideColor=draw.COLOR.BLUE, command=True):
	global commands
	global maxCMDLength
	global variables
	global maxVARLength

	item = {}
	item["name"] = name
	item["description"] = description
	item["overrideColor"] = overrideColor

	if command == True:
		commands[len(commands)] = item
		if len(name) > maxCMDLength:
			maxCMDLength = len(name)
	else:
		variables[len(variables)] = item
		if len(name) > maxVARLength:
			maxVARLength = len(name)

# Register commands to display later
register("dir", "Directory view", draw.COLOR.RED)
register("cd", "Displays/changes the current directory", draw.COLOR.RED)
register("chdir", "Displays/changes the current directory", draw.COLOR.RED)
register("cls", "Clear screen")
register("clear", "Clear screen")
register("set", "Change variables")
register("ver", "View the reported OS version")
register("version", "View the reported OS version")
register("exit", "Exits from the shell")
# Register Variables that can be changed
register("takinginput", f"Vital for system running. Current value: {draw.COLOR.BLUE}{takingInput}", command=False)

def displayRegister(command=True): # Made this first try, I love existing
	global commands
	global maxCMDLength
	global variables
	global maxVARLength

	if command:
		for i in commands.keys():
			cmd = commands[i]
			draw.text("<", end="")
			draw.text(f"{draw.OTHER.B}{cmd["name"].upper()}", cmd["overrideColor"], end="")
			draw.text(f"{" " * (maxCMDLength - len(cmd["name"]) + 4)}> {cmd["description"]}.")
	else:
		for i in variables.keys():
			var = variables[i]
			draw.text("<", end="")
			draw.text(f"{draw.OTHER.B}{var["name"].upper()}", var["overrideColor"], end="")
			draw.text(f"{" " * (maxVARLength - len(var["name"]) + 4)}> {var["description"]}.")

def shutdown(reason:str=None):
	global takingInput

	takingInput = False
	sys.wipeScreen()
	os.system('color 0f')
	draw.text("SHUTTING DOWN", end="")
	if reason is not None:
		draw.text(f": {reason.upper()}")
	sys.time.sleep(1.9)
	sys.winsound.Beep(500, 100)
	sys.wipeScreen()
	exit()

def errScreen(code:str, desc:str):
	sys.wipeScreen()
	os.system('color 1f')
	draw.text(f"ERROR: {code}{" " * ((len(desc) - len(code)) + 1)}")
	draw.text(f'      "{desc}"')
	sys.winsound.Beep(500, 1500)
	shutdown("crash")

sysInfo = sys.getSystemInfo()

while takingInput:
	try:
		cmd = input(f"{curDrive.upper()}:{curPath.upper()}/>")  # Get command and arguments
	except KeyboardInterrupt:
		takingInput = False
		break
	args = cmd.split(" ")  									# Split the command and different arguments
	cmd = cmd.lower()  										# Convert to lowercase
	cmd = args[0] 											# Make sure it only checks the command, not the arguments
	del args[0]  											# Remove command from arguments
	if args == []:  										# Make sure args isn't nothing
		args.append("")  									# If it is, make it an empty string

	match cmd:
		case "help":
			displayRegister()
		case "dir":
			getDir(curDrive.upper(), curPath.upper())
		case "cd":
			if args[0] != "":
				setDir(args[0])
			else:
				draw.text(f"{curDrive}:{curPath}/")
				draw.blank(1)
		case "chdir":
			if args[0] != "":
				setDir(args[0])
			else:
				draw.text(f"{curDrive}:{curPath}/")
				draw.blank(1)
		case "cls":
			sys.wipeScreen()
		case "clear":
			sys.wipeScreen()
		case "exit":
			safeExit = True
			shutdown()
		case "ver":
			draw.text(f"Reported OS version: {osInfo["shellName"]}(C) version {osInfo["shellVer"]}.")
		case "version":
			draw.text(f"Reported OS version: {osInfo["shellName"]}(C) version {osInfo["shellVer"]}.")
		case "set":
			if args[0] == "":
				displayRegister(False)
			elif args[0].lower() == "takinginput":
				if args[1].lower() == "true":
					takingInput = True
				elif args[1].lower() == "false":
					takingInput = False
			else:
				draw.text("Variable not defined.")
				draw.blank(2)
		case "mem":
			draw.text(f"Memory: {math.floor(sysInfo[0] / 1000000)}MB")
		case "":
			draw.blank(1)
		case _:
			draw.text(f"Illegal command: {cmd}.", draw.COLOR.RED)

if not safeExit:
	errScreen("0", "MANUAL_FORCEFUL_EXIT")