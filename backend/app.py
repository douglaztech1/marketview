from flask import Flask, render_template, jsonify, request

from consultas import (
    listar_cidades,
    listar_bairros_por_cidade,
    analise_bairro,
    distribuicao_valores,
    tendencia_precos,
    listar_imoveis_filtrados
)

app = Flask(__name__)


@app.route("/")
def inicio():
    cidades = listar_cidades()
    return render_template("index.html", cidades=cidades)


@app.route("/bairros/<int:id_cidade>")
def bairros(id_cidade):
    bairros = listar_bairros_por_cidade(id_cidade)

    lista_bairros = []

    for bairro in bairros:
        lista_bairros.append({
            "id_bairro": bairro[0],
            "nome": bairro[1]
        })

    return jsonify(lista_bairros)


@app.route("/consultar", methods=["POST"])
def consultar():
    dados = request.get_json()

    cidade = dados["cidade"]
    bairro = dados["bairro"]
    operacao = dados["operacao"]
    id_bairro = dados["id_bairro"]

    resultado = analise_bairro(cidade, bairro, operacao)
    distribuicao = distribuicao_valores(id_bairro, operacao)
    tendencia = tendencia_precos(id_bairro, operacao)
    imoveis = listar_imoveis_filtrados(id_bairro, operacao)

    lista_distribuicao = []

    for item in distribuicao:
        lista_distribuicao.append({
            "faixa": item[0],
            "quantidade": item[1]
        })

    lista_tendencia = []

    for item in tendencia:
        lista_tendencia.append({
            "mes": item[0],
            "preco_medio": float(item[1])
        })

    lista_imoveis = []

    for imovel in imoveis:
        lista_imoveis.append({
            "id_imovel": imovel[0],
            "operacao": imovel[1],
            "valor": float(imovel[2]),
            "area_m2": float(imovel[3]),
            "data_anuncio": imovel[4].strftime("%d/%m/%Y")
        })

    return jsonify({
        "quantidade": resultado[0],
        "preco_medio": float(resultado[1]),
        "preco_medio_m2": float(resultado[2]),
        "distribuicao": lista_distribuicao,
        "tendencia": lista_tendencia,
        "imoveis": lista_imoveis
    })


if __name__ == "__main__":
    app.run(debug=True)