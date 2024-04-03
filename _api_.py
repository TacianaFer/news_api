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
    