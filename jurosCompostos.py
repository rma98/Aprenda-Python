nome = input('Nome: ')

print(f'Olá {nome}, seja muito bem-vindo aos juros compostos! Aqui nos cuidamos da sua aposentadoria!')

dinheiro_inicial = int(input('Digite a quantidade de dinheiro inicial do investimento: '))
tempo_desejado = int(input('Digite quantos meses você deixará o dinheiro invetido: '))
taxa = float(input('Digite, em decimal, qual a taxa mensal de retorno do seu investimento: '))
aporte = float(input('Quanto você consegue aportar por mês: '))
salario_desejado = int(input('Digite o salário mensal que você quer receber ao se aposentar: '))

tempo_decorrido = 0

while tempo_decorrido < tempo_desejado:
    if tempo_decorrido == 0:
        montante = dinheiro_inicial * (1 + taxa) ** 1
        montante = round(montante, 2)
        tempo_decorrido += 1
    else:
        montante = (montante + aporte) * (1 + taxa) ** 1
        montante = round(montante, 2)
        tempo_decorrido += 1

print(f'{"-"*70}')
print(f'Parabéns {nome}! Ao final do período você terá R${montante}!')

salario_mensal = (montante * taxa)
salario_mensal = round(salario_mensal, 2)

if salario_mensal >= salario_desejado:
    print(f'Parabéns, você pode se aposentar! Seu salário mensal com esse montante é de R${salario_mensal}')
elif salario_mensal < salario_desejado:
    print(f'Infelizmente se aposentar não será possível. Com esse montante seu salário é de R${salario_mensal}')