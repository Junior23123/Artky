from email.policy import default
from enum import unique
import re
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
from models import Register, Catalogo, Categoria, setup_db, db
PELICULAS_PER_PAGE=5

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    
    ##ojo esto
    db = SQLAlchemy(app)
    login_manager = LoginManager()
    app.secret_key = 'cairocoders-ednalan'
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-type, Authorizations, true')
        response.headers.add('Access-Control-Allow-Methods', 'GET, OPTIONS, POST, PATCH, DELETE')
        return response

    @app.route('/login', methods=['POST'])
    def login_Post():
        correo = request.json['correo']
        contrasena = request.json['contrasena']
        user = Register.query.filter_by(correo=correo).first()
        print(user)
        if not user or not check_password_hash(user.contrasena, contrasena):
            flash('Por favor revise sus datos e intentelo de nuevo')
            return jsonify({"message": "user not found", "status": 404}), 404
        # login_user(user)
        return jsonify({"message": "success", "status": 200, "data": {"name": user.nombres,
                                                                    "email": user.correo,
                                                                    "typeUser": user.tipo_usuario}}), 200

    # Ruta de la sesion de usurios

    # Ruta Registrar
    # @app.route('/register', )
    # def register():
    #     return render_template("register.html")

    # Ruta recuperar datos de Registrar


    @app.route('/register/registrar', methods=['POST'])
    def resgistrar():
        try:
            nombres = request.json['nombres']
            apellidos = request.json['apellidos']
            correo = request.json['correo']
            contrasena = request.json['contrasena']
            tipo_usuario = request.json['tipo_usuario']
            _hashed_password = generate_password_hash(contrasena)
            registro = Register(nombres=nombres, apellidos=apellidos,
                                correo=correo, contrasena=_hashed_password, tipo_usuario=tipo_usuario)
            db.session.add(registro)
            db.session.commit()
            db.session.commit()

        except:
            db.session.rollback()
            return jsonify({"message": "error server", "status": 500}), 500
        finally:
            db.session.close()
            return jsonify({"message": "success", "status": 201}), 201



    @app.route('/category', methods=['POST'])
    # @login_required
    def createCategoria():
        if request.method == 'POST':
            try:
                name = request.get_json()['name']
                categoria = Categoria(nombre_categoria=name)
                db.session.add(categoria)
                db.session.commit()
                flash('Categoria creada')
            except:
                db.session.rollback()
                return jsonify({"message": "error server", "status": 500}), 500
            finally:
                db.session.close()
                return jsonify({"message": "success", "status": 201}), 201


    @app.route('/category', methods=['GET'])
    # @login_required
    def getCategorias():
        try:
            cols = ['id', 'nombre_categoria']
            data = Categoria.query.all()
            result = [{col: getattr(d, col) for col in cols} for d in data]

            return jsonify(result)
        except:
            db.session.rollback()
            return jsonify({"message": "error server", "status": 500}), 500
        finally:
            db.session.close()


    @app.route('/product', methods=['POST'])
    # @login_required
    def createProducto():
        try:
            name = request.get_json()['name']
            precio = request.get_json()['precio']
            categoria = request.get_json()['categoria']

            producto = Catalogo(
                producto=name, precio=precio, list_id=categoria)

            db.session.add(producto)
            db.session.commit()
            flash('Producto creado')
        except:
            db.session.rollback()
            return jsonify({"message": "error server", "status": 500}), 500
        finally:
            db.session.close()
            return jsonify({"message": "success", "status": 201}), 201


    @app.route('/product', methods=['GET'])
    # @login_required
    def getProductos():
        try:
            cols = ['id', 'producto', 'precio', 'list_id']
            data = Catalogo.query.all()
            result = [{col: getattr(d, col) for col in cols} for d in data]

            return jsonify(result)
        except:
            db.session.rollback()
            return jsonify({"message": "error server", "status": 500}), 500
        finally:
            db.session.close()


    @app.route('/product/<id>', methods=['GET'])
    # @login_required
    def deleteProduct(id):
        my_data = Catalogo.query.get(id)
        db.session.delete(my_data)
        db.session.commit()
        return jsonify({"message": "success", "status": 200}), 200


    return app

