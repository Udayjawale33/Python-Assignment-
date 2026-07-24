def Addition(Data):
    Sum = 0

    for Value in Data:
        Sum = Sum + Value

    return Sum

def main():
    Size = int(input("Enter number of elements : "))

    Data = []

    print("Enter the elements :")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Result = Addition(Data)

    print("Addition of all elements is :", Result)

if __name__ == "__main__":
    main()