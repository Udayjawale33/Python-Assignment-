from functools import reduce

def main():
    Size = int(input("Enter number of elements : "))

    Data = []

    print("Enter the elements :")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    FData = list(filter(lambda No: No % 2 == 0, Data))
    print("List after filter :", FData)

    MData = list(map(lambda No: No * No, FData))
    print("List after map :", MData)

    Result = reduce(lambda No1, No2: No1 + No2, MData)
    print("Output of reduce :", Result)

if __name__ == "__main__":
    main()