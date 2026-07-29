def  CopyFile(FileName,NewFile):


    try:
        fobj = open(FileName,"r")  
        dobj = open(NewFile,"w")
        print("Contents of file") 

        for line in fobj:
            dobj.write(line)

        fobj.close()
        dobj.close()

        print("Contents Copied Successfully")

    except FileNotFoundError :
        print("Unable to open file")


def main():
    Name = input("Enter existing file name : ")
    File = input("Enter new file name :")
    CopyFile(Name,File)

if __name__ == "__main__":
    main()