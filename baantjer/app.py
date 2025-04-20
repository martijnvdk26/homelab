from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    search_query = request.form.get('search', '').strip()
    conn = get_db_connection()
    if search_query:
        like_query = f"%{search_query}%"
        books = conn.execute(
            '''SELECT * FROM boekenlijst 
               WHERE title LIKE ?
               OR CAST(number AS TEXT) LIKE ?
               OR CAST(isbn AS TEXT) LIKE ?
               OR CAST(year AS TEXT) LIKE ?''',
            (like_query, like_query, like_query, like_query)
        ).fetchall()
    else:
        books = conn.execute('SELECT * FROM boekenlijst').fetchall()
    conn.close()
    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)