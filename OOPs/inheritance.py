class first:
    def func1(self):
        print("func1")
class second(first):
    def func2(self):
        print("func2")
class third:
    def func3(self):
        print("func3")
class fourth(second,third):
    def func4(self):
        print("func4")
print("from first function")
obj1 = first()
obj1.func1()
print("from second function")
obj2 = second()
obj2.func1()
obj2.func2()
print("from third function")
obj3 = third()
obj3.func3()
print("From fourth function")
obj4 = fourth()
obj4.func1()
obj4.func2()
obj4.func3()
obj4.func4()