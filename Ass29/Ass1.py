import os

def main():

    if(os.path.exists("Demo1.txt")):
        print("File is present in current directory")
    else:
        print("File is  Not present in current directory")
    
if __name__ =="__main__":
    main()