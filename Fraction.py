class Fraction(object):
	#inicializador
	def __init__(self,numerador,denominador):
		self.numerador = numerador
		self.denominador = denominador

	#metodos acessores e modificadores
	def get_numerador(self):
		return self.numerador
	def get_denominador(self):
		return self.denominador

	def set_numerador(self,numerador):
		self.numerador = numerador			
	def set_denominador(self,denominador):
		self.denominador = denominador

	def __eq__(self,other):
		#comparar se uma instancia da fração é igual a outra
		#return self.get_numerador() == other.get_numerador() and self.get_denominador() == other.get_denominador()
		return self.converter() == other.converter()
	def __mul__(self,other):
		'''
		self,other: instancias de frações
		retorna: uma outra instancia com a multiplicação das instancias passadas
		'''
		new_numerador = self.get_numerador() * other.get_numerador()
		new_denominador = self.get_denominador() * other.get_denominador()
		#retornando a nova instancia
		return Fraction(new_numerador,new_denominador)

	def __truediv__(self,other):
		'''
		self,other: instancias de Frações
		retorna: a divisão das frações passadas
		'''
		new_numerador = self.get_numerador() * other.get_denominador()
		new_denominador = self.get_denominador() * other.get_numerador()
		return Fraction(new_numerador,new_denominador)
	def __floordiv__(self,other):
		'''
		divisão inteira de duas instancias de frações
		'''
		return (self.get_numerador() / self.get_denominador()) // (other.get_numerador() / other.get_denominador())
	
	def __add__(self,other):
		'''
		self,other: instancias de frações
		retorna: a soma das frações
		'''
		new_numerador = (self.get_numerador() * other.get_denominador()) + (self.get_denominador() * other.get_numerador())
		new_denominador = self.get_denominador() * other.get_denominador()
		return Fraction(new_numerador,new_denominador)

	def __sub__(self,other):
		'''
		self,other: instancias de Frações
		retorna: uma nova instancia com a subtração das instancias anteriores
		'''
		new_numerador = (self.get_numerador() * other.get_denominador()) - (self.get_denominador() * other.get_numerador())
		new_denominador = self.get_denominador() * other.get_denominador()
		return Fraction(new_numerador,new_denominador)
	
	def converter(self):
		'''
		retorna o valor flutuante da fração
		'''
		return round(self.get_numerador() / self.get_denominador(),2)

	def __lt__(self,other):
		'''
		retorna True se self for uma fração maior que other e False caso contrario
		'''
		return self.converter() < other.converter()	
	def __str__(self):
		#imprimir a fração na tela na forma de -> numerador/denominador
		return "{}/{}".format(self.get_numerador(),self.get_denominador())


f1 = Fraction(4,6)
f2 = Fraction(2,3)
f3 = Fraction(5,10)
f4 = Fraction(1,2)
f5 = f2 + f3
print(f3 == f4)			
