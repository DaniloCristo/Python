#Função recursiva que recebe um numero e o soma até o 0 ex: 6 + 5 + 4 + 3 + 2 + 1 = 21
def somar(n):
	if n < 0:
		return 0;
	return n + somar(n - 1)

#recebendo o input
n = int(input("Digite um numero para ter sua soma decrescente: "))
resultado = somar(n)
print("Resultado: {0}".format(resultado))		