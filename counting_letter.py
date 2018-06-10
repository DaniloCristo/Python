
def count(file):
    '''
        file: arquivo txt com uma palavra por linha
        retorna: um dicionario com quantas palavras começando com a letra a, b, c, d ... 
    '''
    d = dict()
    #iterando no arquivo
    for line in file:
        word = line.strip()
        if word[0] not in d:
            d[word[0]] = 1
        else:
            d[word[0]] += 1
    return d      

       
file = open("words.txt")
result = count(file)

file.close()

print(result)

