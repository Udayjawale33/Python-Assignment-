
def main():
    num=int(input("Enter the number :"))

    count = 0

    for i in range(1, num+1):
        if num % i == 0:
            count = count + 1
            
    if count == 2:
        print("prime")
    else:
        print("not prime")


        
if __name__ == "__main__":
    main()