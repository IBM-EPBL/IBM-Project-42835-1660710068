from flask import Flask,render_template,request,session, redirect,url_for
import ibm_db


app = Flask(__name__)
app.secret_key='vy@ur434'
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=19af6446-6171-4641-8aba-9dcff8e1b6ff.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=30699;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=bts04620;PWD=3m4fzYEmaQCgXqGx",'','')



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/forgot')
def forgot():
    return render_template('forgotten-password.html')

@app.route('/signup', methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        # conn = connection()
         try:
            sql = "INSERT INTO users VALUES('{}','{}','{}','{}')".format(request.form["name"],request.form["email"],request.form["phone"],request.form["password"])
            ibm_db.exec_immediate(conn,sql)
            return render_template('login.html')
         except:
            return render_template('signup.html')
    else:
            return render_template('signup.html')

@app.route('/login', methods=['POST','GET'])
def login():
     if request.method == 'POST':
       # conn =connection()
        email = request.form["email"]
        password = request.form["password"]
        sql = "SELECT COUNT(*) FROM users WHERE EMAIL=? AND PASSWORD=?"
        stmt = ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt, 1, email)
        ibm_db.bind_param(stmt, 2, password)
        ibm_db.execute(stmt)
        res = ibm_db.fetch_assoc(stmt)
        if res['1'] == 1:
            session['loggedin'] = True
            session['email'] = email
            return render_template('userpage.html')
        else:
            return render_template('login.html')
     else:
            return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__=='__main__':
    app.config['SESSION_TYPE']= 'filesystem'
    app.run(debug=True)

       