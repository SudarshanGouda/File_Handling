''' read
readline
readlines

splitlines
'''
################################    Read  #######################################
with open('Names.txt','r') as file:
    NamesSurnames=file.read()

print(NamesSurnames)
file.close()
################################   Read Line   #######################################

with open('Names.txt','r') as file:
    Nameslist=file.readline()

print(Nameslist)
file.close()

#-------------------------------------------------------------------------
with open ('Names.txt','r') as file:
    Nameslist=file.readline()
    Nameslist1 = file.readline()

print(Nameslist)
print(Nameslist1)
file.close()
#-------------------------------------------------------------------------
with open ('Names.txt','r') as file:
    for line in file.readline():
        print(line)

file.close()

###############################   Read Lines   ###########################################################

with open ('Names.txt','r') as file:
    Nameslist=file.readlines()

print(Nameslist)
file.close()
#-------------------------------------------------------------------------
with open ('Names.txt','r') as file:
    for line in file.readlines():
        print(line)

file.close()