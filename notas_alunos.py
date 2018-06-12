from matplotlib import pyplot as plt
from matplotlib import style

style.use("ggplot")

def graficNotas(d):
	'''
	d : dicionario com o agrupamento de notas e suas respectivas frequencias
	retorna: um histograma usando o matplotlib
	'''
	plt.bar(d.keys(),d.values(),color="g")

	plt.title("Histograma das notas da sua sala")
	plt.ylabel("Quantidade")
	plt.xlabel("Notas")

	plt.show()


def histogram(notas):
	'''
	notas: uma lista com uma serie de notas de alunos entre 0-10
	retorna: um dicionario de chave e valor com ranges por exemplo: 0-3 e a quantidade de notas entre 0-3 na lista recebida
	'''

	d = dict()
	#exibindo notas minimas e maximas
	print("Nota máxima: {}".format(max(notas)))
	print("Nota minima: {}".format(min(notas)))

	#criando o dicionario de acordo com os valores da lista
	for i in notas:
		if i >= 0 and i <= 3:
			if "0-3" not in d:
				d["0-3"] = 1
			else:
				d["0-3"] += 1
		elif i >=4 and i <= 6:
			if "4-6" not in d:
				d["4-6"] = 1
			else:
			 	d["4-6"] += 1
		elif i >= 7 and i <= 9:
			if "7-9" not in d:
				d["7-9"] = 1
			else:
				d["7-9"] += 1
		elif i > 9 and i <= 10:
			if "9.1-10" not in d:
				d["9.1-10"] = 1
			else:
				d["9.1-10"] += 1
	return d


#recebendo as notas do usuario
notas = []
while True:
	value = float(input("Digite a do aluno: (caso tenha acabado digite -1) "))
	if value == -1:
		break
	elif value < -1 or value > 10:
		print("Valor digitado inválido, por favor digite um número entre 0-10")
	else:
		notas.append(value)

d = histogram(notas)

graficNotas(d)			