from pythonDemo.OoopsDemo import Calculator


class ChildImpl(Calculator):
    num2 = 200


    def __init__(self):
        Calculator.__init__(self, 2, 10)

    def GetCompleteData(self):
        return self.num2 + self.num + self.Summation()


obj = ChildImpl()
print(obj.GetCompleteData())
