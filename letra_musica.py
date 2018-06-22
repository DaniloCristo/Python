
def convert_file():
	file = open("letra_musica.txt","r")
	t1 = tuple()

	'''
	file: um arquivo txt
	t1: uma tuple onde sera adicionada a letra da musica onde cada index é um elemento
	retorna: t1
	
	'''

	for line in file:
		word = line.strip()
		t1 += tuple(word.lower())
	return t1	

def counting_letters(l1):
	'''
	l1: uma lista com a letra da musica separada por caractere
	retorna: um dicionario com a quantidade em que cada caractere apareceu na letra
	'''
	d = dict()
	for i in l1:
		if i in d:
			d[i] += 1
		else:
			d[i] = 1
	#removendo espaços e apostofro
	del[d["'"]]
	del[d[" "]]		
	return d

def most_frequencies(d):
	values = d.values()
	maior = max(values)
	words = []
	for word in d:
		if d[word] == maior:
			words.append(word)

	return (words,maior)		


#recebendo a lista com a letra da musica
t1 = convert_file()

#recebendo o dicionario
d = counting_letters(t1)
print(d)
#palavras que mais se repetem
freq = most_frequencies(d)
print(freq)
