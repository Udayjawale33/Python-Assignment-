def order(no):

    for i in range(no,0,-1):

         print(i)


def main():

    value = int(input("Enter the number :"))
    
    order(value)

if __name__ == "__main__":
    main()