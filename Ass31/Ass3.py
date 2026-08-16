# WAP that scans a specified direcotry every minute :
#   display name , number of files , numbers of subdirectories , date and time of scanning 

import os
import time
import schedule


def DirectoryScanner(DirectoryPath):
   
    if not os.path.exists(DirectoryPath):
        print("Directory does not exist")
        return

    if not os.path.isdir(DirectoryPath):
        print("Path is not a directory")
        return

    FileCount = 0
    DirectoryCount = 0

    
    for Name in os.listdir(DirectoryPath):
        FullPath = os.path.join(DirectoryPath,Name)

        if os.path.isfile(FullPath):
            FileCount += 1

        elif os.path.isdir(FullPath):
            DirectoryCount += 1

    
    CurrentTime = time.ctime()

    print("-"*40)
    print("Directory Name :",DirectoryPath)
    print("Number of Files:", FileCount)
    print("Number of Subdirectories:",DirectoryCount)
    print("Date and Time of Scanning:",CurrentTime)
    print("-"*40)


def main():
    DirectoryPath = input("Enter directory path: ")

    DirectoryScanner(DirectoryPath)

    schedule.every(1).minutes.do(DirectoryScanner,DirectoryPath)

    print("Directory scanner started...")
    print("Scanning every 1 minute.")

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()