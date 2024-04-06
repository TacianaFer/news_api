# # Projeto - Extração de Dados I
![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)

- Instituição: Ada Tech-  
- Curso: Engenharia de Dados
- Disciplina: Extração de Dados I 
- Professores: Patricia Bongiovanni Catandi
- Alunos: Jessica Hora ,Levy Marques, Lindy Macedo, Taciana Fernandes, Thiago Breves

## Contexto

O objetivo desse projeto é desenvolver e garantir um pipeline de dados confiavel e estável para empresas que Queiram se manter atualizada sobre os avanços mais recentes no mundo da tecnologia, identificar oportunidades para pesquisa e desenvolvimento  e acompanhar as tendências que podem influenciar estratégias de pesquisa e desenvolvimento. 
Pensando nisso, o time de dados apresentou uma proposta de desenvolvimento de um sistema que coleta, analisa e apresenta as últimas notícias relacionadas à Apple e também estuda o avanço da tecnologia nos últimos anos.

Sendo os Principais Objetivos da Aplicação:

1. **Consumo de dados com a News API**:

   - Implementar um mecanismo para consumir dados de notícias de fontes confiáveis e especializadas a partir da News API:
     [https://newsapi.org/](https://newsapi.org/)

2. **Definir Critérios de Relevância**:

   - Desenvolver critérios precisos de relevância para filtrar as notícias. Escolher 3 palavras-chave como critério de relevância.

3. **Cargas em Batches**:

   - Armazenar as notícias relevantes em um formato estruturado e facilmente acessível para consultas e análises posteriores. Essa carga deve acontecer 1 vez por hora. Se as notícias extraídas já tiverem sido armazenadas na carga anterior, o processo deve ignorar e não armazenar as notícias novamente, os dados carregados não podem ficar duplicados.

4. **Dados transformados para consulta do público final**:

   - A partir dos dados carregados, aplicar as seguintes transformações e armazenar o resultado para a consulta do público final:

     - 4.1 - Quantidade de notícias por ano, mês e dia de publicação;

     - 4.2 - Quantidade de notícias por fonte e autor;

     - 4.3 - Quantidade de aparições das 3 palavras-chave por ano, mês e dia de publicação definidas no item 2

   - Atualizar esses dados transformados 1 vez por dia.


4. **API para consulta do público final**:

    - Além das atividades principais, existe a necessidade de disponibilizar essas informações. Para isso crie uma API que contém as seguintes funções:

        - retornar todas as notícias
        - receber outras notícias que não foram mapeadas pela API original (opcional adicionar validação dos dados de entrada)
        - retornar a quantidade de notícias por ano, mês e dia de publicação do item 4.1
        - retornar a quantidade de notícias por fonte e autor do item 4.2
        - retornar a quantidade de aparições das 3 palavras-chave por ano, mês e dia de publicação  do item 4.3


6. **Deploy**
   - Deploy da API utilizando [Render](https://render.com/)


## Ferramentas Usadas
 Este projeto foi desenvolvido usando Python, Airflow, PostgreSQL, SQL.

## Organização do Projeto
```sh
NEWS_API/
│
├── news_api/                    # Código-fonte do projeto
│   ├── __init__.py              # Arquivo de inicialização do pacote
│   ├── main.ipynb               # Notebook principal do projeto
│   ├── news.db                  # Banco de dados SQLite para armazenar notícias
│   └── news.json                # Arquivo JSON com dados de notícias
│
├── tests/                       # Testes do projeto
│   ├── __init__.py              # Arquivo de inicialização dos testes
│   └── api.py                   # Testes para a API
│
├── poetry.lock                  # Arquivo gerado pelo Poetry para travar as dependências
├── pyproject.toml               # Arquivo de configuração do Poetry
├── README.md                    # Documentação do projeto
└── testar_conexao.ipynb         # Notebook para testar conexão com a API
```
