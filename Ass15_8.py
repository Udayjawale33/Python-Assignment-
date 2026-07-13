
def main():

    Data = list(map(int, input("Enter numbers : ").split()))

    Result = list(filter(lambda No: No % 3 == 0 and No % 5 == 0, Data))

    print("Numbers :", Result)

if __name__ == "__main__":
    main()