def NameLength(Name):
    return len(Name)

def main():
    Name = input("Enter name : ")

    Result = NameLength(Name)

    print("Length of name is :", Result)

if __name__ == "__main__":
    main()