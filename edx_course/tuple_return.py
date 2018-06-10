def oddTuple(aTuple):
    '''
    aTuple: uma tupla
    retorna: uma tupla apenas com os idices não impares
    '''
    #retornando a tupla do primeiro indice e pulando de dois em dois até o fim
    return aTuple[0::2]


#output esperado -> (1,3,5,7)
print(oddTuple((1,2,3,4,5,6,7,8)))