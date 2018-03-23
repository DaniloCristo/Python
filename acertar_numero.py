from random import randint
#gerando um numero aleatorio
n = randint(0,9)
# função que verifica se o palpite esta correto
def verificarPalpite():
	#pegando o palpite
	x = int(input("Digite um palpite entre 0 e 9: "))
	#numero de tentativas até acertar
	tentativas = 1;
	# loop até o palpite ser o numero gerado
	while(x != n):
		tentativas += 1
		print("Você errou, tente novamente");
		x = int(input("Digite um palpite ente 0 e 9: "));

	print("Parabéns, você acertou e precisou de {} tentativa(s)".format(tentativas))	

verificarPalpite()
