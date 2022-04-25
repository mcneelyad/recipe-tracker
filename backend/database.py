from flask_mysqldb import MySQL
import os


def init_db(app):
    app.config['MYSQL_HOST'] = os.environ.get('DB_HOST')
    app.config['MYSQL_USER'] = os.environ.get('DB_USER')
    app.config['MYSQL_PASSWORD'] = os.environ.get('DB_PASSWORD')
    app.config['MYSQL_DB'] = os.environ.get('DB')
    
    mysql = MySQL(app)
    
    return mysql

def get_db(app):
    return init_db(app)

def getRecipes(mysql):
    # data = [
    #     {
    #         "id": 1,
    #         "title": "Spaghetti",
    #     },
    #     {
    #         "id": 2,
    #         "title": "Lasagna",
    #     }
    # ]
    # return data
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM recipe")
    return cur.fetchall()