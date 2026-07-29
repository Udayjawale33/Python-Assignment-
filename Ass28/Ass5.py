def  CheckWord(FileName,Word):


    try:
        fobj = open(FileName,"r")  
        data = fobj.read()

        if Word  in data:
            print("Word is present in file")
        else:
            
            print("Word is not present in the files")
        fobj.close()

    except FileNotFoundError :
        print("Unable to open file :",FileName)


def main():
    Name = input("Enter file name : ")
    Word = input("Enter word to search :")
    CheckWord(Name,Word)

if __name__ == "__main__":
    main()