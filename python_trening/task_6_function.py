def add(x, y):
    return x + y
print (add (1, 2))
print (add ('I a', "m tester"))

def arg(a, b, c=2, d=3):
    return a + b + c + d
print(arg(1, 1, 1, 1))
print(arg(2, 2))
# print(arg(2, 2, '1', 1)) #'1' нельзя из-за строгой типизации необязательных аргументов

def range_arg(a, b, c, d):
    return a + ' ' + b + ' ' + c + ' ' + d
print(range_arg('1', '2', '3', '4'))
print(range_arg('1', '2', d='3', c='4')) #после обращения все последующие аргументы через обращение

def onearg(a = (1, 2, 3, 4)):
    return a[0]
print (onearg ())

def Pir2(radius, pi=3.14159):
    return pi * radius ** 2
print (Pir2 (4))
