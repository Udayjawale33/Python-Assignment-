
from functools import reduce

def main():
    Data = list(map(int, input("Enter numbers : ").split()))

    Result = reduce(lambda A, B: A * B, Data)

    print("Product :", Result)

if __name__ == "__main__":
    main()