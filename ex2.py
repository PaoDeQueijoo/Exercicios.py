# Variáveis para receber valores
sabor = ''
valor = 0
acumulador = 0
tamanho = ''
sabornome = 'Açaí' if sabor == 'CP' else 'Cupuaçu'

def validacao (): # Validação de sabor e tamanho, caso dê errado o programa encerra
    global sabor, valor, acumulador, tamanho, sabornome

    while True:
        sabor = input('\nEntre com o sabor desejado (CP/AC): ').upper()

        if sabor not in ['CP','AC']:
            print('Sabor inválido. Tente novamente')
            continue
        else: 
            break

    while True: 
        tamanho = input('Entre com o tamanho desejado (P/M/G): ').upper()

        if (sabor == 'CP'): # Cupuaçu
            if (tamanho == 'P'): # Tamanho P
                valor = 9
                acumulador = valor + acumulador 
                print(f'Você pediu um {sabornome} no tamanho {tamanho}: R$ {valor:.2f}')
            elif (tamanho == 'M'): # Tamanho M
                valor = 14
                acumulador = valor + acumulador
                print(f'Você pediu um {sabornome} no tamanho {tamanho}: R$ {valor:.2f}')
            elif (tamanho == 'G'): # Tamanho G
                valor = 18
                acumulador = valor + acumulador 
                print(f'Você pediu um {sabornome} no tamanho {tamanho}: R$ {valor:.2f}')
            else: 
                print('Tamanho inválido. Tente novamente.')
                return validacao()  
                
        if (sabor == 'AC'): # Açaí
            if (tamanho == 'P'): # Tamanho P
                valor = 11
                acumulador = valor + acumulador 
                print(f'Você pediu um {sabornome} no tamanho {tamanho}: R$ {valor:.2f}')
            elif (tamanho == 'M'): # Tamanho M
                valor = 16
                acumulador = valor + acumulador 
                print(f'Você pediu um {sabornome} no tamanho {tamanho}: R$ {valor:.2f}')
            elif (tamanho == 'G'): # Tamanho G
                valor = 20
                acumulador = valor + acumulador 
                print(f'Você pediu um {sabornome} no tamanho {tamanho}: R$ {valor:.2f}')
            else: 
                print('Tamanho inválido. Tente novamente.')
                return validacao()
        break

# Mensagem de boas vindas com meu nome
print('Bem-vindo à Açaíteria da Maria Elisa')

print('-'*21+'Cardápio'+'-'*21)
print('-'*50)
print('-'*3 + '|', ' Tamanho ', '|', ' Cupuaçu (CP) ', '|', ' Açaí (AC) ','|' + 3*'-')
print('-'*3 + '|', '    P    ', '|', '  R$',' 9.00    ', '|', ' R$ 11.00  ','|' + 3*'-')
print('-'*3 + '|', '    M    ', '|', '  R$','14.00    ', '|', ' R$ 16.00  ','|' + 3*'-')
print('-'*3 + '|', '    G    ', '|', '  R$','18.00    ', '|', ' R$ 20.00  ','|' + 3*'-')
print('-'*50)

validacao()

# Adicional
while True:
    adicional = input('\nDeseja mais alguma coisa? (S/N) ').upper()

    if (adicional == 'S'):
        validacao()
    elif (adicional == 'N'):
        print(f'\nO valor total a ser pago: R$ {acumulador:.2f}')
        break
    else:
        print('Resposta inválida. Tente novamente.\n')
        continue
