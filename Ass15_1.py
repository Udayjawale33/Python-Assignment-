square = lambda NO : NO * NO 

def main():

    Data =[2,3,4,5,6]

    print("Input data is :",Data)

    Data = list(map(square,Data))
    print("Data after map :",Data)

if __name__ == "__main__":
    main()