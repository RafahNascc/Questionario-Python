#Importar blibliotecas
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='template')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db=SQLAlchemy(app)

from controllers import * 
from models import *

with app.app_context():
    
    if __name__ == '__main__':
        db.create_all()
        app.run(debug=True)