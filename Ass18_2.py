def Maximum(Data):
    Max = Data[0]

    for Value in Data:
        if Value > Max:
            Max = Value

    return Max

def main():
    Size = int(input("Enter number of elements : "))

    Data = []

    print("Enter the elements :")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Result = Maximum(Data)

    print("Maximum number is :", Result)

if __name__ == "__main__":
    main()