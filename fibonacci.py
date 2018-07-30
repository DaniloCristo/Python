#função recursiva para a sequencia de fibonacci
def fib(n):
	#caso n seja menor que 1
	if n <= 1:
		return 0
	elif n == 2 :
		return 1
	else:
		#usando a recursividade para achar o valor correspondente a posição desejada
		return fib(n-1) + fib(n-2)

#input do usuario
pos = int(input("Qual posição da sequencia de Fibonacci deseja encontrar? "))
print(fib(pos))				