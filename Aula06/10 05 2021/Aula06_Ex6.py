# funcao converte numero recebido para o conceito

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

