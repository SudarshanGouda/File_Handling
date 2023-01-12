"""
EXERCISE:

Load names and surnames from a file called:
namesurnames.txt

1) split values. The result should be a list of tuples:
[
 ("Arkadiusz", "Włodarczyk"),
 ("Some", "Guy"),
 ("Another", "AnotherMan")
]

2) save names to a file called names.txt
3) save surnames to a file called surnames.txt
"""
Name_surnames = []
with open('namesurnames.txt','r') as file:
    for line in file:
        Name_surnames.append(tuple(line.replace('\n','').split(' ')))

with open('FirstName.txt','w+') as file:
    for name in Name_surnames:
        file.write(name[0]+'\n')

with open('LastName.txt','w+') as file:
    for name in Name_surnames:
        try:
            file.write(name[1]+'\n')
        except IndexError:
            file.write('\n')
