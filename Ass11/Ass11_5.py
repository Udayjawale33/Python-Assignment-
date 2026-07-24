def is_palindrome(NO1):
    original = NO1
    reverse = 0

    while NO1 > 0:
        digit = NO1% 10
        reverse = reverse * 10 + digit
        NO1 = NO1 // 10

    if original == reverse:
        return True
    else:
        return False

def main():

    
    NO1= int (input("Enetr the number :"))

    if is_palindrome(NO1):
    
        print("Palindrome ")

    else:
        print("Not a Palindrome ")


if __name__ == "__main__":
    main()