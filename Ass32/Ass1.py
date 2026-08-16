# Wap that create a new text file every minutes :
# 1.Filename  2.Creation date 3.Creation time 

import os
import time
import schedule


def CreateTextFile():
    
    CurrentTime = time.localtime()

    Date = time.strftime("%Y-%m-%d",CurrentTime)
    Time = time.strftime("%H-%M-%S",CurrentTime)

    FileName = "Demo_" + Date + "_" + Time + ".txt"
    
    with open(FileName, "w") as fobj:
        fobj.write("Filename    : " + FileName + "\n")
        fobj.write("Creation Date: " + Date + "\n")
        fobj.write("Creation Time: " + Time + "\n")

    print("File Created:",FileName)


def main():

    CreateTextFile()
    schedule.every(1).minutes.do(CreateTextFile)

    print("Automation started...")

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()