from multiprocessing import Pool

def sum_of_squares(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i * i
    return s

def main():
    value= int(input("Enter number of elements: "))

    numbers = []

    print("Enter the elements:")
    
    for i in range(value):
        numbers.append(int(input()))

    with Pool() as p:
        result = p.map(sum_of_squares, numbers)

    print("Input List :", numbers)
    print("Sum of Squares :", result)

if __name__ == "__main__":
    main()