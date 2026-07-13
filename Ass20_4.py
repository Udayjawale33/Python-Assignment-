import threading

def Small(Data):
    Count = 0

    for Ch in Data:
        if Ch.islower():
            Count = Count + 1

    print("Number of lowercase characters :", Count)
    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)

def Capital(Data):
    Count = 0

    for Ch in Data:
        if Ch.isupper():
            Count = Count + 1

    print("Number of uppercase characters :", Count)
    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)

def Digits(Data):
    Count = 0

    for Ch in Data:
        if Ch.isdigit():
            Count = Count + 1

    print("Number of digits :", Count)
    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)

def main():
    Data = input("Enter a string : ")

    T1 = threading.Thread(target=Small, args=(Data,), name="Small")
    T2 = threading.Thread(target=Capital, args=(Data,), name="Capital")
    T3 = threading.Thread(target=Digits, args=(Data,), name="Digits")

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()

if __name__ == "__main__":
    main()