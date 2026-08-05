# Author: Akira Evans
# Project: Pill Management System
# Created: July 21, 2026
# Description: Handles medication tracking and pill management.

from PillManagement import PillManagement
from TimeManagement import TimeManagement

class PillTracker:

    def __init__(self):
        self.time = TimeManagement()
        self.pill = PillManagement()

    def menu(self): 
        while True:   
            print("Pill Tracking Program!")
            print("----------------------")
            print(
                "1. Pill Management\n"
                "2. Time Management\n"
                "3. Exit\n"
            )

            try:
                choice = int(input("Choose Number: "))
            except ValueError:
                print("Type A Number!")
                continue

            if choice == 1:
                
                self.pillMenu()

            elif choice == 2:
                self.timeMenu()

            elif choice == 3:
                print("\nSuccessfully Exited Program!")
                break

            else:
                print("Not A Menu Option!")


    def pillMenu(self):
            
        self.pill.pillMenu()

        try:
            choicePill = int(input("\nChoose Number: "))
        except ValueError:
            print("Type A Number!")
            return

        if choicePill == 1:
            pill = input("\nInsert Pill To Add: ").upper().strip()
            self.pill.addPill(pill)
            self.pill.updatePill()

        elif choicePill == 2:
            pill = input("\nInsert Pill To Remove: ").upper().strip()
            self.pill.removePill(pill)
            self.pill.updatePill()

        elif choicePill == 3:
            self.pill.seePills()

        else:
            print("Not A Menu Option!")


    def timeMenu(self):

        self.time.timeMenu()

        try:
            timeChoice = int(input("Choose Number: "))
        except ValueError:
            print("Type A Number!")
            return

        if timeChoice == 1:
            pill = input("\nInsert Pill To Log Time For: ").upper().strip()
            time = input("Insert Time Pill Was Taken (HHMM AM/PM): ")
            date = (input("Insert The Date Pill Taken (MMDDYYYY): "))

            self.time.logTime(time, pill, date)

        elif timeChoice == 2:
            self.time.removeTime()

        elif timeChoice == 3:
            self.time.seeLog()

        elif timeChoice == 4:
            self.time.recentLog()

        else:
            print("Not A Menu Option!")

            

if __name__ == "__main__":

    track = PillTracker()
    track.menu()
