def Factorial(No):
    Fact = 1

    for i in range(1, No + 1):
        Fact = Fact * i

    return Fact

def main():
    Value = int(input("Enter a number : "))

    Result = Factorial(Value)

    print("Factorial is :", Result)

if __name__ == "__main__":
    main()