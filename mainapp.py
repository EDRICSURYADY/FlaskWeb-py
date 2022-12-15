from flask import Flask,render_template, url_for,redirect,request,session,flash
from flask_mysqldb import MySQL,MySQLdb
from werkzeug.security import check_password_hash,generate_password_hash


app = Flask(__name__)
#koneksi
app.config["SECRET_KEY"]="INISCECRETKEY2022"
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='db_pdip'
mysql= MySQL(app)
@app.route('/')
def index():
    if 'loggedin' in session:
        return render_template('home.html')
    flash('harap login dulu','danger')
    return redirect(url_for('login'))
@app.route('/Fashion')
def Fashion():
        return render_template('Fashion.html')
@app.route('/Contact')
def Contact():
    return render_template('contact.html')   
@app.route('/Login',methods=['POST',"GET"])
def Login():
    
      #JIKA TOMBOL BUTTON DI CLICK -> REQUSET POST
    if request.method =='POST':
        email =request.form['email']
        password = request.form['password']
      #jika email dan password benar
        cursor =mysql.connection.cursor()
        cursor.execute('SELECT *FROM tb_user WHERE email=%s',(email,))
        akun = cursor.fetchone()
        if akun is None:
            flash('login gagal,ceck username anda','danger')
        elif not check_password_hash(akun[3],password):
            flash('login gagal,ceck username anda','danger')
        else:
            session['loggedin']= True
            session['username']= akun[1]
            return redirect(url_for('index'))
    return render_template('Login.html')

@app.route('/register',methods=['GET',"POST"])
def register():
     #JIKA TOMBOL BUTTON DI CLICK -> REQUSET POST
    if request.method =='POST':
        username =request.form['username']
        email= request.form['email']
        password = request.form['password']
    #   #jika email dan password benar
        cursor  =mysql.connection.cursor()
        cursor.execute('SELECT * FROM tb_user WHERE username=%s OR email=%s',(username,email,))
        akun = cursor.fetchone()
        if akun is None:
            cursor.execute('INSERT INTO tb_user VALUES(NULL,%s,%s,%s)',(username,email,generate_password_hash(password)))
            mysql.connection.commit()
            flash('regeistarsi berhasil','success')
        else :
            flash('regeistarsi berhasil','danger')
    return render_template('Register.html')

#logout
@app.route('/logout')
def logout():
    session.pop('loggedin',None)
    session.pop('username',None)
    return redirect(url_for('Login'))
if __name__=="__main__":
    app.run(debug=True)