'''extension is simply saying TEXT that is there only to
            make sure other programs know what is inside the
            type of file for example txt suggest there is text inside


EXCEPTION - an exceptional (unusal) situation in program that makes
            your program suddenly stop working'''

lst= list(map(int,input('Enter 3 number').strip().split()))[:3]

try:
    my_file= open('Try.txt','w')

    my_file.write('Hi I am Sudarshan Gouda\n')
    my_file.write('Working as a Data Scientist\n')
    my_file.write('with 6 years of experience\n')
    my_file.write(lst[3])

finally:
    my_file.close()