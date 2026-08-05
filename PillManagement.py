# Author: Akira Evans
# Project: Pill Management System
# Created: July 21, 2026
# Description: Handles medication tracking and pill management.

class PillManagement:

    def pillMenu(self):
        print(
            "\nPill Management\n"
            "---------------\n"
            "1. Add Pills\n"
            "2. Remove Pills\n"
            "3. See Pills"
        )


    def addPill(self, pill):
        try:
            with open("pills.txt", "r") as file:
                pills = file.read().splitlines()
        except FileNotFoundError:
            pills = []
            
        if pill not in pills:
            with open("pills.txt", "a") as file:
                file.write(pill + "\n")
        else:
            print("\nPill Already Exists! \n")


    def updatePill(self):
        print("Updated Pills: ")

        try:
            with open("pills.txt", "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("No Pills Found In File!")


    def removePill(self, pill):
        try:
            with open("pills.txt", "r") as file:
                pills = file.read().splitlines()
        except FileNotFoundError:
            pills = []

        if pill in pills:
            pills.remove(pill)

            with open("pills.txt", "w") as file:
                file.write("\n".join(pills))
        else:
            print("\nThis Pill Does Not Exist!")


    def seePills(self):
        try:
            with open("pills.txt", "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("File Does Not Exist!")
