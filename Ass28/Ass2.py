def CountWords(FileName):

    try:
        fobj = open(FileName,"r")  
        print("file gets openned") 

        for words in fobj:

            data = fobj.read()
            word = data.split()
            count = len(words)

        fobj.close()

        print("Total number of Words in", FileName, ":")

    except FileNotFoundError as fobj:
        print("Unable to open file:", FileName)


def main():
    Name = input("Enter file name : ")
    CountWords(Name)


if __name__ == "__main__":
    main()