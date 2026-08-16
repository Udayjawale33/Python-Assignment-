#wap that accepts:
 # a message form  the user 
 # a time interval in seconds 
# vaidate that the interal is greater than zero.


import schedule
import time


def main():

    Message = input("Enter the message : ")
    Interval = int(input("Enter the time interval in seconds : "))
 
    if(Interval <= 0):
        print("Error : interval must be greater than zero")
        return
 
    schedule.every(Interval).seconds.do(lambda: print(Message))
 
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ =="__main__":
    main()