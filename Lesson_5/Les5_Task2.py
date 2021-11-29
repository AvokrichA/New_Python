
with open("text.txt", 'r') as file_obj:
    content = (file_obj.readlines())
    print('В файле Text',len(content),'строк')
    for i in range(len(content)):
        content_1 = content[i].split()
        print('В', i + 1,'строке', len(content_1), 'слов(а)')
    print(content)



