# -*- coding: utf-8 -*-
"""
@author: libra
"""

#Ejercicio de diagnostico 1

def sumar(n):
    return (n * (n+1))/ 2

n = int( input("Dame un numero: "))
suma = sumar(n)
print("La suma es: ",suma)

#Ejercicio diagnostico 2

vocales = ['a', 'e', 'i', 'o', 'u']

def buscador_vocales(palabra):
    palabra_tamaño = len(palabra)
    posicion_vocales = []
    for i in range(palabra_tamaño):
        caracter = palabra[i]
        siguiente_caracter = palabra[i+1] if i+1 < palabra_tamaño else None
        if (caracter in vocales) and not (siguiente_caracter in vocales):
            posicion_vocales.append(i)
        print(caracter)
        print(posicion_vocales)
    return posicion_vocales

def traduce_a_f(palabra):
    pos_vocales = buscador_vocales(palabra)
    pafalafabrafa = palabra
    posicion = 0
    for pos in pos_vocales:
        pafalafabrafa = pafalafabrafa[:pos+posicion+1] + 'f' + palabra[pos] + pafalafabrafa[pos+1+posicion:]
        posicion += 2
    return pafalafabrafa

texto = input("Ingrese su texto a traducir: ")

texto_en_f = traduce_a_f(texto)

print("Texto traducido en f: ", texto_en_f)
