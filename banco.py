import mysql.connector
from datetime import datetime

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "noticias_db_sabrina"
}

def criar_tabela():
    conexao = mysql.connector.connect(**db_config)
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS noticias (
            id INT AUTO_INCREMENT PRIMARY KEY,
            titulo TEXT NOT NULL,
            data_extracao DATETIME NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()

def carregar_noticias_do_banco():
    conexao = mysql.connector.connect(**db_config)
    cursor = conexao.cursor()
    cursor.execute("SELECT titulo, data_extracao FROM noticias ORDER BY data_extracao DESC LIMIT 10")
    noticias = cursor.fetchall()
    conexao.close()
    return noticias