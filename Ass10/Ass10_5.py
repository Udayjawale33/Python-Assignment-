def odd(no):
    for i in range(1,no+1,2):
        print(i)

def main():
    value = int(input("enter the number :"))
    odd(value)
if __name__=="__main__":
    main()