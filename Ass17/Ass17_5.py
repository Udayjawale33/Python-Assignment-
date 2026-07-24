def ChkPrime(No):
    if No <= 1:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False

    return True

def main():
    Value = int(input("Enter a number : "))

    Result = ChkPrime(Value)

    if Result == True:
        print("It is Prime Number")
    else:
        print("It is not Prime Number")

if __name__ == "__main__":
    main()