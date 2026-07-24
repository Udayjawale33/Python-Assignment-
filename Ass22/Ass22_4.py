from multiprocessing import Pool
import time
import os

# Function to calculate 1^5 + 2^5 + ... + N^5
def sumoffifthpowers(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 5

    return (os.getpid(), n, total)

def main():
   
    numbers = [1000000, 2000000, 3000000, 4000000]

    print("Input Values:", numbers)

    start_time = time.time()

    with Pool() as p:
        results = p.map(sumoffifthpowers, numbers)
    
    end_time = time.time()

    print("\nResults:")
    for pid, n, total in results:
        print(f"Process ID: {pid}")
        print(f"N = {n}")
        print(f"Sum = {total}")
        print("-" * 60)

    print(f"Total Execution Time: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()