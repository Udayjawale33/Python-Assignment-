checkmini = lambda x,y:( x if x < y  else y )

def main():

    NO1= int(input("Enter first number :"))
    NO2= int (input("Enter second number"))

    
    print( "Minimum number :",checkmini(NO1,NO2))

    
if __name__=="__main__":
    main()