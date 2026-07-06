def cube(no):
    for i in range(1,no+1):
        sum = 0
        sum = sum +  i**3
    return sum

def main():
    value =int(input("enter the number :"))
    ret  = cube(value)
    print("summation is :",ret)

if __name__=="__main__":
    main()