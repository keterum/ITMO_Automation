def task_2():
    a = 6
    b = 7
    if a > b:
        print(a)
    elif a < b:
        print(b)
    else:
        print(a, '=', b)
task_2()


def task_3():
    c = 136
    d = 1
    if c - d == 135 or d - c == 135:
        print('yes')
    else:
        print('no')
task_3()


def task_4():
    Month = 2
    if Month == 1 or 2 or 12:
        print('зима')
    elif Month == 3 or 4 or 5:
        print('весна')
    elif Month == 6 or 7 or 8:
        print('лето')
    elif Month == 9 or 10 or 11:
        print('осень')
    else:
        print('Некорректно')
task_4()


def task_5():
    e = 6
    f = 11
    g = 34
    if e > 10 and f > 10 and g > 10:
        print('yes')
    else:
        print('no')
task_5()

# def task_6():
#     x = [-5, 6, 7, 8, 2]
#     print(len(x[0:5] > 0))
# task_6()

def task_7(month: int, year: int):
    days = 29
    months_of_the_year = 12
    return (month * days) + (year * months_of_the_year * days)
print(task_7(3, 2))
