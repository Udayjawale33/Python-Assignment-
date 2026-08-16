#Wap that monitors the size of a specified file every 30 seconds :
# filesizelog.txt    
# 1. file path 2. file size in bytes 3 .date and time 

import os
import time
import schedule


def MonitorFile(FilePath):

    if not os.path.exists(FilePath):
        print("File does not exist.")
        return

    FileSize = os.path.getsize(FilePath)

    CurrentTime = time.ctime()

    print("-----------------------------------")
    print("File Path :", FilePath)
    print("File Size :", FileSize, "bytes")
    print("Date Time :", CurrentTime)
    print("-----------------------------------")

    with open("filesizelog.txt", "a") as fobj:
        fobj.write("File Path : " + FilePath + "\n")
        fobj.write("File Size : " + str(FileSize) + " bytes\n")
        fobj.write("Date Time : " + CurrentTime + "\n")
        fobj.write("-----------------------------------\n")


def main():

    FilePath = input("Enter File Path: ")

    MonitorFile(FilePath)

    schedule.every(30).seconds.do(MonitorFile,FilePath)

    print("File monitoring started...")

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()