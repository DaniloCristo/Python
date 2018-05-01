#função que retorna True se a palavra passada não conter a letra "e"
def has_no_e(word):
	return not "e" in word

#função que vai imprimir todas as palavras do arquivo sem a letra "e"
def only_no_e(file):
	#variaveis que vão contar a quantidade total de palavras e a quantidade de palavras sem "e"
	no_e = 0
	all_words = 0
	for line in file:
		words = line.strip()
		all_words += 1
		if has_no_e(words):
			no_e += 1
			print(words)
	#porcentagem de palavras sem "e"		
	porcento = (no_e * 100) / all_words
	print("A quantidade de palavras no arquivo é de: {0}".format(all_words))
	print("A quantidade de palavras sem a letra 'e' no arquivo é de: {0}".format(no_e))
	print("A porcentagem de palavras sem a letra 'e' no arquivo é de: {0:.2f}%".format(porcento))

file = open("words.txt")
only_no_e(file)				