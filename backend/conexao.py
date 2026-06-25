import psycopg2

def conectar():

    try:
        conexao = psycopg2.connect(
            host="ep-royal-thunder-acob01h8.sa-east-1.aws.neon.tech",
            database="neondb",
            user="neondb_owner",
            password="npg_RECMjH6qX2Ik",
            sslmode="require"
        )

        print("Conexão realizada com sucesso!")
        return conexao

    except Exception as erro:
        print("Erro ao conectar:")
        print(erro)
        return None