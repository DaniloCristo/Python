#verificar se um determinado valor é divisivel por outro valor de input
#checar divisão exata
def checar(n,d):
	if n % d == 0:
		r = n / d
		print("O numero {0} é divisivel por {1}".format(n,d));
		print("E a divisão é: {0}".format(r))
	else:
		print("O numero {0} dividido por {1} não corresponde a uma divisão exata".format(n,d))	

checar(154,3)		