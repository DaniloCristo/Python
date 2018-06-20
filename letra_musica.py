
def convert_file():
	file = open("letra_musica.txt","r")
	s = ""
	l1 = []

	'''
	file: um arquivo txt
	s: uma string onde vai ser armazenada toda a string
	l1: uma lista onde sera convertida a string, onde cada caractere representara um elemento
	retorna: l1
	'''

	for line in file:
		word = line.strip()
		s += word
	l1 = list(s.lower())
	file.close()
	return l1
	

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

#recebendo a lista com a letra da musica
l1 = convert_file()
#recebendo o dicionario
d = counting_letters(l1)
print(d)
