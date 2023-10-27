# this file makes the folder into a python package

from dotenv import load_dotenv
import os

from flask import Flask

load_dotenv()

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']=os.getenv("SECRET_KEY")

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth/')



    return app

