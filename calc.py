#função de soma
def somar(x,y):
	return x + y

#função de subtração
def sub(x,y):
	return																																																																																																																	 x - y	
#função de multiplicação
def multi(x,y):
	return x * y
#função de divisão
def div(x,y):
	return x / y
#função que seleciona qual operação vai ser realizada
def calcular(n1,n2,operacao):
	if(operacao == 1):
		print(somar(n1,n2))
	elif(operacao == 2):
		print(sub(n1,n2))
	elif(operacao == 3):
		print(multi(n1,n2))
	elif(operacao == 4):
		print(div(n1,n2))
					
#recebendo os valores
n1 = float(input("Digite um numero: "));
operacao = int(input("Somar (1) Subtrair (2) multiplicar (3) Dividir (4) Digite -1 para sair: "));
if(operacao == -1):
	exit();
n2 = float(input("Digite outro numero: "));
	
#chamando a função e passando os valores
calcular(n1,n2,operacao)
