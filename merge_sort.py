def merge_sort(l):
	#caso tenha mais de um item, continuar quebrando ao meio
	if len(l) > 1:
		mid = len(l) // 2
		#cortar a lista recebida em duas metades
		esquerda = l[:mid]
		direita = l[mid:]

		merge_sort(esquerda)
		merge_sort(direita)

		#lista a esquerda
		e = 0
		
		#lista da direita
		d = 0

		#lista ordenada
		k = 0
		
		while e < len(esquerda) and d < len(direita):
			#compara as listas da direita e esquerda ja ordenadas
			if esquerda[e] < direita[d]:
				l[k] = esquerda[e]
				e += 1
			else:
				l[k] = direita[d]	
				d += 1
			k += 1

		while e < len(esquerda):
			#se sobrou itens na esquerda
			l[k] = esquerda[e]
			e += 1
			k += 1

		while d < len(direita):
			#se sobrou elementos na direita
			l[k] = direita[d]
			d += 1
			k += 1					
	#caso contrario, retorne, pois so um item esta ordenado	
	return l

print(merge_sort([9,2,1,7,6,4,-3]))
		