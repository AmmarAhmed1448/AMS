from flask_mysqldb import MySQL
import os
from dotenv import load_dotenv
mysql = MySQL()


load_dotenv()

def init_db(app):
    app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
    app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
    app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
    app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
    # app.config['MYSQL_CURSORCLASS'] = 'DictCursor'  # Optional: To get results as a dictionary
    
    # Initialize the MySQL connection with the app
    mysql.init_app(app)


    try:
        with app.app_context():
            cur = mysql.connection.cursor()
            cur.execute("SELECT 1")
            cur.close()
    except Exception as e:
        raise Exception(f"Database connection failed: {e}")