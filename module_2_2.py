first = int(input('Введите первое целое число: ',)) # запрос на ввод первого числа
second = int(input('Введите второе целое число: ',)) # запрос на ввод второго числа
third = int(input('Введите третье целое число: ',)) # запрос на ввод третьего числа
if first == second == third: # условие равенства всех трех чиел
    print ('3') # вывод в консоль "3"
elif first == second or second == third or third == first: # условие равенства хотя бы двух чисел
    print ('2') # вывод в консоль "2"
else: # в противном случае
    print('0') # вывод в консоль "0"





