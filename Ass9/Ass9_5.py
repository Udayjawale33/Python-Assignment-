def div(no):
    if (no%3 == 0 and no%5 == 0):
        print("divisible by 3 and 5 ")
    else:
        print("its not divisible 3 and 5")


def  main():
    value=int(input("enter the number :"))
    div(value)

if __name__=="__main__":
    main()