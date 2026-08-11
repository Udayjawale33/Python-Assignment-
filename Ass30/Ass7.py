# WAAP that performs a file backupevery hour ..
#  1.Accept the source file path.
#  2.accept the destination directroy path
#  3.copy the sourece file to the destination directory
#  4.add the cuurent date and time to the backup filenaame
#  5.write the backup operation details time.


import os
import shutil
import schedule
import time

def BackupFile(SourcePath,DestinationDir):

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
 
    FileName = os.path.basename(SourcePath)
    Name = os.path.splitext(FileName)
 
    BackupFileName = f"{Name}_{timestamp}"
    DestinationPath = os.path.join(DestinationDir,BackupFileName)
 
    shutil.copy(SourcePath,DestinationPath)
 
    print(f"Backup created : {DestinationPath} at {timestamp}")
 
    fobj = open("BackupLog.txt","a")
    fobj.write(f"Backup of {SourcePath} created as {DestinationPath} at {timestamp}\n")
    fobj.close()
   
def main():

    SourcePath = input("Enter the source file path : ")
    DestinationDir = input("Enter the destination directory path : ")
 
    if(not os.path.isdir(DestinationDir)):
        os.makedirs(DestinationDir)
 
    BackupFile(SourcePath, DestinationDir)
    schedule.every(1).hour.do(BackupFile,SourcePath,DestinationDir)
 
    while True:
        schedule.run_pending()
        time.sleep(60)


    print(f"Backup completed successfully at {timestamp}\n")
  

if __name__ == "__main__":
    main()