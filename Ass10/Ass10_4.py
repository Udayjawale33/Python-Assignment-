def even(no):
    for i in range(2,no+1,2):
        print(i)

def main():
    value = int(input("enter the number :"))
    even(value)

if __name__=="__main__":
    main()