# def task_1(a: int, b: float, c: str, d: list, e: bool):
#     return a, b, c, d, e
# a= 24
# b= 17
# c= 555
# d= [1, 2]
# e= True
# print(task_1(a, b, c, d, e))
# print(task_1(type(a), type(b), type(c), type(d), type(e)))


def task_1():
    a: int = 24
    b: float = 1.7
    c: str = 'grogu'
    d: list = [12, 1, 23, 5]
    e: bool = True

    print(a, type(a), "  ", b, type(b), "  ", c, type(c), "  ", d, type(d), "  ", e, type(e))

task_1()

def task_2() -> list: #Последовательность Фибоначчи
    a = [1, 2, 3, 5, 8, 13, 21]
    return a[0:3]
print(task_2())

def task_3(a) -> int:
    return a ** 2
print(task_3(3))
