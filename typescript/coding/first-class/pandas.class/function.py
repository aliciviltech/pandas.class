# def mySum (a):
#     print(f' value of a {a+a}')
# mySum(1)

# def mySum (a,b):
#     print(f' value of sum {a+b}')
# mySum(4,5)

# def mySum (a, b=2):
#     print(f' value of a {a+b}')
# mySum(3)

# def mySum (a, b=2):
#     print(f' value of a {a+b}')
# mySum(8,6)  /*periortry more*/

# def myCalc(a=0, b=0, c='+'):
#     if(c=='+'):
#         print(a+b)
#     elif(c=='-'):
#         print(a-b)
#     elif(c=='X'):
#         print(a*b)
#     elif(c=='/'):
#         print(a/b)
# myCalc(3,4,c='-')
# myCalc(c='X', b=4, a=3)

# def myFun():
#     return 'Hello IHI'
# x= myFun()
# print(x)

# def myFun():
#     return 34
# myCalc(myFun(), 2, '+')def myFun(): //connect with above if codition.
#     return 'Hello IHI'
# x= myFun()
# print(x)

# def myFun(a,b):
#     return (a+b)
# a = myFun(2, 3)
# print(a) //its ok but sir out 36

def isPrimeNumber(val):
    i=2
    while(i < val):
        if(val % i == 0):
            return (False)
        i+=1
        return (True)
for i in range(100):
        if (isPrimeNumber(i)):
            print(f'{i}:', isPrimeNumber(i))


