class Calculator:
    num = 100

    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("i am called automatically when object is created")

    def getData(self):
        print("i am now executing as a method in class")

    def Summation(self):
        return self.a + self.b + self.num


obj = Calculator(2, 3)
obj.getData()
print(obj.Summation())

