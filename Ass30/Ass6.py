## Was that schedules the following tasks :
    #pirnt lunch time ! every dat at 1:00 pm 
    #print wrap up work every da at 6:00 pm 
   # both tasks should handled by searate fuction

import time 
import schedule


def breaktime():

    print("Lanch Time !")

def workitme():

    print(" Wrap up Work ")

def main():

    schedule.every().day.at("01:00").do(breaktime) 
    schedule.every().day.at("06:00").do(workitme) 
    
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()