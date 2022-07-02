from urllib import response
import hashlib
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import (
    UserMixin, 
    LoginManager, 
    login_user, 
    login_required, 
    current_user      
)   
from flask import (
    Flask,
    abort,
    render_template,
    request,
    flash,
    redirect,
    url_for,
    session
)
from models import setup_db, Register, Catalogo, Categoria
from flask_cors import CORS, cross_origin


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

    #Rutas para renderizar
    #Ruta home
    @app.route('/')
    def home():
        return render_template("home.html")
    #Ruta catalgo
    @app.route('/catalogo', strict_slashes=False)
    def catalogo():
        return render_template("catalogo.html")
    #Ruta login
    @app.route('/login')
    def login():
        return render_template("login.html")

    #Ruta Login
    @app.route('/login', methods=[ 'POST'])
    def login_Post():
        correo= request.form.get('correo')
        contrasena = request.form.get('contrasena')
        print(correo)
        print(contrasena)   
        user= Register.query.filter_by(correo = correo).first()
        print(user.correo)
        print( check_password_hash(user.contrasena, contrasena))
        if not user or not check_password_hash(user.contrasena, contrasena):
            flash('Por favor revise sus datos e intentelo de nuevo')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('usuario'))


    #Ruta de la sesion de usurios
    @login_manager.user_loader  
    def load_user(user_id):
        return Register.query.get(int(user_id))

    #Ruta Registrar 
    @app.route('/register', )
    def register():
        return render_template("register.html")

    #Ruta recuperar datos de Registrar
    @app.route('/register/registrar', methods= ['POST']  )
    def resgistrar():
        try:
            nombres = request.get_json()['nombres']
            apellidos = request.get_json()['apellidos']
            correo = request.get_json()['correo']
            contrasena = request.get_json()['contrasena']
            _hashed_password = generate_password_hash(contrasena)
            registro = Register (nombres=nombres, apellidos=apellidos, correo=correo, contrasena=_hashed_password)
            db.session.add(registro)
            db.session.commit()
            db.session.commit()
            error=False
        
        except:
            db.session.rollback()
            error= True
        finally:            
            db.session.close()
            return render_template('success', error=error)
    #Ruta usuario
    @login_required
    @app.route('/usuario')
    def usuario():
        if 'loggedin' in session:
            return render_template('usuario.html', correo = session['correo'],
            catalogos = Catalogo.query.all(),
            categorias =Categoria.query.order_by('id').all(),
            nombres = current_user.nombres)
            
        return render_template("usuario.html",
        catalogos = Catalogo.query.all(), nombres = current_user.nombres)
    #Ruta de categorias
    @app.route('/categoria/<list_id>', methods=['GET'])
    def get_list_categorias(list_id):
        return render_template('usuario.html',
        categorias =Categoria.query.order_by('id').all(),
        active_list=Catalogo.query.get(list_id),
        catalogos=Catalogo.query.filter_by(list_id=list_id).order_by('id').all()
        )
    #Ruta de administrador
    @app.route('/admin')
    def admin():
        if 'loggedin' in session:
            return render_template('admin.html', correo = session['correo'],
            catalogos = Catalogo.query.all(),
            categorias =Categoria.query.order_by('id').all(),)
            
        return render_template("admin.html",
        catalogos = Catalogo.query.all())
    #Ruta para categorias del administrador
    @app.route('/admin/categoria/<list_id>', methods=['GET'])
    def get_list_categorias_admin(list_id):
        return render_template('admin.html',
        categorias =Categoria.query.order_by('id').all(),
        active_list=Categoria.query.get(list_id),
        catalogos=Catalogo.query.filter_by(list_id=list_id).order_by('id').all()
        )    

    #Ruta para eliminar Catalogos desde administrador
    @app.route('/delete/<id>', methods = ['GET', 'POST'])
    def delete(id):
        my_data = Catalogo.query.get(id)
        db.session.delete(my_data)
        db.session.commit()
        return redirect(url_for('admin'))

    #Ruta para crear Catalogos desde administrador(aun tiene errores)
    @app.route('/insert', methods = ['POST'])
    def insert():

        if request.method == 'POST':
            producto = request.form['producto']
            precio = request.form['precio']
            list_id = request.form['id']
            my_data = Catalogo(producto=producto,precio= precio,list_id= list_id)
            db.session.add(my_data)
            db.session.commit()

            return redirect(url_for('admin("list_id")'))


    
    return app

