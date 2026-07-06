def square(no):
    for i in range(1,no+1):
        sum=0
        sum= sum + i**2
    return sum

def main():

    value=int(input("enter the number :"))
    ret = square(value)
    print("summation is:",ret)



if __name__=="__main__":
    main()