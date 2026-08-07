def main():
   try:

       fobj = open("Demo1.txt","r")  
       print("file gets openned")  

       Data = fobj.read()   
       print(Data)
       fobj.close()
       
   except FileNotFoundError as fobj:
        print("file is not present ")

if __name__ == "__main__":
    main()
