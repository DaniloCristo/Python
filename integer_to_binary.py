def binary(x):
	b = []	
	while x > 0:
		b.append(x % 2)
		x = x // 2
	print(list(reversed(b)))	

x = int(input("Qual numero deseja converter para binario? "))
binary(x)

		
