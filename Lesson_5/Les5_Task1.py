
with open("text.txt", 'r') as file_obj:
    content = file_obj.read()
    end = ()
    print(content)
    for i in content:
        print(i)

