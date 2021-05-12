def salario(a, b):
    b = b
    calc = a * b
    print(f'\nSalário base: R$ {calc:.2f}')
    if b > 40:
        h_extra = (b - 40)
        h_extra = (h_extra * (a * 0.5))
        print(f'Adicional H.E. 50% de: R$ {h_extra:.2f}')
        print(f'Total: R$ {calc + h_extra}')
    else:
        return 0


a = float(input('Quanto você recebe por hora trabalhada: '))
b = float(input('Horas trabalhadas na semana: '))

salario(a, b)
