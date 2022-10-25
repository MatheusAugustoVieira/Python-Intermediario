# Biblioteca para acesso MySQL
import mysql.connector

print('{:=^40}'.format('\033[1;34mLOGIN phpMyAdmin\033[m'))
# Interface para a coleta de informações para o login do usuário no phpMyAdmin.
print("\033[1;34m-\033[m" * 50)
host = input("\033[1;32mDigite o host que você deseja conectar! >>> \033[m")
user = input("\033[1;34mDigite o seu login! >>> \033[m")
passwd = input("\033[1;32mDigite a sua senha! >>> \033[m")
database = input("\033[1;34mQual a base de dados que você deseja acessar? >>> \033[m")
print("\033[1;34m-\033[m" * 50)
print()
# Aqui o host, user, passwd(senha), database, do phpMyAdmin são previamente declaradas antes de passarem pelo while.

'''host = "167.99.252.245"
user = "BES_E5"
passwd = "unscaraae"
database = "BES_E5"'''

var = 0  # O Var é para adicionar a variável
add = "S"  # O add é para o menu iniciar

# O conector é a função que conecta o usuário na base de dados com base nas informações previamente levantadas
conector = mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)
# O cursor é a função que irá coletar os comandos a serem passados para a base de dados.
cursor = conector.cursor()
# Depois, o usuário adiciona variáveis na tabela, e um valor inicial para cada variável
print('{:=^40}'.format('\033[1;34mTABELAS\033[m'))
while (add == "S"):
    # Menu de seleção
    add = input(
        "\033[1;32mO que voce deseja realizar ? \033[m\n "
        "\033[1;32mCriar uma nova tabela              digite : 1 \033[m\n "
        "\033[1;32mDeletar TODA Tabela                digite : 2 \033[m\n "
        "\033[1;32mDar Update na Tabela               digite : 3 \033[m\n "
        "\033[1;32mDeletar toda variável da Tabela    digite : 4 \033[m\n "
        "\033[1;32mAdicionar uma nova variável?       digite : 5 \033[m\n \t ")
    if (add == "1"):
        nomeDaTabela = input(
             "\033[1;35mQual o nome da tabela que você quer criar? >>> \033[m") ## o usuario cria a tabela com nome a sua escolha
        cursor.execute("CREATE TABLE " + nomeDaTabela + " (ID INT AUTO_INCREMENT PRIMARY KEY);")

        var = var + 1
        variavelNome = input(
            "Digite o nome da " + str(var) + "a. variável? >>> ")  # o usario adciona o nome da variavel
        variavelTipo = input(
            "Digite o tipo da " + str(var) + "a. variável? >>> ")  # o usario adciona o tipo da variavel
        variavelValor = input("Digite o valor inicial da " + str(
            var) + "a. variável? (para variáveis string, não se esqueçam das aspas simples '') >>> ")  # o usario adciona o valor da variavel
        cursor.execute("ALTER TABLE " + nomeDaTabela + " ADD " + variavelNome + " " + variavelTipo + ";")
        cursor.execute("INSERT INTO " + nomeDaTabela + " (" + variavelNome + ") VALUES(" + variavelValor + ");")

        break

    if (add == "2"):  # o usario escolhe a opção de deletar toda a tabela
        nomeDaTabela = input(
            "\033[1;35mQual o nome da tabela que você quer DELETAR? >>> \033[m")
        cursor.execute("DROP TABLE " + nomeDaTabela)

        break

    if (add == "3"):  # o usario escolhe a opção dar update da tabela
        nomeDaTabela = input("\033[1;32mQual o nome da tabela que você quer alterar? >>> \033[m")
        coluna = input("\033[1;34mQual o nome da coluna que voce quer alterar ? \033[m")
        variavelNome1 = input("\033[1;32mQual nova a variável voce quer inserir?(para variáveis string,"
                              " não se esqueçam das aspas simples '')\033[m")
        variavelNome2 = input("\033[1;34mQual variável voce quer alterar?(para variáveis string,"
                              " não se esqueçam das aspas simples '')\033[m")
        cursor.execute(
            " UPDATE " + nomeDaTabela + " SET " + coluna + " = " + variavelNome1 + " WHERE " + coluna + " = " + variavelNome2)
        # O usuário escolhe a opção de deletar a tabela
    if (add == "4"):  # o usario escolhe a opção de deletar a tabela
        nomeDaTabela = input("\033[1;32mQual o nome da tabela que você quer alterar? >>> \033[m")
        variavelNome1 = input("\033[1;31mQual linha deseja remover? (Como escrever: Nome = 'Ricardo')>\033[m")

        cursor.execute(" DELETE FROM " + nomeDaTabela + " WHERE " + variavelNome1 + ";")

    if (add == "5"):  # o usario escolhe a opção de alterar a tabela
        nomeDaTabela = input("\033[1;32mQual o nome da tabela que você quer alterar? >>> \033[m")
        variavelNome1 = input("\033[1;31mVariável voce quer adicionar? \033[m")
        tipovariavel = input("\033[1;32m Tipo da Variável voce quer adicionar? \033[m")

        cursor.execute(" ALTER TABLE " + nomeDaTabela + " ADD " + variavelNome1 + " " + tipovariavel + ";")

    break

    # Finalmente, o conector faz um commit de todos os comandos SQL coletados pelo cursor e encerra a conexão com a base de dados...
conector.commit()
conector.close()
