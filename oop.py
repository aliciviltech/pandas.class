# class MyClass:
#     a=0
#     def myFunction (self):
#         print('Hello MyClass Function')
#
# obj = MyClass()
# obj.a = 100
# obj.myFunction()
# print(obj.a)
#
# obj2 = MyClass()
# print(obj2.a)


# class MyClass:
#     a=0
#     def myFunction (self):
#         self.a = 50
#         print('Hello MyClass Function')
#
# obj = MyClass()
# obj.myFunction()
# print(obj.a)


# class MyClass:
#     a=0
#     def myFunction (self, v1=0 , v2=0):
#         self.a = v1 + v2
#         print('Hello MyClass Function')
#
# obj = MyClass()
# obj.myFunction(2,3)
# print(obj.a)

#__________________________constructor___________________________________

# class MyClass:
#     a=0
#     def __init__(self):
#         print('Strat class MyClass')
#     def myFunction (self, v1=0 , v2=0):
#         self.a = v1 + v2
#         print('Hello MyClass Function')
#
# obj = MyClass()
# obj.myFunction(2,3)
# print(obj.a)

# ____________________Encapsulation________________________
# class MyClass:
#     __a=2
#     def myFunction (self):
#         self.__a = 50
#         print(f'Value of a {self.__a}')
#
# obj = MyClass()
# obj.__a = 100
# obj.myFunction()


# class MyClass:
#     __a=2
#     def myFunction (self):
#         self.__a = 50
#         print(f'Value of a {self.__a}')
#         self.__myPrivateFuntion()
#     def __myPrivateFuntion(self):
#         print('Hello Private Function')
# obj = MyClass()
# obj.__a = 100
# obj.myFunction()

