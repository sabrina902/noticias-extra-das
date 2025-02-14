# 📌 Notícias Extração com Flet e MySQL

Este projeto extrai notícias do site G1, armazena em um banco de dados MySQL e exibe na interface gráfica utilizando Flet.

## 🚀 Como rodar o projeto

### 1️⃣ Pré-requisitos
Antes de começar, certifique-se de ter os seguintes programas instalados:
- Python 3.8+
- MySQL Server
- Pip (gerenciador de pacotes do Python)

### 2️⃣ Configuração do Banco de Dados
1. Acesse seu MySQL e crie um banco de dados:
   ```sql
   CREATE DATABASE noticias_db_sabrina;
   ```
2. No arquivo `banco.py`, configure as credenciais do MySQL:
   ```python
   db_config = {
       "host": "localhost",
       "user": "root",
       "password": "",
       "database": "noticias_db_sabrina"
   }
   ```

### 3️⃣ Instalação das Dependências
No terminal, execute:
```sh
pip install -r requirements.txt
```
Caso não tenha um arquivo `requirements.txt`, instale manualmente:
```sh
pip install requests beautifulsoup4 mysql-connector-python flet
```

### 4️⃣ Rodando o Projeto
Execute o seguinte comando no terminal:
```sh
python main.py
```
Isso criará a tabela no banco de dados (se ainda não existir) e abrirá a interface gráfica com as últimas notícias extraídas.

## 📂 Estrutura do Projeto
```
noticias_extracao/
│── main.py        # Interface com Flet
│── banco.py       # Gerenciamento do banco de dados
│── extracao.py    # Extração de notícias do G1
│── README.md      # Documentação do projeto
```

## 🛠️ Tecnologias Utilizadas
- **Python**: Linguagem principal
- **MySQL**: Banco de dados para armazenar as notícias
- **Flet**: Framework para a interface gráfica
- **BeautifulSoup**: Biblioteca para scraping de dados

## ✨ Funcionalidades
✅ Extração de notícias do site G1
✅ Armazenamento das notícias no banco de dados MySQL
✅ Interface gráfica para exibição das notícias
✅ Atualização manual das notícias

