import re
from .clear import clear

def askAppName():
	
	while True:
		name = input("Enter React application name: (0 to exit)\n")

		if name == '0':
			exit()

		if re.match(r"[a-z]+", name) is not None:
			if name[len(name) - 1].isalpha():
				clear()
				choice = input("Proceed with application name -> " + name + " ?: (Y/y/N/n)")
				if choice == 'Y' or choice == 'y':
					return name
		else:
			clear()
			print("Please choose alphanumeric lowecase name with - and _ allowed\n")