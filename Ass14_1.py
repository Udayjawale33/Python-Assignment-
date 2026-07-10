square = lambda no: (no * no)

def main():
    value=int(input("enter the number :"))

    ret= square(value)

    print("square",ret)

if __name__=="__main__":
    main()