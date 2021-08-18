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

notebook = [
    {'name': 'Хлеб', 'cost': 25},
    {'name': 'Сосиски', 'cost': 50},
    {'name': 'Майонез', 'cost': 15},
    {'name': 'Пиво', 'cost': 35},

]
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
        notebook.append({'name': name, 'cost': int(cost)})

    elif choice == 2:
        for i in notebook:
            print(i['name'],'стоит',i['cost'])

    elif choice == 3:
        sum = 0
        for i in notebook:
            sum += i['cost']
        print('Сумма: ', sum)

    elif choice == 4:
        max = 0
        for i in notebook:
            if max < i['cost']:
                max = i['cost']
        for i in notebook:
            if i['cost'] == max:
                print("Самое дорогое из списка", i['name'],i['cost'])

    elif choice == 5:
        name = str(input('что ищем?: '))
        for i in notebook:
            if i['name'] == str(name):
                print(i['name'],i['cost'])

    elif choice == 9:
        break