#função que verifica o valor posicional
def valor(number):
	#checando se o numero recebido esta fora do range decidido de unidades, dezenas e centenas
	if number > 1000 or number < 0:
		#loop pra pegar um numero entre 0 e 999
		while(number>1000 or number < 0):
			number = int(input("Por favor digite um numero entre 0 e 999: "))

	#checando a qual valor posicional o numero number pertence		
	if number > 0 and number < 10:
		return "{0} esta na casa das unidades".format(number)
	elif number > 9 and number < 100:
		return "{0} esta na casa das dezenas".format(number)
	elif number > 99 and number < 1000:
		return "{0} esta na casa das centenas".format(number)
	elif number == 0:
		return "ZERO"

#recebendo um numeor inteiro do usuario
number = int(input("Digite um numero e descubra seu valor posicional: "))
result = valor(number)
print(result)		 				