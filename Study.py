def function(n):
    if (n ==1):
        return 1
    else:
        return function(n -1) + 2*n

x= function(6)
print x


def functionS(n):
    j = 1
    terms = []
    for i in range (1,n):
        j += 2*n
        terms.append(j)
    return terms

x = functionS(6)
print x
