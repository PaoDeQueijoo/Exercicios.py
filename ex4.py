lista_livro = [] # Variável para armazenar livros
id_global = 0 # Variável para receber valores

def menu_principal(): # Menu principal
    global id_global
    while True:
        print('\n' + '-' * 50)
        print('-' * 17, 'MENU PRINCIPAL', 17 * '-')
        print('1 - Cadastrar Livro.')
        print('2 - Consultar Livro(s).')
        print('3 - Remover Livro.')
        print('4 - Sair.')
        try:
            selecionar = int(input('>> '))
            if selecionar not in [1, 2, 3, 4]:
                print('Número inválido, tente novamente.')
                continue
            if selecionar == 1: # Cadastrar livros
                cadastrar_livro(id_global + 1)
            elif selecionar == 2: # Consultar livros
                consultar_livro()
            elif selecionar == 3: # Remover livros
                remover_livro()
            elif selecionar == 4: # Encerrar programa
                print('Encerrando...')
                break
        except ValueError:
            print('Opção inválida, tente novamente.')
            continue

def cadastrar_livro(id): # Cadastrar livros
    global id_global, lista_livro
    id_global += 1
    print('\n' + '-' * 50)
    print('-' * 14, 'MENU CADASTRAR LIVRO', 14 * '-')

    print(f'Id do Livro: {id}')
    nome = input('Nome do livro: ')
    autor = input('Autor do livro: ').upper()
    editora = input('Editora do Livro: ')
    print('-' * 50)
    # Variável que armazena o livro cadastrado e é adicionada a outra variável do tipo lista
    livro = {"id": id, "nome": nome, "autor": autor, "editora": editora}
    lista_livro.append(livro)

def consultar_livro(): # Consultar livro
    while True:
        try:
            print('\n' + '-' * 50)
            print('-' * 16, 'CONSULTAR LIVRO', 17 * '-')
            print('1 - Consultar Todos.')
            print('2 - Consultar por Id.')
            print('3 - Consultar por Autor.')
            print('4 - Retornar ao Menu.')

            selecionar = int(input('>> '))
            if selecionar == 4: # Retornar ao menu
                break
            elif selecionar == 1: # Consultar todos os livros
                if not lista_livro:
                    print('Nenhum livro cadastrado...')
                else:
                    for livro in lista_livro:
                        print(f'ID do Livro: {livro["id"]}')
                        print(f'Nome: {livro["nome"]}')
                        print(f'Autor: {livro["autor"]}')
                        print(f'Editora: {livro["editora"]}\n')
                        continue
            elif selecionar == 2: # Consultar por id
                id_consulta = int(input('Digite o ID do livro desejado: '))
                livro_encontrado = False
                for livro in lista_livro:
                    if id_consulta == livro["id"]:
                        print(f'ID do Livro: {livro["id"]}')
                        print(f'Nome: {livro["nome"]}')
                        print(f'Autor: {livro["autor"]}')
                        print(f'Editora: {livro["editora"]}\n')
                        livro_encontrado = True
                        continue
                if not livro_encontrado:
                    print('Livro não encontrado...')
            elif selecionar == 3: # Consultar por autor
                autor_consulta = input('Digite o autor desejado: ').upper()
                autor_encontrado = False
                for livro in lista_livro:
                    if autor_consulta == livro["autor"]:
                        print('\n' + '-' * 50)
                        print(f'Livro: {livro["nome"]}')
                        print(f'ID: {livro["id"]}')
                        print(f'Autor: {livro["autor"]}')
                        print(f'Editora: {livro["editora"]}\n')
                        print('-' * 50)
                        autor_encontrado = True
                        continue
                if not autor_encontrado:
                    print('Nenhum livro encontrado para o autor informado...')
                    break
            else:
                print('Opção inválida, tente novamente.')
                break
        except ValueError:
            print('Opção inválida, tente novamente.')
            break

def remover_livro(): # Remover livro
    while True:
        try:
            print('\n' + '-' * 50)
            print('-' * 15, 'MENU REMOVER LIVRO', 15 * '-')
            id_remove = int(input('Digite o ID do livro que quer remover: '))
            livro_encontrado = False
            for livro in lista_livro:
                if livro["id"] == id_remove:
                    lista_livro.remove(livro)
                    print(f'Livro {livro["nome"]} removido.')
                    livro_encontrado = True
                    menu_principal()
            if not livro_encontrado:
                print('ID inválido. Tente novamente.')
            else:
                break
        except ValueError:
            print('Opção inválida, tente novamente.')
            break

# Programa Principal
print('Bem vindo à Livraria da Maria Elisa')
menu_principal()