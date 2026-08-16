# Wap that copies all .txt fiels from one directory to another every ten minutes :
# accept source and destination directorices 
# validate both directories 
# copy only .txt files 
# maintain a log of copied files 
# Avoid terminating if one file cannot be copied 


import os
import shutil
import time
import schedule


def CopyTextFiles(SourceDirectory,DestinationDirectory):

    if not os.path.exists(SourceDirectory):
        print("Source directory does not exist.")
        return

    if not os.path.isdir(SourceDirectory):
        print("Source path is not a directory.")
        return

    if not os.path.exists(DestinationDirectory):
        print("Destination directory does not exist.")
        return

    if not os.path.isdir(DestinationDirectory):
        print("Destination path is not a directory.")
        return

    LogFile = "CopyLog.txt"

   
    for FileName in os.listdir(SourceDirectory):

        if FileName.lower().endswith(".txt"):

            SourcePath = os.path.join(SourceDirectory,FileName)
            DestinationPath = os.path.join(DestinationDirectory,FileName)

            if not os.path.isfile(SourcePath):
                continue

            try:
                shutil.copy2(SourcePath,DestinationPath)

                CurrentTime = time.ctime()

                print("Copied:",FileName)

                # Maintain log
                with open(LogFile, "a") as fobj:
                    fobj.write(
                        "File: " + FileName +
                        " | Source: " + SourceDirectory +
                        " | Destination: " + DestinationDirectory +
                        " | Date and Time: " + CurrentTime + "\n"
                    )

            except Exception as e:
                
                print("Unable to copy:",FileName)
                print("Error:",e)

                with open(LogFile,"a") as fobj:
                    fobj.write(
                        "FAILED: " +FileName +
                        " | Error: " + str(e) +
                        " | Date and Time: " + time.ctime() + "\n"
                    )

    print("Copy operation completed.")


def main():

    SourceDirectory = input("Enter source directory: ")
    DestinationDirectory = input("Enter destination directory: ")

   
    CopyTextFiles(SourceDirectory,DestinationDirectory)

    schedule.every(10).minutes.do(
        CopyTextFiles,
        SourceDirectory,
        DestinationDirectory
    )

    print("\nAutomation started...")

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()