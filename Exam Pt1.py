def string_match(a,b):
    variable = 0

    for i in range(len(a)):
        if (a[i:i+2] == b[i:i+2] and len(a[i:i+2]) == 2):
            variable +=1

    print variable


string_match('abc','abc')
string_match('xxcaaz','xxbaaz')
string_match('abc','axc')
