#num = 3
num = -23
#num = 0
# num = 8.46

if num >= 0:
    print('Число больше либо равно 0')
else:
    print('Число отрицательное')

str_1 = 'test'
str_2 = 'test1'
if str_1 in str_2:
    print('2 строка содержит в себе строку 1')
else:
    print('2 строка НЕ содержит в себе строку 1')

num_float = 3.4
# num_float = 0
# num_float = -7
if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('ноль')
else:
    print('Отрицательное число')

permit_print = True
if num > 0 and permit_print:
    print('num - положительное число')
elif num < 0 and permit_print:
    print('num - отрицательное число')
elif num == 0 and permit_print:
    print('num равно 0')
elif not permit_print:
    print('Печать запрещена')


Course_of_Study = 2
if Course_of_Study == 1 or 2 or 3 or 4:
    print('бакалавр')
elif Course_of_Study == 5 or 6:
    print('магистр')
elif Course_of_Study == 7 or 8 or 9:
    print('аспирант')
else:
    print('Введите корректный год обучения')

number = -56
if number > 100 or number < -100:
    print ('-')
else:
    print ('+')