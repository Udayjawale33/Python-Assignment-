#Wap that accepts directory name from the user and counts the number of files inside it every five minutes :
#  Directory path :
#  Number of files 
# Date and time 

import os
import time
import schedule

counter = 1

def DirectoryScanner(DirectoryPath):
    global counter

    if not os.path.exists(DirectoryPath):
        print("Directory does not exist")
        return

    FileCount = 0

    for file in os.listdir(DirectoryPath):
        FullPath = os.path.join(DirectoryPath, file)

        if os.path.isfile(FullPath):
            FileCount += 1

    LogFileName = "Directorylog" + str(counter) + ".txt"

    with open(LogFileName, "w") as fobj:
        fobj.write("Directory Path : " + DirectoryPath + "\n")
        fobj.write("Number of Files : " + str(FileCount) + "\n")
        fobj.write("Date and Time : " + time.ctime() + "\n")

    print("Log file created :",LogFileName)

    counter += 1


def main():

    DirectoryPath = input("Enter Directory Path : ")

    DirectoryScanner(DirectoryPath)
    schedule.every(5).minutes.do(DirectoryScanner,DirectoryPath)

    print("Automation script started...")

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()