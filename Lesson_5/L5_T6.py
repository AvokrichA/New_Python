# Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий
# по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

d = {}
with open('Les5_T6.txt', 'r', encoding='UTF-8') as f_obj:
    while True:
        s=0
        f_obj_line=f_obj.readline()
        if not f_obj_line:
            break
        key_value = f_obj_line.split(" ")
        for i in key_value[1:]:
            j=''
            for x in range(len(i)):
                if i[x].isdigit():
                    j+=i[x]
            if j != '':
                s+= int(j)
        d[key_value[0][0:-1]] = s
print(d)



    # for line in f_obj_line:
    #     key_value = line.split(" ")
    #     value = 0
    #     for i in d:
    #         list=d(i)
    #         if i.isdigit():
    #             value+=i
    #         else:
    #             break
    #         for j in sum_value:
    #             s_value+= sum_value(j)
    #         print(s_value)












