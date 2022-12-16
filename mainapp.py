from flask import Flask,render_template, url_for,redirect,request,session,flash
from flask_mysqldb import MySQL,MySQLdb
from werkzeug.security import check_password_hash,generate_password_hash
import pymysql.cursors,os

conn=cursor=None
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
    return redirect(url_for('Login'))
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

# fungsi untuk menutup koneksi
def closeDb():
    global conn, cursor
    conn.close()

# fungsi view index() untuk menampilkan data dari database
@app.route('/admin')
def admin():
        cursor  =mysql.connection.cursor()
        container = []
        cursor.execute('SELECT * FROM tb_user')
        results = cursor.fetchall()
        for data in results:
         container.append(data)
        return render_template('admin.html', container=container)

# fungsi view tambah() untuk membuat form tambah
@app.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        cursor  =mysql.connection.cursor()
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        sql = "INSERT INTO tb_user (username,email,password) VALUES (%s, %s, %s)"
        val = (username, email, password)
        cursor.execute(sql, val)
        return redirect(url_for('admin'))
    else:
        return render_template('tambah.html')
        # fungsi untuk menghapus data
@app.route('/hapus/<id>',methods=['GET','POST'])
def hapus(id):
    cursor=mysql.connection.cursor()
    cursor.execute('DELETE FROM tb_user WHERE id=%s', [id,])
    return redirect(url_for('admin'))
        #fungsi view edit() untuk form edit
@app.route('/edit/<id>', methods=['GET','POST'])
def edit(id):
    cursor=mysql.connection.cursor()
    cursor.execute('SELECT * FROM tb_user WHERE id=%s', [id,])
    data = cursor.fetchone()
    if request.method == 'POST':
        id = request.form['id']
        username = request.form['username']
        password = request.form['password']
        sql = "UPDATE tb_user SET username=%s, password=%s WHERE id =%s"
        val = (id,username, password)
        cursor.execute(sql, val)
        return redirect(url_for('admin'))
    else:
        return render_template('edit.html', data=data)
        
if __name__=="__main__":
    app.run(debug=True)