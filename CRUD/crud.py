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
nome_produto = "chocolate"
valor = 8
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
#quando editamos o banco de dados, com update ou delete, usamos:
conexao.commit()
# para ler o banco de dados
#resultado = cursor.fetchall()


cursor.close()
conexao.close()