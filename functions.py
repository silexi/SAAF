# Author: Bartu KILIÇ
# Contact: kilicbartu@gmail.com
# GitHub: https://github.com/silexi
# Website: https://bartukilic.com

import os
from art import tprint

def prettyStart():
    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 34)
    tprint(" SAAF")
    print(" System Analysis and Forensic Tool")
    print("       Copyright by silexi\n")
    print("=" * 34)
    
    while True:
        print("\nTools:\n1) System Information Gather\n2) Forensic Dumper (via txt)\n3) IOC Search\n4) Special Scanner\n")
        startForensic = input("> Select an option: ").strip()
        if startForensic.isdigit() and startForensic in ["1", "2", "3", "4"]:
            return startForensic  # Seçilen opsiyonu döndürüyoruz
        else:
            print("Invalid option. Please select a valid number.")
            continue

def checkFolder():
    print("\n> Checking output folder...")
    path = os.path.join(os.getcwd(), "forensec")
    if not os.path.exists(path):
        os.makedirs(path)
        print(">> The forensec directory is created!")
    else:
        print(">> The forensec directory already exists.")
    os.chdir(path)

def writeToFile(filePath, fileContent):
    overwrite = input("\nWARNING! The system information file already exists in the folder. \nIt will be OVERWRITTEN, do you approve? (Y/n): ").strip().lower()
    if overwrite == 'y':
        print(f"\nWriting the {filePath} file...")
        with open(filePath, "w") as f:
            f.write(fileContent)
    else:
        print("Operation cancelled. The file was not overwritten.")

def forensicDumper():
    print("Forensic Dumper is not yet implemented.")
    # Buraya adli döküm işlemleri eklenebilir

def iocSearch():
    print("IOC Search is not yet implemented.")
    # Buraya IOC arama işlemleri eklenebilir

def specialScanner():
    print("Special Scanner is not yet implemented.")
    # Buraya özel tarama işlemleri eklenebilir
