def rev(num):
     
     rev = 0

     while num > 0:
          digit = num % 10
          rev = rev * 10 + digit
          num = num // 10

     return rev
        


def main():

    num = int(input("Enter the Number :"))

    print("Reverse Numbers",rev(num))
     
     

if __name__ =="__main__":
     main()