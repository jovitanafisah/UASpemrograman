import math
import requests
from flask import Flask, render_template, request, redirect, url_for, jsonify   
import Model602 as pelanggan
import Model614 as barang
app = Flask(__name__)

API_URL = "http://localhost:3000"


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
def form_614():
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)
    
    resp = requests.get(
        f"{API_URL}/barang614",
        params={
            "page": page,
            "limit": limit
        }
    )
    data = resp.json()

    total_data = data.get('total', 0)
    total_pages = math.ceil(total_data / limit)

    return render_template('form_614.html', data=data, page=page, total_pages=total_pages)

# ---------- Form Jovi (Data Pelanggan) ----------
@app.route('/form_602', methods=['GET', 'POST'])
def form_602():     
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)

    resp = requests.get(
        f"{API_URL}/pelanggan602",
        params={
            "page": page,
            "limit": limit
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
