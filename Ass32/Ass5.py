#Wap that deletes all empty files from a specified directory every hour
# Scan the directory recursively 
# detect files whose size is zero byte 
# delete the empty files 
# store deleted file paths in a log file
# handle permission errors

import os
import time
import schedule


def DeleteEmptyFiles(DirectoryPath):

   
    if not os.path.exists(DirectoryPath):
        print("Directory does not exist.")
        return

    if not os.path.isdir(DirectoryPath):
        print("Specified path is not a directory.")
        return

    LogFile = "DeletedFilesLog.txt"

    print("\nScanning directory:",DirectoryPath)
    print("Date and Time:", time.ctime())

    
    for Root, Directories, Files in os.walk(DirectoryPath):

        for FileName in Files:

            FilePath = os.path.join(Root,FileName)

            try:
                
                if os.path.getsize(FilePath) == 0:

                    try:
                    
                        os.remove(FilePath)

                        print("Deleted:", FilePath)

                        with open(LogFile,"a") as fobj:
                            fobj.write(
                                FilePath +
                                " | Deleted on: " +
                                time.ctime() +
                                "\n"
                            )

                    except PermissionError:
                        print("Permission denied:",FilePath)

                    except OSError as e:
                        print("Unable to delete:",FilePath)
                        print("Error:", e)

            except PermissionError:
                print("Permission denied while accessing:",FilePath)

            except OSError as e:
                print("Unable to access:",FilePath)
                print("Error:",e)

    print("Scanning completed.")


def main():

    DirectoryPath = input("Enter directory path: ")

    DeleteEmptyFiles(DirectoryPath)

    schedule.every(1).hours.do(DeleteEmptyFiles,DirectoryPath)

    print("\nAutomation started...")
    

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()