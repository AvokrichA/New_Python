# 1. Реализовать класс Matrix (матрица).
# a)Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные
# (список списков) для формирования матрицы.
# b)реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# c) реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

class Matrix:
    def __init__(self, nums):
        self.nums = nums

    def __str__(self):
        for row in self.nums:
            for i in row:
                print(f"{i:4}", end="")
            print()
        return ''

    def __add__(self, other):
        nums = []
        for i in range(len(self.nums)):
            list=[]
            for j in range(len(self.nums[i])):
                sum = self.nums[i][j]+other.nums[i][j]
                list.append(sum)
        return Matrix(nums)

a = Matrix([[3, 2, 1], [5, 3, 8], [3, 6, 9]])
b = Matrix([[3, 2, 1], [6, 5, 4], [9, 8, 7]])
c = Matrix([[3, 2, 1], [5, 3, 8], [3, 6, 9]])+Matrix([[3, 2, 1], [5, 3, 8], [3, 6, 9]])
print(a)
print(b)
print(c)




