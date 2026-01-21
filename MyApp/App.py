import math
import requests
from flask import Flask, render_template, request, redirect, url_for, jsonify, session, flash
import Model602 as pelanggan
import Model614 as barang
from decorators import login_required, mahasiswa_602_required, mahasiswa_614_required

app = Flask(__name__)
app.secret_key = 'secret_key_kelompok7_2025'

API_URL = "http://localhost:3000"

# Database user dengan role berbeda
USERS = {
    'jovi': {'password': 'jovi123', 'role': 'mahasiswa_602', 'nama': 'Jovi'},
    'atha': {'password': 'atha123', 'role': 'mahasiswa_614', 'nama': 'Atha'}
}

def authenticate_user(username, password):
    """Autentikasi user"""
    if username in USERS:
        if USERS[username]['password'] == password:
            return USERS[username]
    return None


# ---------- LOGIN & LOGOUT ----------
@app.route('/login', methods=['GET', 'POST'])
def login():
    """Halaman login dengan role-based access control"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = authenticate_user(username, password)
        if user:
            session['logged_in'] = True
            session['username'] = username
            session['role'] = user['role']
            session['nama'] = user['nama']
            flash(f"Selamat datang, {user['nama']}!", "success")
            return redirect(url_for('home'))
        else:
            flash("Username atau password salah!", "danger")
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    """Logout user"""
    session.clear()
    flash("Anda telah logout.", "info")
    return redirect(url_for('login'))


# ---------- Halaman utama ----------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/forms')
def form():
    return render_template('form_interface.html')



# ---------- Form Atha (Data Barang) ----------
@app.route('/form_614')
@mahasiswa_614_required
def form_614():
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)
    
    resp = requests.get(
        f"{API_URL}/barang614",
        params={
            "page": page,
            "limit": limit,
        }
    )
    data = resp.json()

    total_data = data.get('total', 0)
    total_pages = math.ceil(total_data / limit)

    return render_template('form_614.html', data=data, page=page, total_pages=total_pages)

# ---------- Form Jovi (Data Pelanggan) ----------
@app.route('/form_602', methods=['GET', 'POST'])
@mahasiswa_602_required
def form_602():     
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)

    resp = requests.get(
        f"{API_URL}/pelanggan602",
        params={
            "page": page,
            "limit": limit,
        }
    )

    data = resp.json()

    total_data = data.get('total', 0)
    total_pages = math.ceil(total_data / limit)

    return render_template(
        'form_602.html',
        data=data,
        page=page,
        total_pages=total_pages
    )



if __name__ == '__main__':
    app.run(debug=True)
