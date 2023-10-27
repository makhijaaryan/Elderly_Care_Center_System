# pip install flask
# pip install flask-login
# pip install flask-sqlalchemy
# pip install python-dotenv

from website import create_app

# imgs, js, css in static folder


app=create_app()

if __name__=='__main__':
    app.run(debug=True)