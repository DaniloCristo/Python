#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 00:09:32 2018

@author: danilo
"""

def menorPagamento(saldo):
    '''
    saldo: divida no cartão de creditos
    retorno: um valor que pagaria a divida em 12 meses
    '''
    # valor pra checar um pagamento aproximado
    epsilon = 0.01
    #juros anual
    juros = 0.2
    high = (saldo * (1 + juros/12) ** 12) / 12
    low = saldo  / 12
    guess = (high + low) / 2
    while True:
        meses = 12
        sTemp = saldo
        while meses > 0:
            resto = sTemp - guess
            meses -= 1
            sTemp = resto + (resto * juros/12)
        #procurando por valor aproximado    
        if abs(sTemp) >= epsilon:
            if sTemp > epsilon:
                low = guess
            elif sTemp < epsilon:
                high = guess
            guess = (high + low) / 2
        else:
            break
    return "Pagamento minimo: {0} ".format(round(guess ,2))

print(menorPagamento(320000))        