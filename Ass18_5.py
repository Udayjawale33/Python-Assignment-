import MarvellousNum

def ListPrime(Data):
    Sum = 0

    for Value in Data:
        if MarvellousNum.ChkPrime(Value) == True:
            Sum = Sum + Value

    return Sum

def main():
    Size = int(input("Enter number of elements : "))

    Data = []

    print("Enter the elements :")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Result = ListPrime(Data)

    print("Addition of prime numbers is :", Result)

if __name__ == "__main__":
    main()