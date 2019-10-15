
from flask import Flask, render_template, request, redirect, url_for, flash, session 
from flask_socketio import SocketIO, emit
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config[ 'SECRET_KEY' ] = 'uno2treshema0'
socketio = SocketIO(app)

#https://www.clever-cloud.com/en/
app.config['MYSQL_HOST'] = 'bvdf19qtfn904fgbcwpj-mysql.services.clever-cloud.com'
app.config['MYSQL_USER'] = 'uxvntw3vqhqqu1w5'
app.config['MYSQL_PASSWORD'] = 'mCUlY8fV5cRCPlttFYOU'
app.config['MYSQL_DB'] = 'bvdf19qtfn904fgbcwpj'
mysql = MySQL(app)

app.secret_key = 'uno2treshema0'

@app.route('/')
def home():
    return render_template( './homePage.html' )

@app.route('/about')
def about():
    return render_template( './aboutPage.html' )

@app.route('/chat')
def chat():
    if 'nickName' in session:
        strange = session['nickName']
    else:
        strange = ""

    if strange != "":
        return render_template( './chatPage.html', nickName = strange )
    else:
        flash('Es necesario iniciar session :V')  
        return redirect(url_for('login'))

@app.route('/register')
def register():    
    return render_template('./registerPage.html')

@app.route('/registerUser', methods = ['POST'])
def registeruser():
    if request.method == 'POST':
        nickName = request.form['nickName']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute('SELECT nickName, userEmail FROM users')
        users = cur.fetchall()
        cur.close()
        for user in users:
            if nickName == user[0]:
                flash('El nombre clave ya se encuentra registrado ')  
                return redirect(url_for('register'))
            elif email == user[1]:
                flash('El correo electronico ya se encuentra registrado ')  
                return redirect(url_for('register'))

        userName = request.form['userName']
        firstLastName = request.form['firstLastname']
        secondLastName = request.form['secondLastname']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO users (nickName, userName, firstLastname, secondLastname, userEmail, userPassword) VALUES (%s, %s, %s, %s, %s, %s)',
        (nickName, userName, firstLastName, secondLastName, email, password))
        mysql.connection.commit()
        flash('Se a registrado correctamente :)')        
        return redirect(url_for('login'))
    return redirect(url_for('register'))

@app.route('/login')
def login():   
    return render_template('./loginPage.html')

@app.route('/userlogin', methods = ['POST'])
def userlogin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute('SELECT nickName, userEmail, userPassword FROM users')
        users = cur.fetchall()
        cur.close()
        for user in users:
            if email == user[1] and password == user[2]:
                session['nickName'] = str(user[0])
                return redirect(url_for('chat'))
    flash('El usuario o la contraseña no coiciden')  
    return redirect(url_for('login'))       

def messageRecived():
      print( 'message was received!!!' )

@socketio.on( 'my event' )
def handle_my_custom_event( json ):
  print( 'recived my event: ' + str( json ) )
  socketio.emit( 'my response', json, callback=messageRecived )

if __name__  == '__main__':
    socketio.run(app,debug = True)
