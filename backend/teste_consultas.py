from consultas import quantidade_imoveis_por_cidade


dados = quantidade_imoveis_por_cidade()

for item in dados:
    print(item)

    from consultas import analise_bairro(cidade, bairro, operacao)


dados = analise_bairro(cidade, bairro, operacao)

for item in dados:
    print(item)