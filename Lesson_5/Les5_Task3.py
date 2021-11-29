with open('L5_t3.txt', 'r', encoding='UTF-8') as my_file:
    i = 0
    s = 0
    print('Список сотрудников с окладом менее 20000:')
    while True:
        my_list = my_file.readline()
        if not my_list:
            break
        if float(my_list.split(' ')[1]) < 20000:
            print(my_list.split(' ')[0])
        s += float(my_list.split(' ')[1])
        i += 1

    print('Средняя заработная плата сотрудников:', s/i)




