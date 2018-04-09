#encontrar a distancia entre dois pontos
def distance(x1,y1,x2,y2):
	#aplicando pitagoras para encontrar a distancia
	import math
	dsquare = (x2 - x1) ** 2 + (y2 - y1) ** 2
	return math.sqrt(dsquare)
print(distance(1,2,4,6))	