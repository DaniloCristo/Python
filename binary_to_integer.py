#convertendo o input para uma lista de inteiros e reverter os indices
def converter_input(arr):
	new_arr = []
	#print(arr)
	for i in arr:
		#caso algum valor do input fuja de uma valor binario
		if i != '0' and i != '1':
			print("Seu input tem que ser binario!")
			#print(arr)
			return [0]
		new_arr.append(int(i))
	return list(reversed(new_arr))

#convertendo o numero binario pra decimal
def binary_decimal(arr):
	index = 0
	r = 0
	#convetendo para decimal, mais informações sobre como funciona aqui --> https://www.electronics-tutorials.ws/binary/bin_2.html
	while index < len(arr):
		r += arr[index] * 2 ** index
		index += 1
	#resultado
	return r

#recebendo o input e chamando as funçoes
arr = list(input("Digite o valor binario que deseja converter: "))
new_arr = converter_input(arr)
print(new_arr)
resultado = binary_decimal(new_arr)

print(resultado)				