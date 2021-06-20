# Escreva uma função que, dado um númeronotarepresentando a nota de um estudante, converte o valor de nota para um conceito (A, B, C, D, E e F).

""" Nota / Conceito
>= 9.0 / A  
>= 8.0 / B  
>= 7.0 / C
>= 6.0 / D
>= 5.0 / E
<= 4.0 / F """

def conceito():
    global n
    if n >= 9:
        n = print('A')
        return n
    elif n >= 8:
        n = print('B')
        return n
    elif n >= 7:
        n = print('C')
        return n
    elif n >= 6:
        n = print('D')
        return n
    elif n >= 5:
        n = print('E')
        return n
    elif n >= 0 and n <= 4:
        n = print('F')
        return n
    else:
        n = print('Você digitou uma nota inválida')
        return n


n = float(input('Digite sua nota: '))
conceito()
