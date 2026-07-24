def chkGreater(no1,no2):
    if(no1 > no2):
        print("No1 is grater")
    else:
        print("No2 is grater")

def main():
    no1 = int(input("enter the first number :"))
    no2 = int(input("enter the second number :"))
    chkGreater(no1, no2)

    
if __name__ =="__main__":
    main()