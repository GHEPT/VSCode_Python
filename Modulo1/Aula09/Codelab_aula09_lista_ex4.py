# 4
# Faça um algoritmo que imprima 10 vezes a frase:“Go Blue”.

def so_vai():
    import time
    frase = 'Não sabe mais o que fazer para se tornar um(a) verdadeiro(a) Dev?'
    for i in frase:
        print(i, end='')
        time.sleep(0.06)
    print(f'\n')
    time.sleep(1.5)
    for i in range(1, 10+1):
        g = 'Go BLUE!'
        print(g)
        time.sleep(1)


so_vai()
