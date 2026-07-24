from multiprocessing import Pool
import os

def prime_list(n):
    prime = []

    for num in range(2, n + 1):
        prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            prime.append(num)

    return (os.getpid(), n, prime, len(prime))

def main():
    size = int(input("Enter number of elements: "))

    numbers = []
    print("Enter the numbers:")
    for i in range(size):
        numbers.append(int(input()))

    with Pool() as p:
        result = p.map(prime_list, numbers)

    for pid, n, primes, count in result:
        print("\nProcess ID :", pid)
        print("Input Number :", n)
        print("Prime Numbers :", primes)
        print("Prime Count :", count)

if __name__ == "__main__":
    main()