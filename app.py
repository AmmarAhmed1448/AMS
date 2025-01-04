from flask import Flask
from db import init_db

app = Flask(__name__)

# Initialize the MySQL connection
try:
    init_db(app)
    print("Database connection successful")
except Exception as e:
    print(f"Failed to initialize the database: {e}")


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/login")
def login():
    return "<p>Login</p>"


if __name__ == "__main__":
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"Failed to start the Flask app: {e}")