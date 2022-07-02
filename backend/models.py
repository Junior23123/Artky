
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
database_name = 'artky'
database_path = 'postgresql://{}:{}@{}/{}'.format('postgres','carro', 'localhost:5432', database_name)

db = SQLAlchemy()

def setup_db(app, database_path = database_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    db.create_all()

class Register(UserMixin,db.Model):
    __tablename__= 'registros'
    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(50), nullable=False, unique=True)
    apellidos = db.Column(db.String(50), nullable=False)
    correo = db.Column(db.String(50), nullable=False)
    contrasena = db.Column(db.String(128), nullable=False)    

    def __repr__(self):
        return f'Register:{self.id},{self.nombres}, {self.apellidos}, {self.correo}, {self.contrasena}'

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
