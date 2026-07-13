from functools  import reduce 

Addition = lambda NO1 , NO2 : NO1 + NO2 

def main():

    Data =[11,20,30,40,50]

    print("Input data is :",Data)

    rData = reduce (Addition,Data)
    print("Data after reduce :",rData)

if __name__ == "__main__":
    main()