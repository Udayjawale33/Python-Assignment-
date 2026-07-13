def Minimum(Data):
    Min = Data[0]

    for Value in Data:
        if Value < Min:
            Min = Value

    return Min

def main():
    Size = int(input("Enter number of elements : "))

    Data = []

    print("Enter the elements :")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Result = Minimum(Data)

    print("Minimum number is :", Result)

if __name__ == "__main__":
    main()