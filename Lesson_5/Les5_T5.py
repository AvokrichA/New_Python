# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
# выводить ее на экран.

def num(string):
    total = 0
    for number in string:
        total += int(number)
    return total
my_file = open('L5_T5.txt', 'w+')
my_list = input("Введите числа через пробел:")
my_file.write(my_list)
my_file.seek(0)
my_list1 = my_file.read()
my_list2=my_list1.split(' ')
print(num(my_list2))

my_file.close()





# sum_num2=()
# with open("L5_T5.txt", "w+") as my_list:
#     my_list.write(int(input('Введите числа через пробел:').split(' ')))
#     my_list.append(sum_num2)
#     print(sum(sum_num2))
