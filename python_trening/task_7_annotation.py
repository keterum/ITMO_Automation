a: int = 5
b: str = 'строка'
c: list = [1, 2]
def indent(s: str, width: int) -> str:
    return " " * (max(0, width - len(s))) + s
print(indent('123', 123))

def strlen(s: str='') -> int:
    return len(s)
# print(strlen())

def strlen2(a: list, b: list) -> int:
    return max(len(a), len(b))

def random(my_list: list):
    my_list.random('hellooo')
    return my_list
#HFPJ<HFNMCZ!Разобраться!
# print(random('hi'))


def numblist(a: int, b: int, c: int, d: int) -> list:
    return a + b + c + d
print(numblist(1, 2, 3, 4))






