nome = input('Nome: ')

print(f'Olá {nome}, seja muito bem-vindo aos juros compostos! Aqui nos cuidamos da sua aposentadoria!')

dinheiro_inicial = int(input('Digite a quantidade de dinheiro inicial do investimento: '))
tempo = int(input('Digite quantos anos você deixará o dinheiro invetido: '))
taxa = float(input('Digite, em decimal, qual a taxa anual de retorno do seu investimento: '))

montante = dinheiro_inicial * (1 + taxa) ** tempo
montante = round(montante, 2)
print(f'{"-"*70}')
print(f'Parabéns {nome}! Ao final do período você terá R${montante}!')