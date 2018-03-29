#Função que calcula a media
def calcMedia(n1,n2):
	return (n1 + n2 ) / 2

#Função que existe o resultado
def resultado(n1,n2,nome):
	media = calcMedia(n1,n2)
	return "O aluno {0} Tirou de primeira nota {1} e de segunda nota {2} e obteve uma média de {3}".format(nome,n1,n2,media)

# pegando os valores
nome = input("Qual nome do aluno: ");
n1 = float(input("Digite a primeira nota do aluno: "))
n2 = float(input("Digite a segunda nota do aluno: "))

#imprimindo o resultado
print(resultado(n1,n2,nome));		
