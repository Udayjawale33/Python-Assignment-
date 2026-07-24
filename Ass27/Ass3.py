class Numbers:

    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        if self.Value <= 1:
            return False

        for i in range(2, int(self.Value ** 0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        sum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum += i
        return sum == self.Value

    def Factors(self):
        print("Factors of", self.Value, "are:")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        sum = 0
        for i in range(1, self.Value + 1):

            if self.Value % i == 0:
                sum += i
        return sum

def main():
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))

    obj1 = Numbers(n1)
    obj2 = Numbers(n2)

    print("\n----- First Number -----")
    print("Prime :",obj1.ChkPrime())
    print("Perfect :",obj1.ChkPerfect())
    obj1.Factors()
    print("Sum of Factors :",obj1.SumFactors())

    print("\n----- Second Number -----")
    print("Prime :",obj2.ChkPrime())
    print("Perfect :",obj2.ChkPerfect())
    obj2.Factors()
    print("Sum of Factors :",obj2.SumFactors())


if __name__ == "__main__":
    main()