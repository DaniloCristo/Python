def numero_vogais(s):
	#numero de vogais
	nv = 0
	vogal = ["a","e","i","o","u","A","E","I","O","U"]
	for letter in s:
		#verficiar cada letra da string possa ser uma vogal
		if letter in vogal:
			nv += 1  
	    
	return "O numero de vogais na string é: {0}".format(nv)

s = input("Digite uma string e veja quantas vogais contem nela: ")
result = numero_vogais(s)	   
print(result)