def fact(no):
        
        
        for i in range(1, no + 1):

          if no % i == 0:

           print(i)

def main():
    no = int(input("Enter a number: "))
    
    ret = fact(no)

    print("fact is :",ret)


if __name__ == "__main__":
    main()