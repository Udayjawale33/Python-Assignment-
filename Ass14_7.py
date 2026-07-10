divisible= lambda no :( no % 5 == 0)

def main():

    value=int(input("Enter the number :"))

    ret = divisible(value)

    if divisible(value):

         print("True is divisible 5")

    else:
         print("False is divisible 5")

if __name__ =="__main__":
    main()