nome = input('Nome: ')

print(f'Olá {nome}, seja muito bem-vindo aos juros compostos! Aqui nos cuidamos da sua aposentadoria!')

dinheiro_inicial = int(input('Digite a quantidade de dinheiro inicial do investimento: '))
tempo = int(input('Digite quantos anos você deixará o dinheiro invetido: '))
taxa = float(input('Digite, em decimal, qual a taxa anual de retorno do seu investimento: '))
salario_desejado = int(input('Digite o salário mensal que você quer receber ao se aposentar: '))

montante = dinheiro_inicial * (1 + taxa) ** tempo
montante = round(montante, 2)

print(f'{"-"*70}')
print(f'Parabéns {nome}! Ao final do período você terá R${montante}!')

salario_mensal = (montante * taxa) / 12
salario_mensal = round(salario_mensal, 2)

if salario_mensal >= salario_desejado:
    print(f'Parabéns, você pode se aposentar! Seu salário mensal com esse montante é de R${salario_mensal}')
elif salario_mensal < salario_desejado:
    print(f'Infelizmente se aposentar não será possível. Com esse montante seu salário é de R${salario_mensal}')