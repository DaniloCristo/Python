def convert(file):
    '''
    file: um arquivo de texto
    retorna: cada linha como um elemento de uma lista
    '''
    words = []
    for line in file:
        word = line.strip()
        words.append(word)
    file.close()
    return words
   