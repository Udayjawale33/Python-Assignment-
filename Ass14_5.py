checkeven= lambda NO :(NO % 2 == 0) 

def main():
    value = int(input("enter number :"))

    ret = checkeven(value)  

    print(ret)

    if(ret == True):
        
        print("its even number")
    else:
        print("False")

if __name__ =="__main__":
    main()