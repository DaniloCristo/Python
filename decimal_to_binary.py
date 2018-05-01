def decimalToBinary(x):
	result = ""
	m = x
	while True:
		#vou multiplicar a parte decimal até que ela seja 0 e pegar a parte inteira da multiplicação  
		# para formar a representação binaria do numero
		m = m * 2
		m_inteiro = int(m)
		m_decimal = m - m_inteiro
		result = result + str(m_inteiro)
		m = m_decimal
		if m_decimal == 0:
			break
	#retornando o resultado
	return "O valor binario aproximado de {0} é : 0.{1}".format(x,result)

#recebendo o input entre 0 e 1
x = float(input("Digite um numero entre 0 e 1: "))
while True:
	if x >= 0 and x < 1:
		break
	else:
		x = float(input("Digite um numero entre 0 e 1: "))

resultado = decimalToBinary(x)
print(resultado)						