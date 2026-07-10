checkodd = lambda NO :(NO % 2 == 1) 

def main():
    value = int(input("enter number :"))

    ret = checkodd(value)  

    print(ret)

    if(ret == True):

        print("its odd number")

    else:
        print("False")

if __name__ == "__main__":
    main()