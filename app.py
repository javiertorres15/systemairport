from flask import Flask
from flask import render_template, request, flash, redirect, url_for,session,session
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
    
    
     

    if 'user' in session:
        return render_template('user/indexUser.html')
    else:
        return "no tienes permiso a esta ruta"
@app.route('/searchFlight')
def searchFlight():
    if 'user' in session:
        return render_template('user/searchFlight.html')
    else:
        return "no tienes permiso a esta ruta"
@app.route('/rateFlight')
def rateFlight():
    if 'user' in session:
        return render_template('user/rateFlight.html')
    else:
        return "no tienes permiso a esta ruta"
    
  


#MENU ADMIN
@app.route('/indexAdmin')
def indexAdmin():
    if 'user1' in session:
        return render_template('admin/indexAdmin.html')
    else:
        return "no tienes permiso a esta ruta"   
@app.route('/userAdmin')
def userAdmin():
    if 'user1' in session:
        return render_template('admin/userAdmin.html')  
    else:
        return "no tienes permiso a esta ruta" 
#ELIMINAR USUARIOS
@app.route('/userDelete')
def userDelete():
    sql = "SELECT * FROM `usuarios`;"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    usuarios=cursor.fetchall()
    if 'user1' in session:
        return render_template('admin/userDelete.html',usuarios=usuarios) 
    else:
        return "no tienes permiso a esta ruta"
@app.route('/destroyUser/<int:id>')
def destroyUser(id): 
    conn=mysql.connect()
    cursor=conn.cursor()

    cursor.execute("DELETE FROM usuarios WHERE id=%s",(id))
    conn.commit()
    return redirect('/userDelete')
#EDITAR USUARIOS      
@app.route('/userEdit')
def userEdit():
    if 'user1' in session:
        return render_template('admin/userEdit.html')
    else:
        return "no tienes permiso a esta ruta"         
#/////////////////////////////////////////////////////////////
@app.route('/pilotAdmin')
def pilotAdmin():
    if 'user1' in session:
            return render_template('admin/pilotAdmin.html')
    else:
        return "no tienes permiso a esta ruta"     
@app.route('/pilotAdd')
def pilotAdd():
    if 'user1' in session:
            return render_template('admin/pilotAdd.html')
    else:
        return "no tienes permiso a esta ruta"    
@app.route('/pilotDelete')
def pilotDelete():

    sql = "SELECT * FROM `pilotos`;"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    pilotos=cursor.fetchall()

    if 'user1' in session:
            return render_template('admin/pilotDelete.html', pilotos=pilotos)
    else:
        return "no tienes permiso a esta ruta"   
#ELIMINAR PILOTO
@app.route('/destroyPilot/<int:id>')
def destroyPilot(id): 
    conn=mysql.connect()
    cursor=conn.cursor()

    cursor.execute("DELETE FROM pilotos WHERE id=%s",(id))
    conn.commit()
    return redirect('/pilotDelete')

#EDITAR PILOTO
@app.route('/pilotEdit')
def pilotEdit():
    
    sql = "SELECT * FROM `pilotos`;"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    pilotos=cursor.fetchall()

    if 'user1' in session:
            return render_template('admin/pilotEdit.html', pilotos=pilotos)
    else:
        return "no tienes permiso a esta ruta" 


@app.route('/editPilot/<int:id>')
def editPilot(id):
    
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM pilotos WHERE id=%s",(id))
    pilotos=cursor.fetchall()
    conn.commit()
    
    return render_template('admin/editPilot.html',pilotos=pilotos)

@app.route('/updatePiloto', methods=['POST'])
def updatePiloto(): 
    _identificacion=request.form['txtId']
    _nombres=request.form['txtNombre']
    _apellidos=request.form['txtApellido']
    _genero=request.form['genero']
    _correo=request.form['txtCorreo']
    _nacimiento=request.form['txtFecha']
    _usuario=request.form['txtUsuario']
    _contrasena=request.form['txtContrasena']
    id=request.form['txtVar']

    sql = "UPDATE pilotos SET identificacion=%s, nombres=%s, apellidos=%s, genero=%s, correo=%s, nacimiento=%s, usuario=%s, contrasena=%s WHERE id=%s;"
    
    datos=(_identificacion,_nombres,_apellidos,_genero,_correo,_nacimiento,_usuario,_contrasena,id)

    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return redirect('/pilotAdmin')
    
#////////////////////////////////////////////////////////////
@app.route('/flightAdmin')
def flightAdmin():
    if 'user1' in session:
            return render_template('admin/flightAdmin.html')
    else:
        return "no tienes permiso a esta ruta"   
@app.route('/flightDelete')
def flightDelete():
    sql = "SELECT * FROM `vuelos`;"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    vuelos=cursor.fetchall()
    if 'user1' in session:
            return render_template('admin/flightDelete.html',vuelos=vuelos)
    else:
        return "no tienes permiso a esta ruta"    
@app.route('/flightEdit')
def flightEdit():
    if 'user1' in session:
           return render_template('admin/flightEdit.html')
    else:
        return "no tienes permiso a esta ruta"    
#/////////////////////////////////////////////////////
@app.route('/rateAdmin')
def rateAdmin():

    sql = "SELECT * FROM `sugerencias`;"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    sugerencias=cursor.fetchall()
    print(sugerencias)
    if 'user1' in session:
           return render_template('admin/rateAdmin.html',sugerencias=sugerencias)
    else:
        return "no tienes permiso a esta ruta"    
    




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

    sql = "SELECT vuelos.id, lugares.id AS idOrigen, lugares.ciudad As Origen, vuelos.destino, destino.ciudad, pilotos.id, CONCAT(pilotos.nombres, ' ', pilotos.apellidos) AS piloto, vuelos.fecha FROM vuelos JOIN lugares ON vuelos.origen = lugares.id JOIN destino ON vuelos.destino = destino.id JOIN pilotos ON vuelos.piloto = pilotos.id;"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    vuelos=cursor.fetchall()


    

    if 'user' in session:
        return render_template('user/reservaFlight.html',vuelos=vuelos)  
    else:
        return "no tienes permiso a esta ruta"

#REGISTRO DE RESERVAS  EN LA BASE DE DATOS
@app.route('/addReserva', methods=['POST'])
def addReserva():
    _lugar=request.form['lugarTxt']
    _fechaTxt=request.form['fechaTxt']
    _fechaRegresoTxt=request.form['fechaRegresoTxt']

    sql = "INSERT INTO `reserva` (`id`,`lugar`, `estado`, `fecha`, `fecha_regreso`) VALUES (NULL,%s, NULL, %s, %s);"
    
    datos=(_lugar,_fechaTxt,_fechaRegresoTxt)

    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return render_template('user/reservaFlight.html')

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
    session['user'] = txtUsuario
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


#LOGOUT DE USUARIOS
@app.route("/logoutUser")
def logoutUser():
    session.clear()
    return render_template("login/index.html")



#LOGIN DE ADMIN
@app.route('/admin_login', methods=['POST'])
def ingresarAdminn():
    txtUsuario = request.form["txtUsuario"]
    txtContrasena = request.form["txtContrasena"]
    session['user1'] = txtUsuario
    sql = "SELECT * FROM `administrador` WHERE usuario = %s;"
    datos = (txtUsuario)
    
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    rest=cursor.fetchall()
    
    
       
    if len(rest)!=0:
        if txtUsuario == rest[0][1] and txtContrasena == rest[0][2]:
            session["usuario"] = txtUsuario
            return render_template("admin/indexAdmin.html")
        else:
            flash("Correo o contraseña incorrectos")
            return render_template("admin/loginAdmin.html")
    else:
        flash("Correo o contraseña incorrectos")
        return render_template("admin/loginAdmin.html")

@app.route("/logoutAdmin")
def logoutAdmin():
    session.clear()
    return render_template("admin/loginAdmin.html")

if __name__=='__main__':
    app.run(debug=True)


