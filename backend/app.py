from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import flask_cors as cors
from flask_mysqldb import MySQL

import database as db

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

database = db.get_db(app)

@app.route('/')
def index():
    # return f'DB_PASSWORD = { app.config.get("DB_PASSWORD") }'

    return jsonify(db.getRecipes(database))

if __name__ == '__main__':
    app.run(debug=True)
