import threading

def DisplayForward():
    for i in range(1, 51):
        print(i, end=" ")

def DisplayReverse():
    for i in range(50, 0, -1):
        print(i, end=" ")

def main():
    Thread1 = threading.Thread(target=DisplayForward, name="Thread1")
    Thread2 = threading.Thread(target=DisplayReverse, name="Thread2")

    Thread1.start()
    Thread1.join()

    print()

    Thread2.start()
    Thread2.join()

if __name__ == "__main__":
    main()