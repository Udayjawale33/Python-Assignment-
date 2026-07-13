def ChkDivisible(No):
    if No % 5 == 0:
        return True
    else:
        return False

def main():
    Value = int(input("Enter a number : "))

    Result = ChkDivisible(Value)

    print(Result)

if __name__ == "__main__":
    main()
