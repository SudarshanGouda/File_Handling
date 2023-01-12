'''
additional file opening modes:
r+ - allows to read and write

file.write and file.read


w+ - allows to write and read
the difference between r+ and w+ is that it's gonna
remove existing file if there was no file then
it's gonna create a new file

a+ - "endless" mode of appending and reading
ATTENTION!
write function will ALWAYS append text
even if you change the pointer using "seek"

if file doesn't exist - it creates it

'''

################### Read Plus ###########################

# with open('Names.txt','r+') as file:
#     print(file.readline())
#     file.write('Shivam S')
#     file.seek(0)
#     print(file.readlines())
# file.close()


################### Read Plus ###########################
# with open('FullNames.txt','w+') as file:
#     file.write('Sudarshan Gouda \n'
#                'Anaisha A \n'
#                'Ananya M \n'
#                'Ishana R \n'
#                'Ishita D\n'
#                'Aahva A \n'
#                'Atiksh S \n')
#     file.write('Shivam S \n'
#                'Satwik R \n')
#     file.seek(0)
#     print(file.readlines())

################### Append Plus ###########################

with open('FullNames.txt','a+') as files:
    print(files.tell())
    files.seek(0)
    print(files.readlines())
    print(files.tell())
    files.write('Sandeep M \n')
    files.seek(0)
    print(files.readlines())
