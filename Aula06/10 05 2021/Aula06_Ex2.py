def pos_neg(num):
    if num > 0:
        print('P')
    elif num < 0:
        print('N')
    else:
        print('0')


num = float(input('Digite um valor: '))
pos_neg(num)
