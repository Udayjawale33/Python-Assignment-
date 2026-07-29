def  DisplayFile(FileName):
    count = 0

    try:
        fobj = open(FileName,"r")  
        print("Contents of file") 

        for line in fobj:
            print(line,end="")

        fobj.close()


    except FileNotFoundError as fobj:
        print("Unable to open file:", FileName)


def main():
    Name = input("Enter file name : ")
    DisplayFile(Name)


if __name__ == "__main__":
    main()