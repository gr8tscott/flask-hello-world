# Forked and Editted by: Matthew Scott
# Purpose: test, create, edit and view a database and its tables
# Usage: visit base url of 'https://lab10-cspb3308.onrender.com/' to get started then go through the routes one at a time as they appear on this page.

import psycopg2
from flask import Flask
app = Flask(__name__)

# https://lab10-cspb3308.onrender.com/

@app.route('/')
def hello_world():
    return 'Hello World from Matthew Scott in 3308!'

# Test connection to database
@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://lab10db_5bt0_user:tudWW9fgv87ywhuPtDWBk9n1v29NtLrs@dpg-co48tckf7o1s738q1bj0-a/lab10db_5bt0")
    conn.close()
    return "Database Connection Successful"

#Create table in database
@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgres://lab10db_5bt0_user:tudWW9fgv87ywhuPtDWBk9n1v29NtLrs@dpg-co48tckf7o1s738q1bj0-a/lab10db_5bt0")
    cur = conn.cursor()
    
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"

# Insert data into table
@app.route('/db_insert')
def inserting():
    conn = psycopg2.connect("postgres://lab10db_5bt0_user:tudWW9fgv87ywhuPtDWBk9n1v29NtLrs@dpg-co48tckf7o1s738q1bj0-a/lab10db_5bt0")
    cur = conn.cursor()
    
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Populated"

# Query all of the data from the database and return the information in a table
@app.route('/db_select')
def selecting():
    conn = psycopg2.connect("postgres://lab10db_5bt0_user:tudWW9fgv87ywhuPtDWBk9n1v29NtLrs@dpg-co48tckf7o1s738q1bj0-a/lab10db_5bt0")
    cur = conn.cursor()
    
    cur.execute('''
        SELECT * FROM Basketball;
        ''')
    records = cur.fetchall()
    conn.close()
    
    output = "<table>"
    for record in records:
        output += "<tr>"
        for value in record:
            output += "<td>{}</td>".format(value)
        output += "</tr>"
    output += "</table>"
    return output

# Drop table from database
@app.route('/db_drop')
def dropping():
    conn = psycopg2.connect("postgres://lab10db_5bt0_user:tudWW9fgv87ywhuPtDWBk9n1v29NtLrs@dpg-co48tckf7o1s738q1bj0-a/lab10db_5bt0")
    cur = conn.cursor()
    
    cur.execute('''
        DROP TABLE Basketball;
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Dropped"