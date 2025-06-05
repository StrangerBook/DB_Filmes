import mysql.connector
import os

# Estabelece a conexão com o banco de dados MySQL
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="223399",
    database="filme",
)

# Classe para armazenar temporariamente informações de um filme alterado
class FilmeAlterado:
    def __init__(self, nome, sinopse):
        self.nome = nome
        self.sinopse = sinopse
        self.true = None  # Flag que indica se um filme foi alterado nesta sessão

add_completo = False  # Flag que indica se um filme foi adicionado
filme_alterado = FilmeAlterado(" ", " ")

cursor = conexao.cursor()

# Loop principal do menu
while True:
    os.system('cls')

    opc = input("\n--------------------------------\nBanco de dados de filmes\n 1 - Adicionar filme\n 2 - Ver filmes\n 3 - Alterar filme\n 4 - Deletar filme\n 5 - Sair\n")

    # --------------------- ADICIONAR FILME ---------------------
    if opc == "1":
        ficar = 1
        while ficar == 1:
            os.system('cls')

            # Mostra confirmação de adição de filme
            if add_completo == True:
                print(f"\n---------------------------------\n\nFilme {nome} adicionado!\n")
                add_completo = False

            opc2 = input("\n---------------------------------\n1 - Adicionar filme\n2 - Voltar\n")

            if opc2 == "1":
                os.system('cls')
                nome = input("\n---------------------------------\nEscolha o nome do filme: ")
                sinopse = input("Escreva a sinopse do filme: ")
                comf = input(f"Deseja mesmo adicionar o filme {nome}?\nDigite 1 para COMFIRMAR\nDigite qualquer outra coisa para NEGAR\n")

                if comf == "1":
                    # Insere o novo filme no banco de dados
                    comando = f'INSERT INTO filmes (nome, sinopse) VALUES ("{nome}", "{sinopse}")'
                    cursor.execute(comando)
                    conexao.commit()
                    add_completo = True

            if opc2 == "2":
                ficar = 0

    # --------------------- VISUALIZAR FILMES ---------------------
    if opc == "2":
        os.system('cls')
        ficar = 1
        while ficar == 1:
            opc2 = input("\n---------------------------------\n 1 - Ver todos\n 2 - Pesquisar por nome\n 3 - Pesquisar por id\n 4 - Voltar\n")

            # Exibe todos os filmes
            if opc2 == "1":
                os.system('cls')
                comando = 'SELECT * FROM filmes ORDER BY id'
                cursor.execute(comando)
                resultado = cursor.fetchall()

                print("\n\n---------------------------------\n-- id - nome - sinopse --")
                for i in resultado:
                    print(f"\n{i[0]} - {i[1]} \n{i[2]}")

            # Pesquisa filme por nome
            if opc2 == "2":
                os.system('cls')
                pesq = input("\n---------------------------------\nDigite o nome: ")
                comando = f'SELECT * FROM filmes WHERE nome = "{pesq}"'
                cursor.execute(comando)
                resultado = cursor.fetchall()

                if resultado:
                    print(f"\n{resultado[0][0]} - {resultado[0][1]} \n{resultado[0][2]}")
                else:
                    print("\nNada encontrado")

            # Pesquisa filme por ID
            if opc2 == "3":
                os.system('cls')
                pesq = input("\n---------------------------------\nDigite o id: ")
                comando = f'SELECT * FROM filmes WHERE id = "{pesq}"'
                cursor.execute(comando)
                resultado = cursor.fetchall()

                if resultado:
                    print(f"\n{resultado[0][0]} - {resultado[0][1]} \n{resultado[0][2]}")
                else:
                    print("\nNada encontrado")

            if opc2 == "4":
                ficar = 0

    # --------------------- ALTERAR FILME ---------------------
    if opc == "3":
        ficar = 1
        while ficar == 1:
            os.system('cls')

            # Mostra o último filme alterado na sessão
            if filme_alterado.true == True:
                print(f"\n---------------------------------\nÚltimo filme alterado nesta sessão: {filme_alterado.nome}")

            opc2 = input("\n---------------------------------\n 1 - Alterar por id\n 2 - Alterar por nome\n 3 - Voltar\n")

            # Alterar por ID
            if opc2 == "1":
                os.system('cls')
                alt = input("\n---------------------------------\nDigite o id do filme que deseja alterar: ")
                comando = f'SELECT * FROM filmes WHERE id = "{alt}"'
                cursor.execute(comando)
                resultado = cursor.fetchall()

                if resultado:
                    print(f"\nNome: {resultado[0][1]}\nSinopse: {resultado[0][2]}")
                    comf1 = input(f"\nDeseja seguir com esse filme?\nDigite 1 para COMFIRMAR\nDigite qualquer outra coisa para NEGAR\n")

                    if comf1 == "1":
                        nome_novo = input("Digite o novo nome: ")
                        sinopse_novo = input("Digite a nova sinopse:\n")
                        comando = f'UPDATE filmes SET nome = "{nome_novo}", sinopse = "{sinopse_novo}" WHERE id = "{alt}"'
                        cursor.execute(comando)
                        conexao.commit()

                        filme_alterado.nome = nome_novo
                        filme_alterado.sinopse = sinopse_novo
                        filme_alterado.true = True

                else:
                    print("\nNada encontrado")

            # Alterar por nome
            if opc2 == "2":
                os.system('cls')
                alt = input("\n---------------------------------\nDigite o nome do filme que deseja alterar: ")
                comando = f'SELECT * FROM filmes WHERE nome = "{alt}"'
                cursor.execute(comando)
                resultado = cursor.fetchall()

                if resultado:
                    print(f"\nNome: {resultado[0][1]}\nSinopse: {resultado[0][2]}")
                    comf1 = input(f"\nDeseja seguir com esse filme?\nDigite 1 para COMFIRMAR\nDigite qualquer outra coisa para NEGAR\n")

                    if comf1 == "1":
                        nome_novo = input("Digite o novo nome: ")
                        sinopse_novo = input("Digite a nova sinopse:\n")
                        comando = f'UPDATE filmes SET nome = "{nome_novo}", sinopse = "{sinopse_novo}" WHERE nome = "{alt}"'
                        cursor.execute(comando)
                        conexao.commit()

                        filme_alterado.nome = nome_novo
                        filme_alterado.sinopse = sinopse_novo
                        filme_alterado.true = True

                else:
                    print("\nNada encontrado")

            if opc2 == "3":
                ficar = 0

    # --------------------- DELETAR FILME ---------------------
    if opc == "4":
        delet_comf = False
        ficar = 1
        while ficar == 1:
            os.system('cls')

            # Mensagem de confirmação após deletar
            if delet_comf == True:
                print(f"Filme {delet_nome} deletado com sucesso!")
                delet_comf = False

            opc2 = input("\n---------------------------------\n 1 - Deletar filme por id\n 2 - Voltar\n")

            if opc2 == "1":
                os.system('cls')
                delet = input("\n---------------------------------\nDigite o id do filme que deseja deletar: ")
                comando = f'SELECT * FROM filmes WHERE id = "{delet}"'
                cursor.execute(comando)
                resultado = cursor.fetchall()

                if resultado:
                    delet_nome = resultado[0][1]
                    comf = input(f"\nDeseja mesmo deletar {delet_nome}?\n\nInformações: \n{resultado[0][0]} - {resultado[0][1]} \n{resultado[0][2]}\n\nDigite 1 para COMFIRMAR\nDigite qualquer outra coisa para NEGAR\n")

                    if comf == "1":
                        comando = f'DELETE FROM filmes WHERE id = "{delet}"'
                        cursor.execute(comando)
                        conexao.commit()
                        delet_comf = True

                else:
                    input("Filme não encontrado\nDigite qualquer coisa para voltar\n")

            if opc2 == "2":
                ficar = 0

    # --------------------- SAIR DO PROGRAMA ---------------------
    if opc == "5":
        os.system('cls')
        print("Fechando...")
        break

# Encerra cursor e conexão com o banco de dados
cursor.close()
conexao.close()
