Artky (Artesano-comunidad)
integrantes:

Mayra Medrano
Junior Haro
Yamileth Rincon
Álvaro Herrera
Descripcion:
Somos un grupo de estudiantes de UTEC que a través de "Artky" busca reivindicar la artesanía peruana, a través de un espacio que difunde las creaciones de nuestros artesanos asociados. En la página podrá encontrar el catálogo de artesanías de los miembros de nuestra comunidad.

La idea del proyecto nació a raíz de la pandemia cuando miles de artesanos sufieron pérdidas monetarias debido al confinamiento De esta manera, queremos ayudar con un granito de arena a la comunidad de artesanos peruanos.

Objetivos:
Objetivos principales:

Impulsar el trabajo de los artesanos asociados
Inspirar a nuevos artesanos
Satisfacer las principales necesidades de nuestros usuarios
Misión:

Promover la artesanía peruana a través de medios digitales
Visión:

Ser el principal medio de difusión digital de artesanía en Perú
Información acerca de las librerías/frameworks/plugins utilizados en Front End, Back End y base de datos.
Librerías:

SQLAlchemy:
Proporciona un conjunto completo de patrones diseñados para un acceso a bases de datos eficientes y de alto rendimiento.
redirect:
Un redirect (abreviatura de redirección) es un reenvío automático del lado del servidor o del cliente de una URL a otra. Se usa para la reubicación de un sitio web en un nuevo dominio o el mantenimiento de un servidor.
render_template:
Recibe como parámetro el fichero donde guardamos la plantilla y las variables que se pasan a esta.
request:
Permite el acceso a toda la información que pasa desde el navegador del cliente al servidor.
Url_for:
Se usa para crear una URL para evitar la sobrecarga de tener que cambiar las URL en toda la aplicación.
Flask:
Micro framework escrito en Python y desarrollado para simplificar y hacer más fácil la creación de aplicaciones web.
register:
Sirve al compilador para indicarle que "intentar" almacenar ese valor en un registro de la CPU en vez de directamente en memoria.
Check:
Especifica los valores que acepta un campo, impidiendo que se ingresen valores inapropiados cuando ejecutamos un comando insert o update.
Respuesta:
Sirve para presentar en la pantalla del navegador del cliente el resultado de cualquier código que hayamos escrito.
Cursor:
Se utiliza para el procesamiento individual de las filas devueltas por el sistema gestor de base de datos para una consulta.
Werkzeug.security:
Esta libreria basicamente la hemos usado para hashear la contraseña.
Flask_Migrate
psicopg2
Marcos:

JS -> JavaScript
Pitón
Matraz
Base de datos:

postgresql
Nombre del script a ejecutar para iniciar la base de datos con datos.
app.py
Información acerca de los API.Requests y Responses de cada endpoint utilizado en el sistema.
API.Requests: Usamos varios @app.route que reciben y devuelven la información entre servidor y cliente.

Respuesta:
@app.route('/registrar/registrar', métodos= ['POST'] )
def registrar():
pruebe:
nombres = request.get_json()['nombres']
apellidos = request.get_json()[' apellidos']
correo = request.get_json()['correo']
contrasena = request.get_json()['contrasena']
registro = Register (nombres=nombres, apellidos=apellidos, correo=correo, contrasena=contrasena)
db.session .add(registro)
db.session.commit()
excepto:
db.session.rollback()
error = True
finalmente:
return render_template("register.html", error = error)

Puntos finales

índice '/'
'/home': Muestra la página principal de la aplicación con los botones Iniciar sesión, Registrarse y Configuración.
'/register': Pagina para registrarse
'/login': Iniciar sesión
Hospedadores.
servidor local = 5432
Puerto = 5000
Forma de autenticación.
Para la autentificación de los usuarios usaron lenguaje SQL.
Manejo de errores HTTP:
500: Errores en el servidor
400: Errores en el Cliente
300: Redirección
200: Exitoso
100: Informativo

Manejo de errores:

Los errores dentro de registrarse en la pagina web se manejaron gracias a los "types" que verificaron que un correo es ingresado correctamente.
@app.route('/registrar/registrar', métodos= ['POST'] )
def registrar():
try:
nombres = request.get_json()['nombres']
apellidos = request.get_json()['apellidos' ]
correo = request.get_json()['correo']
contrasena = request.get_json()['contrasena']
registro = Register (nombres=nombres, apellidos=apellidos, correo=correo, contrasena=contrasena)
db.session.add (registro)
db.session.commit()
error=False
excepto:
db.session.rollback()
error= True
finalmente:
db.session.close()
return render_template('success', error=error)

Cómo ejecutar el sistema (Deployment scripts)
Lo primero que debemos hacer es ejecutar el archivo "script.py" para la creación de la tabla en la base de datos y luego ejecutar el archivo "app.py" para levantar el servidor.
