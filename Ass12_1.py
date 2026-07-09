def vowel(ch):

    if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False


def main():
     ch = input("Enter a character: ")

     if vowel(ch):

        print("Vowel")
     else:
        
        print("Consonant")


if __name__ =="__main__":
    main()