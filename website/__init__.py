# this file makes the folder into a python package

# pip install flask
# pip install flask-login
# pip install flask-sqlalchemy
# pip install python-dotenv

from dotenv import load_dotenv
import os

from flask import Flask

load_dotenv()

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']=os.getenv("SECRET_KEY")

    return app

