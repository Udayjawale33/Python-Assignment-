## schedule a task that executes every five minutes : created files marvellous.txt 

import sys 
import time 

import schedule

def DirectoryScanner():
    timestamp = time.ctime()
    LogFileName = "Marvellous%s.log"%(timestamp)
    LogFileName = LogFileName.replace(" ","_")

    print("log file gets create with name  :",LogFileName)

    fobj = open("Marvellous.txt" , "a")

    fobj.write(f"Task executed at : {timestamp} \n")

    fobj.close()


def main():
    Border ="-"*40
    print(Border)
    print("Marvellous Automation Script ")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] =="--h" or sys.argv[1] == "--H"):

            print("the automation script is used to create the new data in existing file after fix interval of time")
            print("for better usage please check --u flag")
            
        elif(sys.argv[1] =="--u" or sys.argv[1] =="--U"):

            print("please execut script as")
            print("python FileName.py DirectoryName")
            print("DiretoryName should be absolute path")

    elif(len(sys.argv)== 1):
        schedule.every(5).minutes.do(DirectoryScanner)

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
       
       print("invalid number of argument")
       print("please use --h or --u formore information")
      
    print(Border)
    print(" Thank you for using Marvellous Automation Script ")
    print(Border)


if __name__ =="__main__":
    main()