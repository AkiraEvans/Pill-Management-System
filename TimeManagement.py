# Author: Akira Evans
# Project: Pill Management System
# Created: July 21, 2026
# Description: Handles medication tracking and pill management.

from datetime import datetime

class TimeManagement:

    def timeMenu(self):
        print(
            "\n1. Log Time\n"
            "2. Remove Most Recent Time\n"
            "3. See Time Log\n"
            "4. Most Recent Log \n"
        )


    def logTime(self, time, pill, date):
        
        dateObj = datetime.strptime(date, "%m%d%Y")
        date = dateObj.strftime("%m/%d/%Y")

        timeObj = datetime.strptime(time, "%I%M %p")
        time = timeObj.strftime("%I:%M %p")

        with open("pills.txt", "r") as file:
            pills = file.read().splitlines()

        if pill in pills:

            with open("times.txt", "a") as file:
                file.write(pill + " taken on " + date + " at " + time + "\n")
        else:
            print("Pill Does Not Exist!")

        
    def removeTime(self):
        with open("times.txt", "r") as file:
            log = file.read().splitlines()

        if log:
            log.pop()
        else:
            print("File Is Empty!")

        with open("times.txt", "w") as file:
            file.write("\n".join(log))


    def seeLog(self):
        with open("times.txt", "r") as file:
            print(file.read())


    def recentLog(self):
        with open("times.txt", "r") as file:
            log = file.read().splitlines()
        
        if log:
            print(log[-1])
        else:
            print("File Is Empty!")

    
