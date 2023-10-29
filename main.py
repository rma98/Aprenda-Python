# comando print
print('Hello world')
# introdução às variáveis
nome = 'Robson'
print(f'{nome}')
# tipos de dados
idade, masculino, peso = 24, True, 68.9
print(f'{type(nome)}\n{type(idade)}\n{type(masculino)}\n{type(peso)}')
# como lidar com strings
frase = 'I love English'.upper().isupper() # .lower() .title() .isupper() is.lower()
print(frase)
# como selecionar letras dentro de uma frase
frase = 'Today is Sunday'.replace('Sunday', 'Monday')
print(f'{frase[0:6]}\nTamanho da frase: {len(frase)}')
# como lidar com números e operações aritméticas
inteiro, num_decimal, convertendo_texto_para_inteiro, convertendo_texto_para_float  = 50, 1.54, int('50'), float('52.46')
soma = 1 + 1
sub = 2 - 1
mult = 3 * 3
div = 10 / 2
div_int = 11 / 3
resto = 10 % 2
potencia = 7 ** 2
equacao = (10 + 5) * 2 ** 2 - 6 / 3
print(equacao)
# funcções matemáticas úteis nativas no Python
num_max, num_min, rentabilidade_ibovespa = max(4, 10), min(4, 10), round(0.45851545, 2)
print(f'Maior: {num_max}\nMenor: {num_min}\nRentabilidade: {rentabilidade_ibovespa}')
# como coletar dados do usuário
# nome = input('Seu nome: ')
# idade = int(input('Sua idade: '))
# altura = float(input('Sua altura: '))
# listas
nomes = ['Breno', 'Leandro', 'Lucas']
print(f'{nomes[0:2]}')
bancos = ['Itau', 'Bradesco', 'Banco do Brasil']
preco_acoes = [20, 15, 10]
bancos.append('Santander')
preco_acoes.append(30)
bancos.insert(1, 'Nubank')
bancos.remove( 'Santander')
preco_acoes.sort()
print(f'{bancos}\n{preco_acoes}')
# condicionais
dinheiro = int(input('Quanto dinheiro você tem para investir?'))
if dinheiro <= 20:
    print('Invista em você mesmo ')
elif dinheiro > 20 and dinheiro <= 1000:
    print('Comece a montar uma carteira de investimento')
else:
    print('Invista pesado e se aposente cedo')
# loops