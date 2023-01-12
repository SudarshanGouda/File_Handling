'''
tell - tells, where is the file indicator (file position of last operation)
seek - seeks the indicator and changes its place to the value we want

JPG
'''
##################################### Tell ###############################
with open('Names.txt','r') as file:

    print(file.readline())
    print((file.tell()))
    print(file.readline())
    print((file.tell()))

##################################### Seek ###############################

with open('Names.txt','r') as file:

    print(file.readline())
    print((file.tell()))
    file.seek(33)
    print(file.readline())
    print((file.tell()))
