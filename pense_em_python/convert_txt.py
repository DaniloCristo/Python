def convert(file):
    '''
    file: um arquivo de texto
    retorna: cada linha como um elemento de uma lista
    '''
    words = []
    for line in file:
        word = line.strip().lower()
        words.append(word)
    file.close()
    return words
  
def tirarSinais(words):
    '''
    words: lista de nomes
    retorna os nomes sem sinais nas letras
    '''
    new_words = words[:]
    for i in words:
        #i = i.lower()
        for j in i:
            if j == "í":
                new_words.remove(i)
                i = i.replace(j, "i")
                new_words.append(i)
            elif j == "á" or j == "â":
                new_words.remove(i)
                i = i.replace(j,"a")
                new_words.append(i)
            elif j == "é" or j == "ê":
                new_words.remove(i)
                i = i.replace(j,"e")
                new_words.append(i) 
            elif j == "ó" or j == "ô":
                new_words.remove(i)
                i = i.replace(j,"o")
                new_words.append(i)
            elif j == "ú":
                new_words.remove(i)
                i = i.replace(j,"u")
                new_words.append(i)                           
            elif j == "ç":
                new_words.remove(i)   
    return new_words

def tirar(words):
    new_words = words[:]
    for i in words:
        for j in i:
            if j == "ã":
                new_words.remove(i)   
    return new_words            
words = convert(open("nomes.txt"))
#print(words)
new_words = tirarSinais(words)
new_words2 = tirar(new_words)
print(new_words2)   
                
