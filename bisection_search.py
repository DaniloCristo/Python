def b(l,n):
	'''
	l: lista ordenada
	n: valor a ser encontrado na lista
	'''
	#index minimo
	low = 0
	#index maximo
	high = len(l)
	#index no meio da lista
	guess = (high + low) // 2
	#caso o high -1(que é o ultimo index) for menor que target, valor nao se econtra na lista
	if l[high - 1] < n:
		return "Numero nao se encontra na lista"
	
	#enquanto o guess nao representar o numero target
	while l[guess] != n:
		#verificar se o numero presente no index guess é maior que o taget
		if l[guess] > n:
			high = guess
		elif l[guess] < n:
			#verificar se o numero presente no index guess é menor que o taget
			low = guess
		
		#caso entre aqui significa que a lista nao possuir o target procurado
		if l[guess] > n and l[guess - 1] < n:
			return "Numero não se encontra na lista"
		#guess no meio da lista
		guess = (high + low) // 2
	return "O numero {} esta no index {}".format(n,guess)

print(b([1,2,3,5,6,7,8,9,10],4))				