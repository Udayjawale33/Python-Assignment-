import threading

Results = {}

def Addition(Data):
    Sum = 0

    for Value in Data:
        Sum = Sum + Value

    Results["Sum"] = Sum

def Product(Data):
    Mult = 1

    for Value in Data:
        Mult = Mult * Value

    Results["Product"] = Mult

def main():
    Size = int(input("Enter number of elements : "))

    Data = []

    print("Enter the elements :")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    T1 = threading.Thread(target=Addition, args=(Data,))
    T2 = threading.Thread(target=Product, args=(Data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Sum of elements is :", Results["Sum"])
    print("Product of elements is :", Results["Product"])

if __name__ == "__main__":
    main()