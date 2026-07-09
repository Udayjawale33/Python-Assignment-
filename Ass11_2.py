def main():
    num = int(input("Enter a number : "))

    num = abs(num)  
    count = 0

    if num == 0:
     count = 1
     
    else:
     while num > 0:
        count = count + 1
        num = num // 10

    print("Count of digits =", count)

if __name__=="__main__":
    main()