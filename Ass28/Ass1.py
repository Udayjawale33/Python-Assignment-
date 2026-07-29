def CountLines(FileName):
    count = 0

    try:
        fobj = open(FileName,"r")  
        print("file gets openned") 

        for line in fobj:
            count = count + 1

        fobj.close()

        print("Total number of lines in", FileName, ":", count)

    except FileNotFoundError as fobj:
        print("Unable to open file:", FileName)


def main():
    Name = input("Enter file name : ")
    CountLines(Name)


if __name__ == "__main__":
    main()