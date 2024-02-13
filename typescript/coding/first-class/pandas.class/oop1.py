# __________________inheritance___________________
# class A:
#     a = 100
#     def funA(self):
#         print(f'It is funA {self.a}')
#
# class B(A):
#     def funB(self):
#         print(f'It is funB {self.a}')
#
# obj = B()
# obj.funA()
# obj.funB()

# __________________Poly___________________
# class A:
#     def myFun(self):
#         print('It is A')
#
#
# class B(A):
#     def myFun(self):
#         print('It is B')
#
# class C(B):
#     def myFun(self):
#         print('It is C')
#
#
# obj = C()
# obj.myFun()

# ___________________Abstract______________________
class A(ABC):
    @abstractmethod
    def


class B(A):
    def myFunA(self):
        print("it is Fun1")

obj = B()
obj.myFunA()

