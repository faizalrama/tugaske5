from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return render_template('login.html')
@app.route("/login", methods=['POST'])
def login():
    USERNAME = 'user'
    PASSWORD = 'pass'
    username = request.form['username']
    password = request.form['password']
    
    if username == USERNAME and password == PASSWORD:
        return redirect(url_for('home'))
    else:
        flash('Invalid credentials. Please try again.')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/produk')
def produk():
    return render_template('produk.html')


@app.route("/pesan")
def  pesan():
    return render_template("pesan.html")

@app.route("/transaksi")
def transaksi():
    return render_template("transaksi.html")

