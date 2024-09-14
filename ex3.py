
def escolha_servico(): # Iniciar função para escolher
    global servico 
    print('Entre com o tipo de serviço desejado') 
    print('DIG - Digitalização')
    print('ICO - Impressão Colorida')
    print('IPB - Impressão Preto e Branco')
    print('FOT - Fotocópia')
    

    while True: # Validação
        servico = input('>>').upper()
        if servico not in ['DIG', 'ICO', 'IPB', 'FOT']:
            print('Escolha inválida, entre com o tipo de serviço novamente\n')
            print('\nEntre com o tipo de serviço desejado')
            print('DIG - Digitalização') 
            print('ICO - Impressão Colorida')
            print('IPB - Impressão Preto e Branco')
            print('FOT - Fotocópia')
            continue
        else:
            if (servico == 'DIG'):  # Digitalização
                servico = 1.10
                return 1.10
            elif (servico == 'ICO'): # Impressão Colorida
                servico = 1.00
                return 1.00
            elif (servico == 'IPB'): # Impressão Preto e Branco
                servico = 0.40
                return 0.40
            else: # Fotocópia
                servico = 0.20
                return 0.20
            
def num_pagina(): # Número de páginas e desconto
    global desconto, paginas
    desconto = 0 # Variável que recebe o valor do desconto
    paginas = 0 # Variável que recebe a quantidade de páginas
    while True:
        try:
            paginas = int(input('\nEntre com o número de páginas: '))
            if paginas >= 20000:
                print('Não aceitamos tantas páginas de uma vez.')
                print('Por favor, entre com o número de páginas novamente.')
                continue
            if paginas >= 20 and paginas < 200: # 15%
                desconto = paginas - ((paginas * 15) / 100)
                return desconto
            elif paginas >= 200 and paginas < 2000: # 20%
                desconto = paginas - ((paginas * 20) / 100)
                return desconto
            elif paginas >= 2000 and paginas < 20000: # 25%
                desconto = paginas - ((paginas * 25) / 100)
                return desconto
            else: # 0%
                desconto = paginas
                return desconto
        except ValueError:
            print('Opção inválida. Tente novamente.')
            continue

def servico_extra(): # Serviço adicional
    global extra    
    while True:
        try:
            print('\nDeseja adicionar algum serviço?')
            print('1 - Encadernação Simples   - R$ 15.00')
            print('2 - Encadernação Capa Dura - R$ 40.00')
            print('0 - Não desejo mais nada.')
            extra = int(input('>>'))
            if extra not in [1, 2, 0]:
                print('Opção inválida. Tente novamente')
            else:
                if (extra == 1): # Encadernação Simples
                    extra = 15
                    return 15
                elif (extra == 2): # Encadernação Capa Dura
                    extra = 40
                    return 40
                else: # Não quero mais nadinha de nada
                    extra = 0
                    return 0

        except ValueError:
            print('Opção inválida. Tente novamente.')
            continue

# Programa Principal

print('Bem-vindo a Copiadora da Maria Elisa\n')

valorservico = escolha_servico() # Variável que recebe uma função
numeropag = num_pagina() # Variável que recebe uma função
valor_extra = servico_extra() # Variável que recebe uma função
# Total
print(f'Total: R${((valorservico * numeropag) + valor_extra):.2f} (serviço: R${servico:.2f} * páginas: {desconto:.0f} + extra: R${extra} )')