'''

a - A ppend (adding new content at the end)'''

with open('Names.txt','a') as file:
    print(file.tell())
    file.write('Santosh B \n')

file.close()
with open('Names.txt','r') as file:
    for line in file.readlines():
        print(line)

file.close()

