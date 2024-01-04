# class student:
#     name=""
#     def __init__(self,name):
#         self.name=name
#         print(self.name)
#     def into(self,l):
#         print("hello world!")
#         self.l=l
#         print(l)
# obj=student('hello')
# obj.into("hell")
class l1:
    __name=""
    #def __init__(self,n):
    def demo(self,n):
        self.__name=n
        print(self.__name)
    def check(self,a,b):
        print(self.__name)
        if(a>b):
            print(a)
        else:
            print(b)
class l2(l1):
    def inn(self):
        print(self.__name)

#obj2=l1("j")
#obj2=l2()
obb=l2()
obb.demo("Taranvir")
obb.inn()
