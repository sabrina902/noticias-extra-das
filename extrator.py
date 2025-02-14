import requests
from bs4 import BeautifulSoup
import mysql.connector
from datetime import datetime
from banco import db_config

def buscar_e_salvar_noticias():
    url = "https://g1.globo.com/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        titulos = soup.find_all("a", class_="feed-post-link")

        conexao = mysql.connector.connect(**db_config)
        cursor = conexao.cursor()

        novas_noticias = []
        for titulo in titulos[:10]:
            titulo_texto = titulo.text.strip()
            cursor.execute("SELECT id FROM noticias WHERE titulo = %s", (titulo_texto,))
            cursor.fetchall()

            if not cursor.fetchone():
                data_extracao = datetime.now()
                sql = "INSERT INTO noticias (titulo, data_extracao) VALUES (%s, %s)"
                valores = (titulo_texto, data_extracao)
                cursor.execute(sql, valores)
                novas_noticias.append((titulo_texto, data_extracao))

        conexao.commit()
        conexao.close()
        return novas_noticias
    else:
        return []