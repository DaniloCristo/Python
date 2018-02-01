def ConverterMinutos(horas):
	return horas * 60;

#input da quantidade de horas

horas = int(input("Quantida de horas: "));

#chamando a função e passando a quantidade de horas
minutos = ConverterMinutos(horas);

print("A quantida de horas convertidas para minutos é de {} minutos ".format(minutos));	