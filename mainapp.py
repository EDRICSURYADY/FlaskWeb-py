from flask import Flask,render_template, url_for,redirect,request,session
from flask_mysqldb import MySQL,MySQLdb


app = Flask(__name__)
app.config["SECRET_KEY"]="INISCECRETKEY2022"

@app.route('/')
def index():
    nilai = "to the club banteng men!"
    return render_template('home.html',nilai=nilai)

@app.route('/Fashion', methods=['GET'])
def Fashion():
    if "email" in session:
        return render_template('Fashion.html')
    else:
        return redirect(url_for("Login"))
@app.route('/Contact')
def Contact():
    #jika dia sedang login
    if "email" in session:
        return render_template('contact.html')
    else:
        #jika dia tidak sedang login
        return redirect(url_for("Login"))
    return render_template('contact.html')   

@app.route('/Login',methods=['POST',"GET"])
def Login():
    
      #JIKA TOMBOL BUTTON DI CLICK -> REQUSET POST
    if request.method =='POST':
        email =request.form['email']
        password = request.form['password']
      #jika email dan password benar
        if email == "admin@gmail.com" and password == 'pass':
            session['email'] = email
            return redirect(url_for('index'))
            #jika salah email atau passowrd
        else:
            #harus login terlebih dahulu
            return redirect(url_for('Login'))
    return render_template('Login.html')

@app.route('/',methods=['POST',"GET"])
def reg():
     #JIKA TOMBOL BUTTON DI CLICK -> REQUSET POST
    if request.method =='POST':
        email =request.form['email']
        password = request.form['password']
      #jika email dan password benar
        if email == "admin@gmail.com" and password == 'pass':
            session['email'] = email
            return redirect(url_for('Login'))
            #jika salah email atau passowrd
        else:
            #harus regis terlebih dahulu
            return redirect(url_for('reg'))
    return render_template('Register.html')

if __name__=="__main__":
    app.run(debug=True)