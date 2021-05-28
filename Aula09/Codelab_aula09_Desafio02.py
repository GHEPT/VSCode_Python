# Desafio2
# Faça um script que peça ao usuário o número de matérias da escola, ou seja, um inteiro positivo
# Em seguida, ele vai digitando o valor de cada nota, de cada matéria e isso será armazenado numa lista. Ao final,seu script deverá fornecer a média geral do aluno.

a = int(input('Digite a quantidade de matérias você tem na escola: '))
materias = a 
notas = []
for i in range(1, materias+1):
    b = float(input(f'Insira sua nota na matéria {i}: '))
    notas.append(b)
    media = sum(notas) / materias
print(f'A média das {materias} matérias é {media}')
