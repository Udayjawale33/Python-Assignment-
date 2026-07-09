def sum(num):

    total = 0
    
    while num > 0:
        sum = num % 10
        total = total + sum
        num = num // 10

    return total

def main():

    num = int(input("Enter the Number :"))
    print("sum of digits",sum(num))


if __name__ =="__main__":
    main()