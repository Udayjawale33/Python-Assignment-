import threading

def DisplayEven():
    for i in range(1, 11):
        print(i * 2)

def DisplayOdd():
    for i in range(1, 11):
        print((i * 2) - 1)

def main():
    Even = threading.Thread(target=DisplayEven, name="Even")
    Odd = threading.Thread(target=DisplayOdd, name="Odd")

    Even.start()
    Odd.start()

    Even.join()
    Odd.join()

if __name__ == "__main__":
    main()