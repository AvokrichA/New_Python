class Cell:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):
        difference = self.num - other.num
        if difference >=0:
            return Cell(difference)
        else:
            print('Ошибка вычисления. Разность двух чисел, не должна быть меньше 0')

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __truediv__(self, other):
        return  Cell(self.num // other.num)

    def __make_order__(self, count):
        x = ''
        for i in range(self.num //count):
            x += '*' * count + '\n'
            x+= '*' * (self.num % count) + '\n'
            return x
    def __str__(self):
        return f'{self.num}'

cell = Cell(10)
print(cell.__make_order__(8))
cell_1 = Cell(30)
print(cell_1.__make_order__(5))

print(cell-cell_1)
print(cell+cell_1)
print(cell*cell_1)
print(cell/cell_1)
print(cell_1-cell)




