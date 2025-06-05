import mysql.connector
import os

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="223399",
    database="filme",
)

class FilmeAlterado:
    def __init__(self, nome, sinopse):
        self.nome = nome
        self.sinopse = sinopse
        self.true = None

add_completo = False
filme_alterado = FilmeAlterado(" ", " ")

cursor = conexao.cursor()

#menu
while True:
    
    os.system('cls')

    opc = input("\n--------------------------------\nBanco de dados de filmes\n 1 - Adicionar filme\n 2 - Ver filmes\n 3 - Alterar filme\n 4 - Deletar filme\n 5 - Sair\n")

    if opc == "1":
    #adicionar filme

        ficar = 1
        while ficar == 1:
        #menu de adição
            os.system('cls')

            if add_completo == True: #mostra o filme adicionado se foi adicionado algum
                print(f"\n---------------------------------\n\nFilme {nome} adicionado!\n")
                add_completo = False

            opc2 = input("\n---------------------------------\n1 - Adicionar filme\n2 - Voltar\n")

            if opc2 == "1":

                os.system('cls')
                nome = input("\n---------------------------------\nEscolha o nome do filme: ")
                sinopse = input("Escreva a sinopse do filme: ")
                comf = input(f"Deseja mesmo adicionar o filme {nome}?\n Digite 1 para COMFIRMAR\n Digite qualquer outra coisa para NEGAR\n")

                if comf == "1":
                    comando = f'INSERT INTO filmes (nome, sinopse) VALUES ("{nome}", "{sinopse}")'
                    cursor.execute(comando)
                    conexao.commit()

                    add_completo = True

            if opc2 == "2":
                ficar = 0
        
    if opc == "2":
        #menu de vistoria
        os.system('cls')
        ficar = 1
        while ficar == 1:
            
            opc2 = input("\n---------------------------------\n 1 - Ver todos\n 2 - Pesquisar por nome\n 3 - Pesquisar por id\n 4 - Voltar\n")

            if opc2 == "1":
                
                os.system('cls')
                comando = 'SELECT * FROM filmes ORDER BY id'
                cursor.execute(comando)
                resultado = cursor.fetchall()

                print("\n\n---------------------------------\n-- id - nome - sinopse --")

                for i in resultado:
                    print(f"\n{i[0]} - {i[1]} \n{i[2]}")
            
            if opc2 == "2":

                os.system('cls')
                pesq = input("\n---------------------------------\nDigite o nome: ")
                comando = f'SELECT * FROM filmes WHERE nome = "{pesq}"'
                cursor.execute(comando)
                resultado = cursor.fetchall()

                x = len(resultado)

                if x > 0:
                    print(f"\n{resultado[0][0]} - {resultado[0][1]} \n{resultado[0][2]}")
                else:
                    print("\nNada encontrado")
            
            if opc2 == "3":
                os.system('cls')
                pesq = input("\n---------------------------------\nDigite o id: ")
                comando = f'SELECT * FROM filmes WHERE id = "{pesq}"'
                cursor.execute(comando)
                resultado = cursor.fetchall()

                x = len(resultado)

                if x > 0:
                    print(f"\n{resultado[0][0]} - {resultado[0][1]} \n{resultado[0][2]}")
                else:
                    print("\nNada encontrado")
            
            if opc2 == "4":
                ficar = 0
            

    if opc == "3":
        #menu de alteração

        ficar = 1
        while ficar == 1:
            os.system('cls')

            if filme_alterado.true == True:
                print(f"\n---------------------------------\nUltimo filme alterado nessa sessão: {filme_alterado.nome}")

            opc2 = input("\n---------------------------------\n 1 - Alterar por id\n 2 - Alterar por nome\n 3 - Voltar\n")

            if opc2 == "1":
                os.system('cls')
                alt = input("\n---------------------------------\nDigite o id do filme que deseja alterar: ")

                comando = f'SELECT * FROM filmes WHERE id = "{alt}"'
                cursor.execute(comando)
                resultado = cursor.fetchall()

                x = len(resultado)

                if x > 0:
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

                        if filme_alterado.true != True:
                            filme_alterado.true = True

                else:
                    print("\nNada encontrado")
                

            if opc2 == "2":
                os.system('cls')
                alt = input("\n---------------------------------\nDigite o nome do filme que deseja alterar: ")

                comando = f'SELECT * FROM filmes WHERE nome = "{alt}"'
                cursor.execute(comando)
                resultado = cursor.fetchall()

                x = len(resultado)

                if x > 0:
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

                        if filme_alterado.true != True:
                            filme_alterado.true = True

                else:
                    print("\nNada encontrado")

            if opc2 == "3":
                ficar = 0

    if opc == "4":
        #menu de deletar
        delet_comf = False
        ficar = 1
        while ficar == 1:

            os.system('cls')

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

                x = len(resultado)

                if x > 0:
                    delet_nome = resultado[0][1]


                    comf = input(f"\nDeseja mesmo deletar {delet_nome}?\n\nInformações: \n{resultado[0][0]} - {resultado[0][1]} \n{resultado[0][2]}\n\n Digite 1 para COMFIRMAR\n Digite qualquer outra coisa para NEGAR\n")
                    
                    if comf == "1":
                        comando = f'DELETE FROM filmes WHERE id = "{delet}"'
                        cursor.execute(comando)
                        conexao.commit()

                        delet_comf = True
                
                else:
                    input("Filme não encontrado\nDigite qualquer coisa para voltar\n")

            if opc2 == "2":
                ficar = 0
        
        
    if opc == "5":
        os.system('cls')
        print("Fechando...")
        break

cursor.close()
conexao.close()