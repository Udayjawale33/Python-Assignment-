import threading

def EvenList(Data):
    Sum = 0

    for Value in Data:
        if Value % 2 == 0:
            Sum = Sum + Value

    print("Sum of even elements is :", Sum)

def OddList(Data):
    Sum = 0

    for Value in Data:
        if Value % 2 != 0:
            Sum = Sum + Value

    print("Sum of odd elements is :", Sum)

def main():
    Size = int(input("Enter number of elements : "))

    Data = []

    print("Enter the elements :")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Even = threading.Thread(target=EvenList, args=(Data,), name="EvenList")
    Odd = threading.Thread(target=OddList, args=(Data,), name="OddList")

    Even.start()
    Odd.start()

    Even.join()
    Odd.join()

if __name__ == "__main__":
    main()