MarketView

Dashboard web para análise do mercado imobiliário, desenvolvido como projeto acadêmico utilizando Python, Flask e PostgreSQL.

* Objetivo

O MarketView foi desenvolvido com o objetivo de permitir a análise de indicadores do mercado imobiliário por meio de uma interface intuitiva e moderna. A aplicação possibilita a consulta de imóveis por cidade, bairro e tipo de operação, apresentando informações estatísticas e gráficas para apoiar a tomada de decisão.

* Funcionalidades

- Consulta de imóveis por cidade, bairro e operação.
- Filtro dinâmico de bairros conforme a cidade selecionada.
- Cálculo do preço médio dos imóveis.
- Cálculo do preço médio por metro quadrado.
- Quantidade de imóveis encontrados.
- Gráfico de distribuição dos valores dos imóveis.
- Gráfico de tendência dos preços.
- Tabela dinâmica com os imóveis filtrados.
- Interface responsiva com tema escuro.

* Tecnologias Utilizadas

## Backend
- Python 3
- Flask
- PostgreSQL
- Psycopg2

## Frontend
- HTML5
- CSS3
- JavaScript
- Chart.js

## Banco de Dados
- PostgreSQL
- Neon Database

## Hospedagem
- GitHub
- Render

* Estrutura do Projeto

backend/
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── conexao.py
├── consultas.py
└── requirements.txt

A aplicação encontra-se publicada no Render:
https://marketview-3em0.onrender.com
Autor: Douglas Rodrigues
