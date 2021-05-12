# recebe data e entrega mes por extenso

def retorna_mes():
    mes_ext = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    mes_ext = mes_ext[mes_ref]
    return mes_ext


data = input('Digite uma data aleatória no formato XX/XX/XXXX: ')
mes_ref = int(data[3:5]) - 1
print(retorna_mes())
