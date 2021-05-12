# IMC = peso / (altura(m) , altura(m))

def imc(p, a):
    r = p / (a * a)
    return r


p = float(input('\nDigite o seu peso: '))
a = float(input('Digite a sua altura (em m): '))

imc(p, a)
print(f'O seu IMC é: {imc(p, a):.2f}\n')