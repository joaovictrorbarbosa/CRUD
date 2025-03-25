import mysql.connector

#criando conexão entre banco de dados e nosso crud
conexao = mysql.connector.connect(
    host ='localhost' ,
    user= 'root',
    password='' ,
    database= 'db_crud',
)

#testando conexão com cursor
cursor = conexao.cursor()

#CREATE
nome_produto = str(input('DIGITE O NOME DO PRODUTO: '))
valor = float(input('DIGITE O VALOR DO PRODUTO (EM REAIS): '))
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
#quando editamos o banco de dados, com update ou delete, usamos:
conexao.commit()
# para ler o banco de dados

#READ
comando = f'SELECT * from vendas;'
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)

#UPDATE
idVendas = int(input('DIGITE O ID DO PRODUTO: '))
valor_novo = float(input('DIGITE QUAL O NOVO VALOR: '))
comando = f'UPDATE db_crud.vendas SET valor = {valor_novo} WHERE idVendas = {idVendas}'
cursor.execute(comando)
conexao.commit()

#DELETE
idVendas = int(input('DIGITE O ID DO PRODUTO QUE DESEJA EXCLUIR: '))
comando = f'DELETE FROM db_crud.vendas WHERE idVendas = "{idVendas}"'
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()