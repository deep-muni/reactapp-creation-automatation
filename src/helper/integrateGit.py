import os
from .clear import clear
import validators

def validate(url):
	if not validators.url(url):
		return False
	return validators.url(url)

def integrateGit():

	choice = input("Do you want to integrate Git Repository: (Y/y/N/n)\n")
	result = {'status': False, 'url': ''}

	while True:
		if choice == 'Y' or choice == 'y':

			url = input("\nPlease enter the URL: (quit to exit)\n")

			if url == "quit":
				exit()

			if validate(url):
				
				if os.system("git clone " + url) == 0:
					clear();
					result['status'] = True
					result['url'] = url
					return result
		
			else:
				clear()
				print("Invalid Input (Try Again)\n")
		elif choice == 'N' or choice == 'n':
			clear()
			return result
		else:
			clear()
			print("Invalid Input (Try Again)\n")