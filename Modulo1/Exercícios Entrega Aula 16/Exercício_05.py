#05 - Refatore o exercício 2, para que uma função receba a frase, faça todo o tratamento necessário e retorne o resultado. Depois mostre na tela o resultado e a quantidade de letras foram retiradas da frase original.

def frase(): # FUNÇÃO
   cont = 0 # VARIÁVEL QUE VAI CONTAR AS VOGAIS DA FRASE DO USUÁRIO
   a = input('\nDigite uma frase: ').lower() # TRANSFORMA A FRASE INTEIRA EM CARACTERES MINÚSCULOS
   for i in a: # CONTADOR VAI PASSAR NA FRASE
      if i in 'aáàãeéêiíoôóuú': # E VAI VERIFICAR EM CADA RODADA SE ELE ENCONTRA ESSAS VOGAIS DA STRING
         cont += 1 # EM CADA RODADA QUE ENCONTRAR O CONTADOR VAI SOMAR 1
         a = a.replace(i, ' ') # E A FRASE ORIGINAL VAI TER A VOGALENCONTRADA SUBSTITUÍDA POR UM ESPAÇO 
   print()
   print('-=' * 30)
   print(f'A sua frase contém {cont} vogais')
   print('-=' * 60)
   print(f'Esta mesma frase sem vogais ficaria assim: [ {a} ]')
   print('-=' * 60)
   print(f'[ {cont} vogais ] foram retiradas da frase original')
   print('-=' * 60)


frase()
