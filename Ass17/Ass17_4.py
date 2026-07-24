def SumFactors(No):
    Sum = 0

    for i in range(1, No):
        if No % i == 0:
            Sum = Sum + i

    return Sum

def main():
    Value = int(input("Enter a number : "))

    Result = SumFactors(Value)

    print("Addition of factors is :", Result)

if __name__ == "__main__":
    main()