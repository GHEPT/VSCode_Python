# Exercício 6

# Um  professor,  muito  legal,  fez  3  provas  durante  um semestre,mas  só  vai  levar  em  conta  as duas notas mais altas para calcular a média. Faça  uma  aplicação  que  peça  o  valor  das  3  notas,  mostre  como  seria  a  média  com  essas  3 provas, a média com as 2 notas mais altas, bem como sua nota mais alta e sua nota mais baixa.

def notas(a, b, c):
    med = (a + b + c) / 3 
    med_altas = ((a + b + c) - (min(lista))) / 2
    lista = [a, b, c]
    min(lista)
    max(lista)
    print(f'A média das três notas seria: {med}')
    print(f'A média com as duas notas mais altas é: {med_altas}')
    print(f'A nota mais alta foi: {max(lista)}')
    print(f'Sua nota mais baixa foi: {min(lista)}')


a = float(input('Digite a nota 1: '))
b = float(input('Digite a nota 2: '))
c = float(input('Digite a nota 3: '))

notas(a, b, c)
