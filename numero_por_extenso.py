d = {"0":"Zero","1":"Um","2":"Dois","3":"Três","4":"Quatro","5":"Cinco","6":"Seis","7":"Sete","8":"Oito","9":"Nove","10":"Dez","11":"Onze","12":"Doze","13":"Treze","14":"Quatorze","15":"Quinze","16":"Desesseis","17":"Desessete","18":"Dezoito","19":"Dezenove","20":"Vinte","30":"Trinta","40":"Quarenta","50":"Cinquenta","60":"Sessenta","70":"Setenta","80":"Oitenta","90":"Noventa","100":"Cento","200":"Duzentos","300":"Trezentos","400":"Quatrocentos","500":"Quinhentos","600":"Seiscentos","700":"Setecentos","800":"Oitocentos","900":"Novecentos","1000":"Mil","2000":"Dois mil","3000":"Três mil","4000":"Quatro mil","5000":"Cinco mil","6000":"Seis mil","7000":"Sete mil","8000":"Oito mil","9000":"Nove mil","10000":"Dez Mil"}

def numero(n_string):
	'''
		n_string: string com um numero entre 0 e 100
		retorna: o numero por extenso
	'''
	#verificando se o valor passado é menor que 20
	if int(n_string) <= 20:
		return "Numero por extenso: {0}".format(d[n_string])
	elif n_string == "100":
		#Problema do 100 sozinho ser CEM e se tiver dezenas e/ou unidades com ele ser CENTO
		return "Numero por extenso: Cem"	
	else:
		#dividinvo cada caractere
		lista_numero = list(n_string)
		lista_numero.reverse()
		for i in range(len(lista_numero)):
			lista_numero[i] = int(lista_numero[i]) * 10 ** i
		lista_numero.reverse()

	#novo array com cada posição em seu valor por extenso
	n_extenso = []
	for i in range(len(lista_numero)):
		#evitando que fique por ex: cento e setenta e zero
		if lista_numero[i] != 0:
			#print(a[i])
			if i < len(lista_numero) and lista_numero[i] == 10 and lista_numero[i + 1] != 0:
				#caso um dos valores seja entre 10 e 20
				#adicionar seu valor
				#para evitar ficar ex: cento e dez e tres
				n_extenso.extend([d[str(lista_numero[i] + lista_numero[i + 1])],"e"])
			elif lista_numero[i - 1] != 10:
				#apenas entra aqui caso o valor anterior não seja entre 10 e 20	
				n_extenso.extend([d[str(lista_numero[i])], "e"])
	#excluindo o ultimo "e" da lista
	n_extenso.pop()
	#retornando o n como string
	n_extenso = " ".join(n_extenso)		
	return "Numero por extenso: {0}".format(n_extenso)
#recebendo do usuario
n = input("Digite um numero entre 0 e 10999: ")
result = numero(n)

print(result)
