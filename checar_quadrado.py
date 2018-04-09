#função que recebe um numero
def checar(n1):
    counter = 0
    #enquanto o counter elevado a segunda potencia for menor que o numero recebido
    while counter ** 2 < n1:
        #interando o counter
        counter += 1
    # se o counter elevado ao quadrado for maior, não é um quadrado perfeito 
    if counter ** 2 > n1:
        print("{0} Não é um quadrado perfeito".format(n1))
    else:
        print("Seu quadrado perfeito é: {0}".format(counter))

#teste
x = int(input("Digite o numero que deseja descobrir sua raiz quadrada: "))
checar(x)        