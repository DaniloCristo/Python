def kmToM(km):
	#convertendo km para metros
	m = km * 1000;
	return "{} metros".format(m);

def mToKm(m):
	#convertendo metros para km
	km = m / 1000;	
	return "{} Km".format(km);

#Decisão de qual tipo de conversão fazer
print("Se deseja converter de Km para Metros digite 1");
print("Se deseja converter de Metros para Km digite 2");
escolha = int(input());	

#verificando a posição escolhida
if escolha == 1:
	km = int(input("Digite o valor em Km que deseja converter: "));
	print(kmToM(km));

elif escolha == 2:
	m = int(input("Digite o valor em Metros que deseja converter: "));
	print(mToKm(m));

else:
	print("Valor inválido");		