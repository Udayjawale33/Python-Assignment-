import multiprocessing
import os
import math

def calculate_factorial(n):
    pid = os.getpid()
    fact = math.factorial(n)

    print("Process ID :", pid)
    print("Input Number :", n)
    print("Factorial :", fact)
    print("-" * 40)

def main():
    numbers = [10,15,20,25]

    p = multiprocessing.Pool()

    p.map(calculate_factorial,numbers)

    p.close()
    p.join()

if __name__ == "__main__":
    main()