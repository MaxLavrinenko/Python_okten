# мучить вас сильно не буду
# просто разберите лекцию
#
# и переделайте это задание:
#
# Создать класс записной книжки
# -А каждая манипуляция над ней должна быть методом класса
# -Все данные сохраняем в переменной класса
# реализовать записную книжку покупок:
# - каждая запись должна содержать название покупки и ее цену
# -сделать менюшку для работы с записной книжкой:
#     '1) Создать запись'
#     '2) Список все записей'
#     '3) Общая сумма всех покупок'
#     '4) Самая дорогая покупка'
#     '5) Поиск по названию покупки'
#     '9) Выход'
# - можете придумать свои пункты
#
# но в этот раз данные записываем в файл
import json


class NoteBook:
    __note = []

    def __init__(self, text):
        self.__text = text

    @classmethod
    def set_text(cls, text, cost):
        cls.__text = text
        cls.__cost = cost
        with open('1.json', 'r+') as file:
            cls.__note = list(json.load(file))
        cls.__note.append({'name': text, 'cost': cost})
        with open('1.json', 'w+') as file:
            json.dump(cls.__note, file)

    @classmethod
    def get(cls):
        with open('1.json', 'r') as file:
            d = json.load(file)
            return print(d)

    @classmethod
    def sum(cls):
        __sum = 0
        with open ('1.json','r+') as file:
            ld = list(json.load(file))
        for d in ld:
            __sum += int(d['cost'])
        return print(f'Сумма: {__sum}')

    @classmethod
    def max(cls):
        __max = 0
        with open ('1.json','r+') as file:
            ld = list(json.load(file))
        for d in ld:
            if __max < int(d['cost']):
                __max = int(d['cost'])
        for d in ld:
            if int(d['cost']) == __max:
                print("Самое дорогое из списка", d['name'], d['cost'])

    @classmethod
    def search(cls):
        __name = input(str('что ищем?: '))
        __res = ''
        with open ('1.json','r+') as file:
            ld = list(json.load(file))
        for d in ld:
            if d['name'] == str(__name):
                __res = d['name']
                print(f'ВОТ : {__res}', f"Цена: {d['cost']}")



while True:
    print('1) Создать запись')
    print('2) Список всех записей')
    print('3) Общая сумма всех покупок')
    print('4) Самая дорогая покупка')
    print('5) Поиск по названияю покупки')
    print('9) Выход')

    choice = int(input('Введите пункт из меню: '))

    if choice not in [1, 2, 3, 4, 5, 9]:
        print('Нет такого пункта')
        continue

    if choice == 1:
        name = input('ВВедите название продукта: ')
        cost = input('Стоимость: ')
        NoteBook.set_text(name, cost)

    elif choice == 2:
        NoteBook.get()

    elif choice == 3:
        NoteBook.sum()

    elif choice == 4:
        NoteBook.max()

    elif choice == 5:
        NoteBook.search()

    elif choice == 9:
        break
