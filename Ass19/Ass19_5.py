from functools import reduce

def ChkPrime(No):
    if No <= 1:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False

    return True

def main():
    Size = int(input("Enter number of elements : "))

    Data = []

    print("Enter the elements :")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    FData = list(filter(ChkPrime, Data))
    print("List after filter :", FData)

    MData = list(map(lambda No: No * 2, FData))
    print("List after map :", MData)

    Result = reduce(lambda No1, No2: No1 if No1 > No2 else No2, MData)
    print("Output of reduce :", Result)

if __name__ == "__main__":
    main()