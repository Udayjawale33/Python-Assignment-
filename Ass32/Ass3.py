#Wap that reads and display the contents of a specified text file every minute :
# File does not exist , file is empty , permission is denied file cannot be opened

import os
import time
import schedule


def ReadFile(FilePath):

    if not os.path.exists(FilePath):
        print("Error: File does not exist.")
        return

    if not os.path.isfile(FilePath):
        print("Error: Specified path is not a file.")
        return

    try:
       
        with open(FilePath, "r") as fobj:

            Data = fobj.read()

            if Data == "":
                print("File is empty.")
            else:
                print("-----------------------------------")
                print("File Contents:")
                print(Data)
                print("-----------------------------------")

    except PermissionError:
        print("Error: Permission is denied.")

    except OSError:
        print("Error: File cannot be opened.")


def main():

    FilePath = input("Enter File Path: ")

    ReadFile(FilePath)

    schedule.every(1).minutes.do(ReadFile,FilePath)

    print("File monitoring started...")

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()