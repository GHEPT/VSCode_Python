
import random

# 02
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: 

# A) Quantas vezes apareceu o valor 9. 
# B) Em que posição foi digitado o primeiro valor 3.

a = float(input('Digite um valor: '))
b = float(input('Digite um valor: '))
c = float(input('Digite um valor: '))
d = float(input('Digite um valor: '))

tupla = (a, b, c, d)

print(tupla.count(9))
print(tupla.index(3))
