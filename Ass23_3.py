from multiprocessing import Pool
import os

def count_even(n):
    count = 0

    for i in range(1, n + 1):
        if i % 2 == 0:
            count += 1

    return (os.getpid(), n,count)

def main():
    
    numbers = [1000000,2000000,3000000,4000000]

    with Pool() as p:
        results = p.map(count_even,numbers)

    print("Count of Even Numbers from 1 to N")
    print("-" * 40)
    
    for pid, n, count in results:
        print(f"Process ID : {pid}")
        print(f"Input Number       : {n}")
        print(f"Even Number Count : {count}")
        print("-" * 40)
        
if __name__ == "__main__":
    main()