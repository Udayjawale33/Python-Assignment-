def main():
    value =int(input("enter first number :"))
    factorail = 1
    for i in range(1, value + 1):
         
         factorail =  factorail + i
    print("factorail =",factorail)
    
if __name__=="__main__":
    main()