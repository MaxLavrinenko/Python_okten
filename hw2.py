# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,

# st = input("Enter string:  ")
# resint = []
# for i in st:
#     if i.isdigit():
#         resint.append(i)
# resint = ','.join(resint)
# print(resint)

# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі
# st = input('Enter string: ')
# for i in st:
#     if i.isalpha():
#         st = st.replace(i,' ')
# st= ','.join(st.split())
# print(st)


# 1)есть строка:
# greeting = 'Hello, world'
# записать каждый символ в лист поменяв его на верхний регистр
# пример:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
# greeting = 'Hello, world'
# greeting = list(greeting.upper())
# print(greeting)

# вариант 2 (правильный)
# l = [i.upper() for i in greeting]
# print(l)

# 2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
# пример:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
#
# l = [i**2 for i in range(50) if i % 2 !=0]
# print(l)
#

# function
#
# - створити функцію яка виводить ліст
# l = [1,2,3,4,5,6]
#
#
# def func(*args):
#     print(args)
#

# func(*l)
# - створити функцію яка приймає три числа та виводить та повертає найменьше.


# def func(a,b,c):
#     print(min(a,b,c))


# func(8,4,6)

# - створити функцію яка приймає три числа та виводить та повертає найбільше.


# def func(a,b,c):
#     print(max(a,b,c))
#
#
# func(8,4,6)
# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше


# def func(*args):
#     print(max(args))
#     return min(args)
#
#
# x = func(3,5,6,7,8,1)
# print(x)

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
# l=[10,5,11]
#
#
# def func(*args):
#     sum=0
#     for i in args:
#         sum= sum + i
#     return sum
#
#
# x = func(*l)
# print(x)
# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
# def func(*args):
#     sum = 0
#     for i in args:
#         sum= sum + i
#     return sum/len(args)
#
#
# x = func(*l)
# print(x)

# ...decorators
# - є функція: pr def pr():
#                 return 'Hello_boss_!!!'
#  написати декоратор до цієї функції, який замінює нижні підчеркування на пробіли і повертає це значення
#
# функцию pr менять не можно

# def decor(f):
#     def inner(*args,**kwargs):
#         return f(*args,**kwargs).replace('_',' ')
#     return inner
#
#
# @decor
# def pr():
#     return 'Hello_boss_!!!'
#
#
# print(pr())
