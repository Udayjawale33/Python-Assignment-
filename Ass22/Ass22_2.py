from multiprocessing import Pool
import os

def factorial(no):
    fact = 1
    for i in range(1, no + 1):
        fact = fact * i

    return (os.getpid(), no, fact)

def main():
    size = int(input("Enter number of elements: "))

    numbers = []
    
    print("Enter the numbers:")
    for i in range(size):
        numbers.append(int(input()))

    with Pool() as p:
        result = p.map(factorial, numbers)

    print("\nProcess ID\tInput\tFactorial")
    for pid, num, fact in result:
        print(f"{pid}\t\t{num}\t{fact}")

if __name__ == "__main__":
    main()