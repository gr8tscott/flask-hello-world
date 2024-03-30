import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Matthew Scott in 3308!'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgres://lab10db_5bt0_user:tudWW9fgv87ywhuPtDWBk9n1v29NtLrs@dpg-co48tckf7o1s738q1bj0-a/lab10db_5bt0")
    conn.close()
    return "Database Connection Successful"
