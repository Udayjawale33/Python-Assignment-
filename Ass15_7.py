divisible= lambda no :( no % 5 == 0)

def main():

    value=int(input("Enter the number :"))

    ret = divisible(value)

    print(ret)

    