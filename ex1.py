# Mensagem de boas-vindas com o nome
print('Bem-vindo a Loja da Maria Elisa')

# Variáveis que armazenam o valor do produto e a quantidade
valor = float(input('Valor do produto: '))
quantidade = int(input('Quantidade do produto: '))

# Variável que recebe o valor total/valor final
valort = valor * quantidade

desc1 = 0 / 100
desc2 = 4 / 100
desc3 = 7 / 100
desc4 = 11 / 100

# if, elif e else, aqui é calculado o valor com e sem desconto
if (valort <2500): # 0%
    print(f'Valor SEM desconto: R${valort:.2f}')

elif (valort < 6000): # 4%
    print(f'Valor SEM desconto: R${valort}0')
    print(f'Valor COM desconto: R${valort-(valort * desc2):.2f}')

elif (valort <10000): # 7%
    print(f'Valor SEM desconto: R${valort}0')
    print(f'Valor COM desconto: R${valort-(valort * desc3):.2f}')

else: # 11%
    print(f'Valor SEM desconto: R${valort}0')
    print(f'Valor COM desconto: R${valort-(valort * desc4):.2f}')