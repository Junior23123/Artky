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

def paginate_peliculas(request, selection):
    #TODO
    pass

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    
    ##ojo esto
    db = SQLAlchemy(app)
    login_manager = LoginManager()

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
        print(correo,contrasena)
        if not user or not check_password_hash(user.contrasena, contrasena):
            flash('Por favor revise sus datos e intentelo de nuevo')
            return jsonify({"message": "user not found", "status": 404}), 404
        # login_user(user)
        return jsonify({"message": "success", "status": 200, "data": {"name": user.nombres, "email": user.correo}}), 200


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
            _hashed_password = generate_password_hash(contrasena)
            registro = Register(nombres=nombres, apellidos=apellidos,
                                correo=correo, contrasena=_hashed_password)
            db.session.add(registro)
            db.session.commit()
            db.session.commit()

        except:
            db.session.rollback()
            return jsonify({"message": "error server", "status": 500}), 500
        finally:
            db.session.close()
            return jsonify({"message": "success", "status": 201}), 201
    # Ruta usuario


    # @app.route('/usuario')
    # # @login_required
    # def usuario():
    #     if 'loggedin' in session:
    #         return render_template('usuario.html', correo=session['correo'],
    #                                productos=Categoria.query.all(),
    #                                nombres=current_user.nombres)

    #     return render_template("usuario.html",
    #                            catalogos=Catalogo.query.all(), nombres=current_user.nombres, productos=Categoria.query.all())

    # Ruta de categorias


    @app.route('/categoria/<list_id>', methods=['GET'])
    # @login_required
    def get_list_categorias(list_id):
        return render_template('usuario.html',
                            productos=Categoria.query.all(),
                            active_list=Catalogo.query.get(list_id),
                            catalogos=Catalogo.query.filter_by(
                                list_id=list_id).order_by('id').all()
                            )
    # Ruta de administrador


    @app.route('/admin')
    def admin():
        if 'loggedin' in session:
            return render_template('admin.html', correo=session['correo'],
                                catalogos=Catalogo.query.all(),
                                categorias=Categoria.query.order_by('id').all(),
                                nombres=current_user.nombres)

        return render_template("admin.html",
                            catalogos=Catalogo.query.all(), nombres=current_user.nombres, productos=Categoria.query.all())
    # Ruta para categorias del administrador


    @app.route('/admin/categoria/<list_id>', methods=['GET'])
    # @login_required
    def get_list_categorias_admin(list_id):
        return render_template('admin.html',
                            categoria=Categoria.query.order_by('id').all(),
                            catalogos=Catalogo.query.filter_by(
                                list_id=list_id).order_by('id').all()
                            )


    # Ruta para eliminar Catalogos desde administrador
    @app.route('/delete/<id>', methods=['GET', 'POST'])
    # @login_required
    def delete(id):
        my_data = Catalogo.query.get(id)
        db.session.delete(my_data)
        db.session.commit()
        return redirect(url_for('admin'))


    @app.route('/create', methods=['GET', 'POST'])
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
                abort(500)
            finally:
                return redirect(url_for('admin'))


    @app.route('/createProducto', methods=['GET', 'POST'])
    # @login_required
    def createProducto():
        if request.method == 'POST':
            try:
                name = request.get_json()['name']
                precio = request.get_json()['precio']
                categoria = request.get_json()['categoria']
                producto = Catalogo(
                    producto=name, precio=precio, categoria=categoria)
                db.session.add(producto)
                db.session.commit()
                flash('Producto creado')
            except:
                db.session.rollback()
                abort(500)
            finally:
                return redirect(url_for('admin'))


    # Ruta para crear Catalogos desde administrador(aun tiene errores)
    @app.route('/insert', methods=['POST'])
    # @login_required
    def insert():
        if request.method == 'POST':
            try:
                producto = request.get_json()['producto']
                precio = request.get_json()['precio']
                list_id = request.get_json()['categoria']
                my_data = Catalogo(producto=producto,
                                precio=precio, list_id=list_id)
                db.session.add(my_data)
                db.session.commit()
                flash('Producto creado')
            except:
                db.session.rollback()
                abort(500)
            finally:
                return redirect(url_for('admin'))


    return app

