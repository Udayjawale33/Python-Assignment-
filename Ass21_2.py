import threading

def Maximum(Data):
    Max = Data[0]

    for Value in Data:
        if Value > Max:
            Max = Value

    print("Maximum element is :", Max)

def Minimum(Data):
    Min = Data[0]

    for Value in Data:
        if Value < Min:
            Min = Value

    print("Minimum element is :", Min)

def main():
    Size = int(input("Enter number of elements : "))

    Data = []

    print("Enter the elements :")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    T1 = threading.Thread(target=Maximum, args=(Data,))
    T2 = threading.Thread(target=Minimum, args=(Data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()