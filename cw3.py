# 1) создать класс Human (name, age)
# создать два класса Prince и Cinderella:
# у золушки должно быть имя возраст и размер ноги
# у принца имя, возраст и размер найденой туфельки, так же должен быть метод который принимает лист золушек и ищет ту самую
# 
# класса золушки должна быть переменная count которая будет считать сколько экземпляров класса золушка было создано
# и метод класса который будет показывать это количество

# class Human:
#     def __init__(self,name,age):
#         self.age = age
#         self.name = name
#
# class Prince(Human):
#     def __init__(self,name,age,f_shoe):
#         super().__init__(name,age)
#         self.f_shoe = f_shoe
#     def find_cinderella(self,other):
#         for cinderella in other:
#             if self.f_shoe == cinderella.shoe_size:
#                 print(f'Your destiny is {cinderella.name}')
#
#
#
# class Cinderella(Human):
#     __count = 0
#
#     def __init__(self,name,age,shoe_size):
#         super().__init__(name,age)
#         self.shoe_size = shoe_size
#         self.up_count()
#
#     @classmethod
#     def up_count(cls):
#         cls.__count +=1
#
#     @classmethod
#     def get_count(cls):
#         return cls.__count
#
# cinderela1 = Cinderella('Olga',25,36)
# cinderela2 = Cinderella('Anna',28,37)
# cinderela3 = Cinderella('Tanya', 26,38)
# print(Cinderella.get_count())
# cinderellas = [cinderela1,cinderela2,cinderela3]
# prince = Prince('Oleg',30,37)
# prince.find_cinderella(cinderellas)
#

# 2)
# Создать класс записной книжки
# -А каждая манипуляция над ней должна быть методом класса
# -Все данные сохраняем в переменной класса
#
#
# реализовать записную книжку покупок:
# - каждая запись должна содержать название покупки и ее цену
# -сделать менюшку для работы с записной книжкой:
#     '1) Создать запись'
#     '2) Список все записей'
#     '3) Общая сумма всех покупок'
#     '4) Самая дорогая покупка'
#     '5) Поиск по названию покупки'
#     '9) Выход'

# class NoteBook:
#     __note = []
#
#     def __init__(self, text):
#         self.__text = text
#     @classmethod
#     def set_text(cls, text,cost):
#         cls.__text = text
#         cls.__cost = cost
#         cls.__note.append({'name':str(text),'cost':int(cost)})
#     @classmethod
#     def get_list(cls):
#         return print(cls.__note)
#     @classmethod
#     def sum(cls):
#         __sum = 0
#         for i in cls.__note:
#             __sum +=i['cost']
#         return print(f'Сумма: {__sum}')
#     @classmethod
#     def max(cls):
#         __max = 0
#         for i in cls.__note:
#             if __max < i['cost']:
#                 __max = i['cost']
#         for i in cls.__note:
#             if i['cost'] == __max:
#                 print("Самое дорогое из списка", i['name'], i['cost'])
#     @classmethod
#     def search(cls):
#         __name = input(str('что ищем?: '))
#         __res = ''
#         for i in cls.__note:
#             if i['name'] == str(__name):
#                 __res = i['name']
#                 print(f'ВОТ : {__res}', f"Цена: {i['cost']}")
#             else:print("Нет такого продукта")
#
# while True:
#     print('1) Создать запись')
#     print('2) Список всех записей')
#     print('3) Общая сумма всех покупок')
#     print('4) Самая дорогая покупка')
#     print('5) Поиск по названияю покупки')
#     print('9) Выход')
#
#     choice = int(input('Введите пункт из меню: '))
#
#     if choice not in [1, 2, 3, 4, 5, 9]:
#         print('Нет такого пункта')
#         continue
#
#     if choice == 1:
#
#         name = input('ВВедите название продукта: ')
#         cost = input('Стоимость: ')
#         NoteBook.set_text(name,cost)
#
#     elif choice == 2:
#         NoteBook.get_list()
#
#     elif choice == 3:
#        NoteBook.sum()
#
#     elif choice == 4:
#         NoteBook.max()
#
#     elif choice == 5:
#         NoteBook.search()
#
#     elif choice == 9:
#         break