# Exercício Treino 2

# Escreva uma função que recebe dois números (a e b) como parâmetros e retorna True caso a soma dos dois seja maior que um terceiro parâmetro, chamado limite.

def numeros(a, b, limite):
    teste = a + b
    if teste > limite:
        print('True')


a = float(input('Digite um valor: '))
b = float(input('Digite outro valor: '))
limite = float(input('Digite um valor limite: '))

numeros(a, b, limite)
