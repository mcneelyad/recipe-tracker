from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_mysqldb import MySQL
import flask_cors as cors
import os

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['MYSQL_HOST'] = os.environ.get('DB_HOST')
app.config['MYSQL_USER'] = os.environ.get('DB_USER')
app.config['MYSQL_PASSWORD'] = os.environ.get('DB_PASSWORD')
app.config['MYSQL_DB'] = os.environ.get('DB')

database = MySQL(app)

@app.route('/')
def index():    
    return { 'message': 'Hello World!' }

@app.route('/recipes')
def get_recipes():
    cur = database.connection.cursor()
    cur.execute("SELECT * FROM recipe")
    row_headers=[ x[0] for x in cur.description ]
    result_data = cur.fetchall()
    recipes = []
    for result in result_data:
        recipes.append(dict(zip(row_headers,result)))
    return jsonify(recipes)

@app.route('/recipes/<int:id>')
def get_recipe_by_id(id):
    cur = database.connection.cursor()
    cur.execute("SELECT * FROM recipe WHERE id = %s", (id,))
    row_headers=[ x[0] for x in cur.description ]
    result_data = cur.fetchall()
    if len(result_data) == 0:
        return { 'message': 'Recipe not found' }
    recipes = []
    for result in result_data:
        recipes.append(dict(zip(row_headers,result)))
    print(recipes)
    return jsonify(recipes)

if __name__ == '__main__':
    app.run(debug=True)
