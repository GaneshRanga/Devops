from flask import Flask, render_template, request, redirect, url_for
import os
import psycopg2

app = Flask(__name__)

# Connect to PostgreSQL
pg_host = os.environ.get('PG_HOST', 'postgres-service')
pg_port = os.environ.get('PG_PORT', 5432)
pg_user = os.environ.get('PG_USER', 'granga401')
pg_password = os.environ.get('PG_PASSWORD', 'p@ssw0rd')
pg_database = os.environ.get('PG_DATABASE', 'psql_db')
pg_conn = psycopg2.connect(host=pg_host, port=pg_port, user=pg_user, password=pg_password, database=pg_database)
pg_cursor = pg_conn.cursor()
pg_conn.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        pg_cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        pg_conn.commit()
        return redirect(url_for('index'))

@app.route('/data')
def show_data():

    # Retrieve data from PostgreSQL
    pg_cursor.execute("SELECT * FROM users")
    users_pg = pg_cursor.fetchall()

    return render_template('data.html', users_pg=users_pg)

if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True)
