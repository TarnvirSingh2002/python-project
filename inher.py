class demo:
    __name=None
    def show(self):
        print(self.__name)

class demo2(demo):
    def view(self):
        print(self.__name)

obj=demo2()
obj.show()
obj.view()