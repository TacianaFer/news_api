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
        SELECT TO_CHAR(publishedAt, 'YYYY') AS year,
       TO_CHAR(publishedAt, 'MM') AS month,
       TO_CHAR(publishedAt, 'DD') AS day,
       COUNT(*) AS count
        FROM news
        GROUP BY year, month, day;


    """

    with engine.connect() as con:
        result = con.execute(text(query)).fetchall()
    # result = engine.execute(query).fetchall()
    data = [{"year": row.year, "month": row.month, "day": row.day, "count": row.count} for row in result]
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
