def addition(no1,no2):
    ans = no1 + no2
    
    return ans

def subtraction(no1,no2):
    ans = no1 - no2

    return ans

def multiplication(no1,no2):
    ans = no1 * no2

    return ans

def division(no1,no2):
    ans = no1 / no2

    return ans

def main():
    print("Enter first number :")
    value1 = int(input())

    print("Enter second number :")
    value2 = int(input())

    ret = addition(value1 , value2)
    ret1 = subtraction(value1,value2)
    ret2 = multiplication(value1,value2)
    ret3 = division(value1,value2)

    print("addition is :",ret)
    print("subtraction is:",ret1)
    print("multiplication is:",ret2)
    print("division is :",ret3)

if __name__ =="__main__":
    main()