def area(lenght,width):

    ans = lenght * width

    return ans

def main():

    lenght = float(input("enter lenght is: "))
    width = float(input("enter width is :"))

    area(lenght,width)

    print("area of rectangle :",lenght*width)

if __name__ =="__main__":
    main()