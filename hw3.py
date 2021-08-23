# написать функцию на замыкания которая будет в себе хранить лист дел, вам нужно реализовать два метода
# - первый записывает в эту переменную запись
# - второй возвращает все записи
#
# запишите 5 тудушек
# и выведете все
# 2) протипизировать первое задание
from typing import Callable, List


def notebook() -> Callable:
    todo_list: list = []

    def add_todo(todo: str) -> List:
        nonlocal todo_list
        todo_list.append(todo)

        def get_all() -> None:
            nonlocal todo_list
            print(todo_list)

        get_all()
        return todo_list

    return add_todo


nb = notebook()
nb('wake up')
nb('go breakfast')
nb('go to work')
nb('kill the people')
nb('do homework')

# 3) С помощью lambda функции извлеките из списка числа, делимые на 15 без остатка.
# l = [15, 25, 30, 60, 120, 20]
# print(list(filter(lambda x: x % 15 == 0, l)))

# 4) написать функцию которая будет принимать целое число n и посчитайте n + nn + nnn.
# Пример:
# summ(7) -> 7+77+777=861
#
# def summ(a):
#     res= a + int((f'{a}'+f'{a}')) + int((f'{a}{a}{a}'))
#     print(res)
#
# summ(7)
