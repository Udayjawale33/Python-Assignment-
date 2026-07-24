def Frequency(Data, No):
    Count = 0

    for Value in Data:
        if Value == No:
            Count = Count + 1

    return Count

def main():
    Size = int(input("Enter number of elements : "))

    Data = []

    print("Enter the elements :")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Number = int(input("Enter element to search : "))

    Result = Frequency(Data, Number)

    print("Frequency is :", Result)

if __name__ == "__main__":
    main()