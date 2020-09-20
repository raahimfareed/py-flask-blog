from flask import Flask, redirect, render_template, url_for, flash, request, session
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path("./config") / ".env"

load_dotenv(dotenv_path=env_path)


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{os.getenv('POSTGRES_USER')}:" \
                                        f"{os.getenv('POSTGRES_PASSWORD')}@" \
                                        f"{os.getenv('POSTGRES_HOST')}:" \
                                        f"{os.getenv('POSTGRES_PORT')}/" \
                                        f"{os.getenv('POSTGRES_DB')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    display_name = db.Column(db.String(200))
    username = db.Column(db.String(200), unique=True)
    email = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(255))
    date_joined = db.Column(db.Date)


@app.route('/')
@app.route('/index')
def index():
    return render_template('pages/main/index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        return 'Hello World!'
    else:
        return render_template('pages/main/login.html')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        return 'Hello World!'
    else:
        return render_template('pages/main/signup.html')


if __name__ == "__main__":
    db.create_all()
    app.run()
