# Author: Bartu KILIÇ
# Contact: kilicbartu@gmail.com
# GitHub: https://github.com/silexi
# Website: https://bartukilic.com

from systeminformations import *
from functions import *

def main():
    choice = prettyStart()
    if choice == "1":
        startWindowsForensic()
    elif choice == "2":
        forensicDumper()
    elif choice == "3":
        iocSearch()
    elif choice == "4":
        specialScanner()

def startWindowsForensic():
    checkFolder()
    getSystemInformations()

if __name__ == "__main__":
    main()
