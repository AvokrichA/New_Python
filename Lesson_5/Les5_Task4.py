with open('L5_T4.txt', encoding='UTF-8') as f_obj:
    for line in f_obj:
        print(line)
rus_dict = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_dict = []
with open('L5_T4.txt') as f_obj:
    for i in f_obj:
        i = i.split(' ', 1)
        new_dict.append(rus_dict[i[0]] + i[1])
    print(new_dict)

with open('L5_T4_1.txt', 'w', encoding='UTF-8') as file_obj_1:
    file_obj_1.writelines(new_dict)

