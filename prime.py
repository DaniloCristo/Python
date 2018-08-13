#usando generator
def genPrimes():
	#numeros anteriores
	previous = [1.5]
	#guess para o proximo numero primo
	proximo_primo = int(previous[-1]) + 1	
	previous.pop()
	while True:
		#condição para vê se o promo_primo é um primo 
		while not all(proximo_primo % n != 0 for n in previous):
			#tentar o proximo
			proximo_primo += 1
		yield proximo_primo
		previous.append(proximo_primo)	
				
						


foo = genPrimes()
'''
print(foo.__next__())
print(foo.__next__())
print(foo.__next__())
print(foo.__next__())'''

for i in range(100):
	#imprimir os 100 primeiros numeros primos
	print(foo.__next__())


