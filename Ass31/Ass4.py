# Wap that create a new log file after every ten minutes:
# 

import time
import schedule

def CreateLogFile():

    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = "Marvellous_"+timestamp+".log"

    
    with open(filename, "w") as fobj:
        fobj.write("Marvellous Automation Log\n")
        fobj.write("Log file created successfully\n")
        fobj.write("Date and Time:"+time.ctime()+"\n")

    print("Log file created:",filename)

def main():
  
    CreateLogFile()

    schedule.every(10).minutes.do(CreateLogFile)

    print("Automation started...")

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()