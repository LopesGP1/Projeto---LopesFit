import mysql.connector
from mysql.connector import Error

def conectar_banco():
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='65323310',
            database='lopesfit_db',
            port = '3306'
        )
        if conexao.is_connected():
            print("Conexão com o banco de dados realizada com sucesso.")
            return conexao
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None


'''
Exemplo de uso para outro arquivo.
from db import conectar_banco

conexao = conectar_banco()

if conexao:
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM tb_usuario")
    resultados = cursor.fetchall()
    
    for linha in resultados:
        print(linha)

    conexao.close()

'''