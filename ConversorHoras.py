#receber minutos e converter para horas
def Converter(minutos):
	return int(minutos / 60);


minutos = int(input("Digite a quantidade de minutos: "));

horas = Converter(minutos);

print("A quantidade de minutos passada convertida para horas é de {} Horas".format(horas));
