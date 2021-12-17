# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
# Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Рисовать ручкой', self.title)

class Pensil(Stationery):
    def draw(self):
        print('Рисовать карандашом', self.title)

class Handle(Stationery):
    def draw(self):
        print('Рисовать маркером', self.title)

pen_1 = Pen('Линия 0,7 мм')
pensil_1 = Pensil('Линия 2 мм')
handle_1 = Handle('Линия 4 мм')

for i in (pen_1, pensil_1, handle_1):
    i.draw()
