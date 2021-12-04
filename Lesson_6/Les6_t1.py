class Dish:
#создаем конструктор
    def __init__(self, title, country, weight):
        self.title = title      # создаем атрибут(self.title) и передаем значение(title)
        self.country = country
        self.weight = weight
#создаем метод
    def get_title_and_country(self): #принято всегда указывать self (можно назвать по друому,
        # но это плохой тон в среде программистов, сюда же можно передавать любые параметры, через запятую после self)
        return f'{self.title} from {self.country}'

#создаем класс потомок

class SpicyDish(Dish):   #если название из двух слов, пишем каждое слово с большой буквы, не используем разделитель(пробел, подчеркивание и пр)
    def __init__(self, title, country, weight):
        self.title = title      # создаем атрибут(self.title) и передаем значение(title)
        self.country = country
        self.weight = weight
        self.spicy = True   #создаем новый атрибут (любое, в этом случае булево значение)

        #создаем еще один новый атрибут
    def get_info(self):
        return ('This is spicy dish!')

#создаем новый объект
my_spicy_dish = SpicyDish('Harcho', 'Georgia', 500)


my_Dish1 = Dish('Pasta', 'Italy', '300') #создаем объект внутри конструктора (переменную my_Dish1), обязательно указываем класс (Dish) и передаем параметры
my_Dish2 = Dish('Borcsh', 'Ucraine', '350')
# print(my_Dish1.title)
# print(my_Dish1.country)
# print(my_Dish1.weight)
# print(my_Dish1.get_title_and_country())
print(my_spicy_dish.spicy)
print(my_spicy_dish.get_info())







