# -*- coding: utf-8 -*-
"""Ejercicio 1 y 3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KgV-5eZuKMFwOvSelTAKg4HBCepyVGAB
"""

# Duplicar los valores de elementos de una lista

my_list = [1, 2, 3, 4, 5]
doubled_list = list(map(lambda x: x * 2, my_list))
print(doubled_list)

# depende del valor: duplicar si es par, triplicar si es impar

lista1 =  [1, 2, 3, 4, 5, 6]
lista2 = list(map(lambda x: x * 2 if x % 2 == 0 else x * 3, lista1))

listapar = [x for x in lista2 if x % 2 == 0]
listaimpar = [x for x in lista2 if x % 2 != 0]

print("numeros pares: ",listapar)
print("numeros impares: ",listaimpar)