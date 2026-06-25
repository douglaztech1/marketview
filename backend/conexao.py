import os
import psycopg2

def conectar():
    try:
        conexao = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            sslmode="require"
        )

        return conexao

    except Exception as erro:
        print("Erro ao conectar:")
        print(erro)
        return None