largest = lambda no1,no2,no3: no1 if no1 > no2 and no1 > no3 else (no2 if no2 > no3 else no3)

def main():

    value1 = int(input("Enter first number: "))
    value2= int(input("Enter second number: "))
    value3 = int(input("Enter third number: "))

    print("Largest number =", largest(value1,value2,value3))

if __name__ == "__main__":
    main()