def binary(x):
	if x < 0:
		#tratar caso o x seja negativo	
		is_neg = True
		x = abs(x)
	else:
		is_neg = False

	result = ''	
		
	if x == 0:	
		result = '0'
	
	while x > 0:
		#acumulando result sempre adicionando o resultado a esquerda
		result = str(x % 2) + result
		x = x // 2	
	if is_neg:
		#se o x for negativo atribuir o sinal negativo a result
		result = '-' + result
	return result		

#user input
x = int(input("Qual numero deseja converter para binario? "))
r = binary(x)
print(r)
		
