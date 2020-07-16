import os
from helper.clear import clear
from helper.selectDirectory import selectDirectory
from helper.selectDrive import selectDrive
from helper.integrateGit import integrateGit
from helper.askAppName import askAppName

# clear()

# drive = selectDrive()
# pwd = selectDirectory(drive)

# os.chdir(pwd)

# print("Current Directory:\n",pwd,"\n")

temp = "E:\\Project\\Learning\\React"

os.chdir(temp)

result = integrateGit()
clear()

if(result['status'] == True):
	# name = getAppName(result['url'])
	pass
else:
	name = askAppName()
	pass

# clear()
print("Initiating React Application")