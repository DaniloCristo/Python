def in_bisect(arr,s):
    '''
        arr: uma lista ordenada, s: valor alvo
        retorna: a posição do valor alvo na lista ou False caso não esteja la
    '''
    high = len(arr)
    low = 0
    guess = (high + low) // 2
    while arr[guess] != s:
        if arr[guess] > s:
            high = guess
        elif arr[guess] < s:
            low = guess
        
        #checando caso o valor passado não esteja dentro da lista
        if s > arr[guess] and s < arr[guess + 1]:
            return False
        
        guess = (high + low) // 2
    return "O indice em que o valor alvo se encontra é: {0}".format( guess)
    
#teste simples 
print(in_bisect(["a","b","c"],"b"))

#usando a função criada em outro arquivo
import convert_txt as c

file = open("../words.txt")
#guardar o resultado da lista em words
words = c.convert(file)    
file.close() 

#procurando o indice da palavra "abandon"
print(in_bisect(words,"abandon"))            
    