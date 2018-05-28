def criptoCifra(s):
	'''
		input : string
		output : string criptografada usando a cifra de cesar chave 1
	'''	
	s = s.lower()
	s2 = ""
	#iterando sobre a string
	for letter in s:
		code = ord(letter)
		#Criando a nova string com base no valor acii
		if code == 122:
			nextCode = 97
			s2 = s2 + chr(nextCode)
		elif code >= 97 and code < 122:
			nextCode = code + 1
			s2 = s2 + chr(nextCode)
		else:
			s2 = s2 + letter

	return s2.capitalize()

def descriptoCifra(s):
	'''
		input : string criptografada com chave 1 usando a cifra de cesar
		output : a string descriptografada
	'''
	s = s.lower()
	s2 = ""
	for letter in s:
		code = ord(letter)
		#criando a nova string com base no valor ascii
		if code == 97:
			nextCode = 122
			s2 = s2 + chr(nextCode)
		elif code > 97 and code <= 122:
			nextCode = code - 1
			s2 = s2 + chr(nextCode)
		else:
			s2 = s2 + letter	

	return s2.capitalize()			

#pegando os inputs
s = input("Digite uma string: ")
n = int(input("Digite 1 para criptografar e 2 para descriptografar: "))
if n == 1:
	print("Sua string criptogragafada...")
	print(criptoCifra(s))
elif n == 2:
	print("Sua string descriptografada...")
	print(descriptoCifra(s))
else:
	print("Valor invalido")			 				  