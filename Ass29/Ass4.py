import sys


def CompareFiles(fobj1,fobj2):
    try:
        obj1 = open(fobj1,"r")
        obj2 = open(fobj2,"r")

        if obj1.read() == obj2.read():
            print("Success")
        else:
            print("Failure")

        obj1.close()
        obj2.close()

    except FileNotFoundError:
        print("File not found")

def main():
    if len(sys.argv) != 3:
        print("Same files are present")
        return
    CompareFiles(sys.argv[1], sys.argv[2])


if  __name__ == "__main__":
    main()