
def sumAll(s):
    '''
    s : uma string com numeros separados por virgula
    retorno: a soma desses numeros
    '''
    #separando cada item por index do array quando encontrar uma virgula
    arr = s.split(",")
    total = 0
    for n in arr:
        total += float(n)
    return total

print(sumAll("1.23,2.34,3.45,4"))    
    