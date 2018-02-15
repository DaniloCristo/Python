#classe
class Euclides:
	#construtor que recebe dois numeros com uma condição de serem maiores que 0
	def __init__(self,x = 0,y = 0):
		if x > 0:
			self.x = x

		if y > 0:
			self.y = y	

	#algoritmo que encontra o maior divisor comum, conhecido como o algoritmo de Euclides		
	def divisorComun(self):
		resto = self.x % self.y
		if resto == 0:
			return "O maior divisor comun é: {0}".format(self.y)		
		else:
			while resto != 0:
				self.x = self.y
				self.y = resto
				resto = self.x % self.y

				if(resto == 0):
					return "O maior divisor comun é: {0}".format(self.y)

#recebimento dos valores e instancia da classe
x = int(input("Digite o numerador positivo e maior que 0: "));
y = int(input("Digite o denominador positivo e maior que 0: "));

e = Euclides(x,y);

print(e.divisorComun());						