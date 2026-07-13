checkeven = lambda No : ( No % 2 == 0)

def main():

    Data =[10,21,50,70,85]
    
    print("Input data is  :",Data)
    
    FData = list(filter(checkeven,Data))
    print("Data after filter :",FData)

if __name__ =="__main__":
    main()