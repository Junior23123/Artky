from email.policy import default
from enum import unique
import sys
from unicodedata import name
from xml.dom.minidom import Identified
import psycopg2
import psycopg2.extras
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from flask_login import (UserMixin, LoginManager,
                         login_user, login_required, current_user)
from flask import(Flask, jsonify,
                  redirect,
                  render_template,
                  abort,
                  request,
                  url_for,
                  flash,
                  session)
from sqlalchemy import null
import hashlib
from werkzeug.security import generate_password_hash, check_password_hash

database_name = 'artky'
database_path = 'postgresql://{}:{}@{}/{}'.format('postgres','carro', 'localhost:5432', database_name)

db = SQLAlchemy()


def setup_db(app, database_path = database_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    db.create_all()
    app.secret_key = 'cairocoders-ednalan'
class Register(UserMixin,db.Model):
    __tablename__= 'registros'
    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(50), nullable=False, unique=True)
    apellidos = db.Column(db.String(50), nullable=False)
    correo = db.Column(db.String(50), nullable=False)
    contrasena = db.Column(db.String(128), nullable=False)    
    tipo_usuario = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'Register:{self.id},{self.nombres}, {self.apellidos}, {self.correo}, {self.contrasena}, {self.tipo_usuario}'

class Catalogo(db.Model):
    __tablename__ = 'catalogos'
    id = db.Column(db.Integer, primary_key = True)
    producto = db.Column(db.String(50), nullable = False)
    precio = db.Column(db.Integer, nullable = False)
    list_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable= False)

    def __repr__(self):
        return f'Catalogo:{self.id}, {self.producto}, {self.precio} '

class Categoria(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key = True)
    nombre_categoria = db.Column(db.String(50), nullable = False)
    catalogos = db.relationship('Catalogo', backref = 'list', lazy = True)

    def __repr__(self):
        return f'Categoria: {self.id}, {self.nombre_categoria}  '
