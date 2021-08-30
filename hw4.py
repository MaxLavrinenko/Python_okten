# Создать класс Rectangle:
# -конструктор принимает две стороны x,y
# -описать арифметические методы:
#   + сума площадей двух экземпляров класса
#   - разница площадей
#   == или площади равны
#   != не равны
#   >, < меньше или больше
#   при вызове метода len() подсчитывать сумму сторон
# class Rectangle:
#     def __init__(self, x, y):
#         self.y = y
#         self.x = x
#
#     def area(self):
#         return self.x * self.y
#
#     def __add__(self, other):
#         return self.area() + other.area()
#
#     def __sub__(self, other):
#         return self.area() - other.area()
#
#     def __eq__(self, other):
#         return self.area() == other.area()
#
#     def __ne__(self, other):
#         return self.area() != other.area()
#
#     def __lt__(self, other):
#         return self.area() < other.area()
#
#     def __gt__(self, other):
#         return self.area() > other.area()
#
#     def __len__(self):
#         return (self.x + self.y) * 2
#
# rectangle1 = Rectangle(3,4)
# rectangle2 = Rectangle(2,3)
# print(rectangle1.area())
# print(rectangle2.area())
# print(rectangle1 + rectangle2)
# print(rectangle1 - rectangle2)
# print(rectangle1 == rectangle2)
# print(rectangle1 != rectangle2)
# print(rectangle1 > rectangle2)
# print(rectangle1 < rectangle2)
# print(len(rectangle1))
# print(len(rectangle2))

########################################################################################

# Це завдання на наслідування... все максимально розбити по классах
#
# 1) написати програму для запису відомостей про пасажирські перевезення
# 2) перевезення відбувається трьома способами, літаком, машиною, поїздом,
# 3) дані які треба буде зберігати:
#   - вартість квитка(літак, поїзд)
#   - кількість пасажирів(машина)
#   - час в дорозі(всі)
#   - час реєстрації(літак)
#   - клас:перший,другий(літак)
#   - вартість пального(машина)
#   - км(машина)
#   - місце: купе,св(поїзд)
# 4) методи:
#   - розрахунок вартості доїзду(машина)
#   - загальний час перельоту(літак)
#   - порівняти час в дорозі між двома будь якими транспортними засобами(двома об'єктами) - наприклад"літак на 5 годин швидше за поїзд"
#   - вивести всі дані про перевезення(поїзд)


######################################################################

# 1)Створити пустий list
# 2)Створити клас Letter
# 3) створити змінну класу __count.
# 4) при створенні об'єкта має створюватись змінна об'єкта(пропертя) __text, для цієї змінної мають бути гетер і сетер
# 5) при створені об'єкта __count має збільшуватися на 1
# 6) має бути метод(метод класу) для виводу __сount
# 7) має бути метод який записує в наш ліст текст з нашої змінної __text
#
# l = []
#
#
# class Letter:
#     __count = 0
#
#     def __init__(self, text):
#         self.__text = text
#         self.__up_count()
#
#     def set_text(self, text):
#         self.__text = text
#
#     def get_text(self):
#         return str(self.__text)
#
#     @classmethod
#     def __up_count(cls):
#         cls.__count += 1
#
#     @classmethod
#     def get_count(cls):
#         return cls.__count
#
#     def text_to_list(self):
#         l.append(self.__text)
#
#
# letter1 = Letter('text1')
# letter2 = Letter('text2')
# print(letter1.get_text())
# print(letter2.get_text())
# letter1.text_to_list()
# letter2.text_to_list()
# print(l)
# print(Letter.get_count())
# letter1.set_text('textset1')
# print(letter1.get_text())
# letter2.set_text('settext2')
# print(letter2.get_text())