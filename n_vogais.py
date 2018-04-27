def numero_vogais(s):
	#numero de vogais
	nv = 0
	for letter in s:
		#verficiar cada letra da string possa ser uma vogal
	    if letter == "A" or letter == 'a'  or letter == 'E'  or letter == 'e'  or letter == 'I'  or letter == 'i'  or letter == 'O'  or letter == 'o'  or letter == 'U'  or letter == 'u':
	        nv += 1
	    
	return "O numero de vogais na string é: {0}".format(nv)

s = input("Digite uma string e veja quantas vogais contem nela: ")
result = numero_vogais(s)	   
print(result)