from flask import Flask
from flask import render_template, request, flash, redirect, url_for,session,jsonify
import flask
from flaskext.mysql import MySQL
from pymysql import cursors
import os


app= Flask(__name__)
app.secret_key = os.urandom(24)
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='systemairport'
mysql.init_app(app)


@app.route('/')
def index():
    return render_template('login/index.html')

#MENU USUARIOS
@app.route('/indexUser')
def indexUser():
    return render_template('user/indexUser.html')
@app.route('/searchFlight')
def searchFlight():
    return render_template('user/searchFlight.html')
@app.route('/rateFlight')
def rateFlight():
    return render_template('user/rateFlight.html')
  


#MENU ADMIN
@app.route('/indexAdmin')
def indexAdmin():
    return render_template('admin/indexAdmin.html')
@app.route('/userAdmin')
def userAdmin():
    return render_template('admin/userAdmin.html')  
@app.route('/userDelete')
def userDelete():
    return render_template('admin/userDelete.html')   
@app.route('/userEdit')
def userEdit():
    return render_template('admin/userEdit.html')    
#/////////////////////////////////////////////////////////////
@app.route('/pilotAdmin')
def pilotAdmin():
    return render_template('admin/pilotAdmin.html')
@app.route('/pilotAdd')
def pilotAdd():
    return render_template('admin/pilotAdd.html')
@app.route('/pilotDelete')
def pilotDelete():
    return render_template('admin/pilotDelete.html')
@app.route('/pilotEdit')
def pilotEdit():
    return render_template('admin/pilotEdit.html')
#////////////////////////////////////////////////////////////
@app.route('/flightAdmin')
def flightAdmin():
    return render_template('admin/flightAdmin.html')
# @app.route('/flightAdd')
# def flightAdd():
#     return render_template('admin/flightAdd.html')
@app.route('/flightDelete')
def flightDelete():
    return render_template('admin/flightDelete.html')
@app.route('/flightEdit')
def flightEdit():
    return render_template('admin/flightEdit.html')
#/////////////////////////////////////////////////////
@app.route('/rateAdmin')
def rateAdmin():
    return render_template('admin/rateAdmin.html')


#LOGIN ADMIN
@app.route('/loginAdmin')
def loginAdmin():
    return render_template('admin/loginAdmin.html')




#PARA SELECCIONAR EL GENERO REGISTRO USUARIO (lista desplegable)
@app.route('/registro')
def registro():

    
    sql = "SELECT * FROM `genero`;"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    genero=cursor.fetchall()
    
    return render_template('login/registro.html', genero=genero)

#PARA SELECCIONAR EL PILOTO AGREGAR VUELO (lista desplegable)
@app.route('/flightAdd')
def flightAdd():
    
    sql = "SELECT * FROM `pilotos`;"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    pilotos=cursor.fetchall()
    
    
    return render_template('admin/flightAdd.html', pilotos=pilotos)

#PARA SELECCIONAR DESTINO EN RESERVA VUELOS (LISTA DESPLEGABLE)
@app.route('/reservaFlight')
def reservaFlight():

    sql = "SELECT * FROM `vuelos`;"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    vuelos=cursor.fetchall()

    


    return render_template('user/reservaFlight.html',vuelos=vuelos)  

#REGISTRO DE PILOTOS EN LA BASE DE DATOS
@app.route('/registroPiloto', methods=['POST'])
def registroPiloto():

    _identificacion=request.form['txtId']
    _nombres=request.form['txtNombre']
    _apellidos=request.form['txtApellido']
    _genero=request.form['genero']
    _correo=request.form['txtCorreo']
    _nacimiento=request.form['txtFecha']
    _usuario=request.form['txtUsuario']
    _contrasena=request.form['txtContrasena']



    sql = "INSERT INTO `pilotos` (`id`,`identificacion`, `nombres`, `apellidos`, `genero`, `correo`, `nacimiento`, `usuario`, `contrasena`) VALUES (NULL,%s, %s, %s, %s, %s, %s, %s, %s);"
    
    datos=(_identificacion,_nombres,_apellidos,_genero,_correo,_nacimiento,_usuario,_contrasena)

    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return render_template('admin/indexAdmin.html')



#REGISTRO DE USUARIOS EN LA BASE DE DATOS
@app.route('/store', methods=['POST'])
def storage():

    _identificacion=request.form['txtId']
    _nombres=request.form['txtNombre']
    _apellidos=request.form['txtApellido']
    _genero=request.form['genero']
    _correo=request.form['txtCorreo']
    _nacimiento=request.form['txtFecha']
    _usuario=request.form['txtUsuario']
    _contrasena=request.form['txtContrasena']

    

    sql = "INSERT INTO `usuarios` (`id`,`identificacion`, `nombres`, `apellidos`, `genero`, `correo`, `nacimiento`, `usuario`, `contrasena`) VALUES (NULL,%s, %s, %s, %s, %s, %s, %s, %s);"
    
    datos=(_identificacion,_nombres,_apellidos,_genero,_correo,_nacimiento,_usuario,_contrasena)

    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return render_template('login/index.html')


#REGISTRO DE COMENTARIOS EN LA BASE DE DATOS
@app.route('/rateVuelo', methods=['POST'])
def rateVuelo():

    txtSugerencia=request.form['txtSugerencia']
    calificacion=request.form['calificacion']
    

    
    sql = "INSERT INTO `sugerencias` (`id`, `comentario`, `rate`) VALUES (NULL,%s, %s);"
    
    datos=(txtSugerencia,calificacion)

    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return render_template('user/indexUser.html')


#REGISTRO DE VUELOS EN LA BASE DE DATOS
@app.route('/addVuelo', methods=['POST'])
def addVuelo():

    origen=request.form['origen']
    destino=request.form['destino']
    piloto=request.form['piloto']
    fecha=request.form['fecha']
        
    sql = "INSERT INTO `vuelos` (`id`, `origen`, `destino`, `piloto`, `fecha`) VALUES (NULL,%s, %s, %s, %s);"
    
    datos=(origen,destino,piloto,fecha)

    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return render_template('admin/flightAdd.html')







#LOGIN DE USUARIOS
@app.route('/star_login', methods=['POST'])
def ingresar():
    txtUsuario = request.form["txtUsuario"]
    txtContrasena = request.form["txtContrasena"]
    sql = "SELECT * FROM `usuarios` WHERE usuario = %s;"
    datos = (txtUsuario)
    
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    rest=cursor.fetchall()
    
    
   
    if len(rest)!=0:
        if txtUsuario == rest[0][7] and txtContrasena == rest[0][8]:
            session["usuario"] = txtUsuario
            return render_template("user/indexUser.html")
        else:
            flash("Correo o contraseña incorrectos")
            return render_template("login/index.html")
    else:
        flash("Correo o contraseña incorrectos")
        return render_template("login/index.html")









if __name__=='__main__':
    app.run(debug=True)


