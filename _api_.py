import pandas as pd
from flask import Flask, jsonify
from sqlalchemy import create_engine, text

app = Flask(__name__)

engine = create_engine(
    "postgresql://ada:PR1gvstOECPAb8Yqat1OptlTPm2orbDC@dpg-co6a0ka0si5c73cck8d0-a.oregon-postgres.render.com/database_vx82"
)


# Contar as notícias por ano, mês e dia de publicação
@app.route("/count_by_date")
def count_by_date():
    query = """
        SELECT 
            date_part('year', cast(publishedat as date)) as ano_publicacao,
            date_part('month', cast(publishedat as date)) as mes_publicacao,
            date_part('day', cast(publishedat as date)) as dia_publicacao,
            count(*) as contagem_noticias
        from news
        group by ano_publicacao, mes_publicacao, dia_publicacao
    """

    with engine.connect() as con:
        result = con.execute(text(query)).fetchall()
    # result = engine.execute(query).fetchall()
    data = [
        {
            "ano_publicacao": row.ano_publicacao,
            "mes_publicacao": row.mes_publicacao,
            "dia_publicacao": row.dia_publicacao,
            "contagem_noticias": row.contagem_noticias,
        }
        for row in result
    ]
    return jsonify(data)


# Contar as notícias por fonte e autor
@app.route("/count_by_source_author")
def count_by_source_author():
    query = """
        SELECT source_name, author, COUNT(*) as count
        FROM news
        GROUP BY source_name, author
    """
    with engine.connect() as con:
        result = con.execute(text(query)).fetchall()
    data = [{"source_name": row.source_name, "author": row.author, "count": row.count} for row in result]
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)


    # receber outras noticias que não foram mapeadas pela APi original

@app.route("/add_news", methods=['POST'])
def add_news():
    try:
        news_data = request.get_json()
        print(news_data)

        query = f"""
            INSERT INTO news (source_name, author, title, description, url, url_to_image, published_at, content)
            VALUES ('{news_data['source_name']}', '{news_data['author']}', '{news_data['title']}', '{news_data['description']}', '{news_data['url']}', '{news_data['url_to_image']}', '{news_data['published_at']}', '{news_data['content']}')
        """
        print(query)

        with engine.connect() as con:
            con.execute(text(query))
            con.commit()
            return jsonify({"message": "Noticia adicionada com sucesso!"}), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

    if __name__ "__main__":
        app.run(debug=True)

