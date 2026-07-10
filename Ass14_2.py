cube = lambda no: (no * no * no)

def main():
    value=int(input("enter the number :"))

    ret= cube(value)

    print("cube :",ret)

if __name__=="__main__":
    main()