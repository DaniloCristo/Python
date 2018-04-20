#usando binary search para achar um numero aleatorio entre o range 1-50 e exibir o numero de tentativas
def check_guess(x):
	initialValue = 1
	finalValue = 50
	#divisão inteira do guess
	guess = (initialValue + finalValue) // 2
	numGuess = 1
	#caso o x seja algum dos extremos
	if initialValue == x:
		print("Numero de tentativas para chegar ao resultado {0}".format(numGuess))
		return initialValue
	elif finalValue == x:
		print("Numero de tentativas para chegar ao resultado {0}".format(numGuess))
		return finalValue

	if guess != x:
		while True:
			if guess > x:
				finalValue = guess
			else:
				initialValue = guess	
			numGuess += 1
			guess = (initialValue + finalValue) // 2
			#sair do loop caso ache o valor
			if guess == x:
				break;
	print("Numero de tentativas para chegar ao resultado {0}".format(numGuess))
	return guess



#gerando numero aleatorio
from random import randint
x = randint(1,50)
#x = 45
resultado = check_guess(x)
print(resultado)						