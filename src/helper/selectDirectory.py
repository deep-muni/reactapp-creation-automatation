import os
from .clear import clear


def selectDirectory(pwd):
    os.chdir(pwd)

    while True:
        while True:
            clear()
            print("Current Directory: " + pwd + "\n")

            i = 0
            list_of_dir = os.listdir()
            for directory in list_of_dir:
                print(i + 1, directory)
                i += 1

            print("\nb: Back | s: Select\n")

            print("Select:")
            num = input()

            clear()

            if num == "b":
                os.chdir("../")
                pwd = os.getcwd()
            elif num == "s":
                break
            elif 0 < int(num) < i + 1:
                pwd = pwd + "\\" + list_of_dir[int(num) - 1]
                os.chdir(pwd)
            else:
                continue

        print("Selected Directory: " + pwd)
        print("\nContinue?: (y/n)")
        ch = input()

        clear()

        if ch == "y":
            return pwd
        else:
            continue
