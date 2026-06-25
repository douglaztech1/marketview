from conexao import conectar


def quantidade_imoveis_por_cidade():

    banco = conectar()

    if banco is None:
        print("Conexão falhou. Abortando consulta.")
        return []

    cursor = banco.cursor()

    sql = """
        SELECT 
            cidades.nome AS cidade,
            COUNT(imoveis.id_imovel) AS quantidade
        FROM cidades
        JOIN bairros
        ON cidades.id_cidade = bairros.id_cidade
        JOIN imoveis
        ON bairros.id_bairro = imoveis.id_bairro
        GROUP BY cidades.nome
        ORDER BY quantidade DESC;
    """

    cursor.execute(sql)

    resultado = cursor.fetchall()

    cursor.close()
    banco.close()

    return resultado

def analise_bairro(cidade, bairro, operacao):

    banco = conectar()

    if banco is None:
        return None

    cursor = banco.cursor()

    sql = """
        SELECT
            COUNT(imoveis.id_imovel),
            ROUND(AVG(imoveis.valor),2),
            ROUND(AVG(imoveis.valor / imoveis.area_m2),2)
        FROM imoveis
        JOIN bairros
        ON imoveis.id_bairro = bairros.id_bairro
        JOIN cidades
        ON bairros.id_cidade = cidades.id_cidade
        WHERE cidades.nome = %s
        AND bairros.nome = %s
        AND imoveis.operacao = %s;
    """

    valores = (cidade, bairro, operacao)

    cursor.execute(sql, valores)

    resultado = cursor.fetchone()

    cursor.close()
    banco.close()

    return resultado

def listar_cidades():
    banco = conectar()

    if banco is None:
        return []

    cursor = banco.cursor()

    sql = """
        SELECT id_cidade, nome
        FROM cidades
        ORDER BY nome;
    """

    cursor.execute(sql)
    resultado = cursor.fetchall()

    cursor.close()
    banco.close()

    return resultado


def listar_bairros_por_cidade(id_cidade):
    banco = conectar()

    if banco is None:
        return []

    cursor = banco.cursor()

    sql = """
        SELECT id_bairro, nome
        FROM bairros
        WHERE id_cidade = %s
        ORDER BY nome;
    """

    cursor.execute(sql, (id_cidade,))
    resultado = cursor.fetchall()

    cursor.close()
    banco.close()

    return resultado

def distribuicao_valores(id_bairro, operacao):

    banco = conectar()

    if banco is None:
        return []

    cursor = banco.cursor()

    sql = """
        SELECT
            CASE
                WHEN valor <= 500000 THEN 'Até 500 mil'
                WHEN valor <= 1000000 THEN '500 mil a 1 milhão'
                ELSE 'Acima de 1 milhão'
            END AS faixa_preco,
            COUNT(*) AS quantidade
        FROM imoveis
        WHERE id_bairro = %s
        AND operacao = %s
        GROUP BY faixa_preco
        ORDER BY faixa_preco;
    """

    cursor.execute(sql, (id_bairro, operacao))

    resultado = cursor.fetchall()

    cursor.close()
    banco.close()

    return resultado

def tendencia_precos(id_bairro, operacao):

    banco = conectar()

    if banco is None:
        return []

    cursor = banco.cursor()

    sql = """
        SELECT
            TO_CHAR(DATE_TRUNC('month', data_anuncio), 'MM/YYYY') AS mes,
            ROUND(AVG(valor), 2) AS preco_medio
        FROM imoveis
        WHERE id_bairro = %s
        AND operacao = %s
        GROUP BY DATE_TRUNC('month', data_anuncio)
        ORDER BY DATE_TRUNC('month', data_anuncio);
    """

    cursor.execute(sql, (id_bairro, operacao))

    resultado = cursor.fetchall()

    cursor.close()
    banco.close()

    return resultado

def listar_imoveis_filtrados(id_bairro, operacao):

    banco = conectar()

    if banco is None:
        return []

    cursor = banco.cursor()

    sql = """
        SELECT
            id_imovel,
            operacao,
            valor,
            area_m2,
            data_anuncio
        FROM imoveis
        WHERE id_bairro = %s
        AND operacao = %s
        ORDER BY valor DESC;
    """

    cursor.execute(sql, (id_bairro, operacao))

    resultado = cursor.fetchall()

    cursor.close()
    banco.close()

    return resultado