#   - найти min число в листе
# print(min(l))

#   - удалить все дубликаты в листе
# Вариант 1
# wol = set(l)
# print(wol)

# Вариант 2
# l = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
# i = 0
# while i < len(l):
#     a = l[i]
#     if l.count(a) > 1:
#         while l.count(a) > 1:
#             l.remove(a)
#     else:
#         i += 1
# print(l)
#   - заменить каждое четвертое значение на "Х"
# l = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
# for i in l[4::4]:
#     l[l.index(i)] = 'X'
# print(l)

# 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой
# side = 5
# i = side
# while i >= 1:
#     if i == side or i == 1:
#         j = side
#         while j > 0:
#                 print('*', end='')
#                 j -= 1
#         print('')
#     else:
#         j = side - 2
#         print('*', end='')
#         while j > 0:
#             print(' ', end='')
#             j -= 1
#         print('*')
#     i -= 1
###################
# 3) вывести табличку умножения с помощью цикла while
# i = 1
# while i <= 10:
#     j = 1
#     while j <= 10:
#         print(i * j, end='\t')
#         j = j + 1
#     print('')
#     i = i +1
###################
# 4) переделать первое задание под меню с помощью цикла
l = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
while True:
    print("1. Найти min число в листе")
    print("2. Удалить все дубликаты в листе")
    print("3. Заменить каждое четвертое значение на 'X' ")

    choise = int(input("Введите № задания от 1 до 3: "))
    if choise == 1:
        print("1.Найти min число в листе")
        print(min(l))
    elif choise == 2:
        print("2.Удалить все дубликаты в листе")
        i = 0
        while i < len(l):
            a = l[i]
            if l.count(a) > 1:
                while l.count(a) > 1:
                    l.remove(a)
            else:
                i += 1
        print(l)
    elif choise == 3:
        print("3. Заменить каждое четвертое значение на 'X'" )
        for i in l[4::4]:
            l[l.index(i)] = 'X'
        print(l)
    else:
        print("Нет такого решения")