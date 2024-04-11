import platform
import psutil
import cpuinfo
import time
import os
if platform.system() == "Windows":
	import winsound

def beep(frequency, duration):
	if platform.system() == 'Windows':
		winsound.Beep(frequency, duration)

def wipeScreen():
	if platform.system() == "Windows":
		os.system('cls')
	else:
		os.system('clear')

def pause(length:float):
	time.sleep(length)

def getSystemInfo():
	uname_results = platform.uname()
	info = []
	info.append(psutil.virtual_memory().total) # 0
	info.append(uname_results.processor) # 1
	info.append(psutil.cpu_freq().max) # 2
	info.append(psutil.cpu_times()) # 3
	info.append(psutil.cpu_count()) # 4

	return info

def changeDir(path="."):
	os.chdir(path)
	return os.getcwd()