#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 13:03:17 2018

@author: danilo
"""

def mdc(x,y):
    '''
       input: dois valores inteiros
       output: maior divisor comum
    '''
    if x % y == 0:
        return y
    #dando os novos valores para x e y
    x,y = y,x % y
    return mdc(x,y)

print(mdc(24,16))
    