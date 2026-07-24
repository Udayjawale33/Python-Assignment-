#write a python program using multiprocessing.pool to calculate the sum of all odd numbeer from 1 to N for every number from the given list ..

from multiprocessing import Pool
import os

def sum_odd(n):
    total = 0
    for i in range(1, n + 1, 2):
        total += i

    return (os.getpid(), n, total)

def main():
    
    numbers = [1000000,2000000,3000000,4000000]

    with Pool() as p:
        results = p.map(sum_odd, numbers)

    print("Sum of odd Numbers from 1 to N")
    print("-" * 40)

    for pid, n, total in results:
        print(f"Process ID : {pid}")
        print(f"Input Number  : {n}")
        print(f"Sum of Odd Numbers   : {total}")
        print("-" * 40)

if __name__ == "__main__":
    main()