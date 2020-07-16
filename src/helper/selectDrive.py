import win32api
from .clear import clear

def selectDrive():
	drives = win32api.GetLogicalDriveStrings()
	drives = drives.split('\000')[:-1]

	while True:
		print("Select the drive:\n")

		i = 1

		for drive in drives:
			print(str(i) + ". " + drive)
			i += 1

		choice = input("\nChoice:\n")

		try:
			if int(choice) > 0 and int(choice) <= len(drives):
				return drives[int(choice) - 1]
			else:
				clear()
				print("Invalid Input (Try Again)\n")
		except:
			clear()
			print("Invalid Input (Try Again)\n")

