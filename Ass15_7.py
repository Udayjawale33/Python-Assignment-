
def main():
    Data = input("Enter strings : ").split()

    Result = list(filter(lambda Str: len(Str) > 5, Data))

    print("Strings :", Result)

if __name__ == "__main__":
    main()