
import sys
 
def main():
    
    if(len(sys.argv) != 3):
        print("Invalid number of arguments")
        print("Usage : FileCopy.py SourceFile DestinationFile")
        return
 
    SourceFile = sys.argv[1]
    DestinationFile = sys.argv[2]
 
    try:
        fobj1 = open(SourceFile,"r")
        Data = fobj1.read()
        fobj1.close()
 
        fobj2 = open(DestinationFile,"w")
        fobj2.write(Data)
        fobj2.close()
 
        print("File copied successfully")
 
    except FileNotFoundError:
        print("Source file is not present")
 
if __name__ == "__main__":
    main()
 
