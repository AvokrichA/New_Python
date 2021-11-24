with open('L5_t3.txt', 'r', encoding='UTF-8') as my_file:
    my_list=tuple(my_file.read().split('\n'))
    print(my_list, sep=':')




    # sal = []
    # poor = []
    # my_list = my_file.read().split('\n')
    # print(my_list)
    # for i in my_list:
    #     i = i.split()
    #     if float(i[::2]) < 20000:
    #         poor.append(i[0])
    #         sal.append(i[::2])
    # print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(float, sal)) / len(sal)}')
