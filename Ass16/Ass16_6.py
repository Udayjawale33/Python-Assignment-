def ChkNumber(No):
    if No > 0:
        print("Positive Number")
    elif No < 11:
        print("Negative Number")
    else:
        print("Zero")

def main():
    Value = int(input("Enter a number : "))

    ChkNumber(Value)

if __name__ == "__main__":
    main()