from flask import Flask, jsonify
import pandas as pd
from sqlalchemy import create_engine

app = Flask(__name__)

engine = create_engine('sqlite:///news_api/news.db')

# Contar as notícias por ano, mês e dia de publicação
@app.route('/count_by_date')
def count_by_date():
    query = """
        SELECT strftime('%Y', publishedAt) as year,
               strftime('%m', publishedAt) as month,
               strftime('%d', publishedAt) as day,
               COUNT(*) as count
        FROM news
        GROUP BY year, month, day
    """
    result = engine.execute(query).fetchall()
    data = [{"year": row.year, "month": row.month, "day": row.day, "count": row.count} for row in result]
    return jsonify(data)

# Contar as notícias por fonte e autor
@app.route('/count_by_source_author')
def count_by_source_author():
    query = """
        SELECT source, author, COUNT(*) as count
        FROM news
        GROUP BY source, author
    """
    result = engine.execute(query).fetchall()
    data = [{"source": row.source, "author": row.author, "count": row.count} for row in result]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

# Retornar todas a noticias
@app.route('/all_news')
def get_all_news():
    query = """
        SELECT *
        FROM news
    """
    result = motor.execute(query).fetchall()
    data = [{"title": row.title, "author": row.author, "publishedAt": row.publishedAt} for row in result]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

# Retornar as noticias por ID
@app.route('/news/<int:news_id>')
def get_news_by_id(news_id):
    if news_id in noticias_db:
        return jsonify(noticias_db[news_id])
    else:
        return jsonify({"error": "Notícia não encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True)
