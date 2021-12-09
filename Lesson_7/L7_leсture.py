# from abc import ABC, abstractmethod
#
# class TransportCompany:
#     def move_goods(self, transport, goods):
#         transport.move()
#         print(f'{goods} muved!')
#
# class Transport(ABC):
#     @abstractmethod
#     def move(self):
#         pass
#
#
# class Plane(Transport):
#
#     def move(self):
#         print('Flying')
#
# class Boat(Transport):
#
#     def move(self):
#         print('Swimming')
#
# my_plaine = Plane()
# my_plaine.move()
#
# goods = ['books', 'phones']
# transport_company = TransportCompany()
# transport_company.move_goods(my_plaine, goods)


















# class Dish:
#     count_created = 0
#
#     def __init__(self, title, country, weight, spicy):
#         self._title = title
#         self.__country = country
#         self.weight = weight
#         self.spicy = spicy
#         Dish.count_created +=1
#
#     def __str__(self):          #перегружаем метод str (для предотвращения ошибки: <__main__.Dish object at 0x0000027EF0C88C10)
#         return f'{self._title} ({self.__country})'  # здесь, обязательно возвращаем строку в который будет какая-то информация
#
#     def __repr__(self):          #перегружаем метод repr (для предотвращения ошибки в списках, словарях, кортежах, множествах: <__main__.Dish object at 0x0000027EF0C88C10)
#         return f'{self._title} ({self.__country})'
#
#     def __add__(self, other):    #перегружаем метод add, для возмоджности производить сложение(для других мат. оперций используются меоды: __mul__, __truediv__, __sub__) с объектами
#         weight = self.weight + other.weight
#         return Dish(self._title, self.__country, weight, self.spicy)           #метод add, должен возвращать новй объект класса Dish и передавать туда какие-то параметры
#
#     def get_title_and_country(self, count=1):
#         result = f'{self._title} from {self.__country}' * count
#         return result
#
#     def _get_county(self):
#         return self.__country
#
# my_spicy_dish = Dish('Harcho', 'Georgia', 500, True)
# my_spicy_dish_1 = Dish('Harcho', 'Georgia', 300, True)
#
# # проверяем перегрузку метода str
# print(my_spicy_dish)
#
# #проверяем перегрузку метода repr
# my_list = [my_spicy_dish]
# print(my_list)
#
# # проверяем перегрузку метода add
#
# result = my_spicy_dish + my_spicy_dish_1
# print(result.weight)



