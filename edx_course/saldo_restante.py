def saldoRestante(saldo):
    '''
        b: valor numerico que representa uma divida no cartão de creditos
        retorno: após pagar por 12 meses o minimo da fatura o quanto ainda sobrara para pagar
        
    '''
    #pagamrnto minimo = 4 % do saldo
    pagamentoMinimo = 0.04
    #juros de 20% anuais
    juros = 0.2 / 12
    meses = 12
    while meses > 0:
        restante = saldo - (pagamentoMinimo * saldo)
        meses -= 1
        saldo = restante * (1 + juros)
    return "Após pagar o minimo do cartão de creidtos por 12 meses, você ainda deve: {0}".format(round(saldo,2))
print(saldoRestante(42))    