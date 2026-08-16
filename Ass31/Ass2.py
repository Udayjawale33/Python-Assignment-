# create a function named:
#displaymessage(message):
#the message should be accpeted to the user
import schedule
import time
import sys

def DisplayMessage(message):

   print(message)

def main():

    message = ("Jay Ganesh.....")

    schedule.every(5).seconds.do(DisplayMessage,message)
     
    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    main()