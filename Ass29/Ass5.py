import sys

def Frequency(FileName,Word):
    try:
        fobj = open(FileName,"r")

        data = fobj.read()
        count = data.count(Word)

        print(Word,"appears",count,"times in",FileName)

        fobj.close()

    except FileNotFoundError:
        print("Unable to open file")

def main():

    if len(sys.argv) != 3:
        print("count of occureeences ")
        return

    Frequency(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()