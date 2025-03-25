import mysql.connector
from CRUD.lib.sistema import *
from CRUD.lib.interface import *
from time import sleep

#criando conexão entre banco de dados e nosso crud
conexao = mysql.connector.connect(
    host ='localhost' ,
    user= 'root',
    password='' ,
    database= 'db_crud',
)

#testando conexão com cursor
cursor = conexao.cursor()

while True:
    resposta = menu(['Cadastrar Produtos', 'Listar produtos', 'Modificar produtos','Excluir produtos','sair do programa'])
    if resposta == 1: #CREATE
        cabecalho('NOVO CADASTRO')
        nome_produto = str(input('DIGITE O NOME DO PRODUTO: '))
        valor = float(input('DIGITE O VALOR DO PRODUTO (EM REAIS): '))
        comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
        cursor.execute(comando)
        conexao.commit()
    elif resposta == 2: #READ
        cabecalho('PRODUTOS CADASTRADOS:')
        comando = f'SELECT * from vendas;'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        print(resultado)
    elif resposta == 3: #UPDATE
        cabecalho('ALTERANDO PRODUTO:')
        idVendas = int(input('DIGITE O ID DO PRODUTO: '))
        valor_novo = float(input('DIGITE QUAL O NOVO VALOR: '))
        comando = f'UPDATE db_crud.vendas SET valor = {valor_novo} WHERE idVendas = {idVendas}'
        cursor.execute(comando)
        conexao.commit()
    elif resposta == 4: #DELETE
        idVendas = int(input('DIGITE O ID DO PRODUTO QUE DESEJA EXCLUIR: '))
        comando = f'DELETE FROM db_crud.vendas WHERE idVendas = "{idVendas}"'
        cursor.execute(comando)
        conexao.commit()
    else:
        print('Saindo do programa...')
        sleep (2)
        break

cursor.close()
conexao.close()