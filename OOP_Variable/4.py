class C:
    def __init__(self, v) :
        self.__value = v
    def show(self) :
        print(self.__value)


c1 = C(10)
c1.show()
# print(c1.__value)
