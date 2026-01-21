import email
from flask import Flask, render_template, request, redirect, url_for, jsonify   
import Model602 as pelanggan
import Model614 as barang
app = Flask(__name__)


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
@app.route('/form_614', methods=['GET', 'POST'])
def form_614():
    if request.method == 'POST':
        nama = request.form['nama614']
        kategori = request.form['kategori614']
        stok = int(request.form['stok614'])
        harga = int(request.form['harga614'])
        catatan = request.form['catatan614']

        barang.add_barang(nama, kategori, stok, harga, catatan)
        return redirect(url_for('form_614'))

    data = barang.get_barang_all()
    return render_template('form_614.html', data=data)


@app.route('/edit_barang/<int:id>', methods=['PUT'])
def edit_barang(id):
    data = request.get_json()
    success = barang.update_barang(id,
                            data.get('nama'),
                            data.get('kategori'),
                            data.get('stok'),
                            data.get('harga'),
                            data.get('catatan'))
    return jsonify(success=success)


@app.route('/hapus_barang/<int:id>', methods=['DELETE'])
def hapus_barang(id):
    success = barang.delete_barang(id)
    return jsonify(success=success)


# ---------- Form Jovi (Data Pelanggan) ----------
@app.route('/form_602', methods=['GET', 'POST'])
def form_602():     
    if request.method == 'POST':
        nama = request.form['nama602']
        alamat = request.form['alamat602']
        telepon = request.form['telepon602']
        email = request.form['email602']
        jumlahpesanan = int(request.form['jumlahpesanan602'])
# memanggil fungsi add_pelanggan dari Model602.py
        pelanggan.add_pelanggan(nama, alamat, telepon, email, jumlahpesanan)
        return redirect(url_for('form_602'))
# menampilkan semua data pelanggan
    data = pelanggan.get_pelanggan_all()
    return render_template('form_602.html', data=data)

#memperbarui data pelanggan berdasarkan id
@app.route('/edit_pelanggan/<int:id>', methods=['PUT'])
def edit_pelanggan(id):
    data = request.get_json()
    success = pelanggan.update_pelanggan(id,
                               data.get('nama'),
                               data.get('alamat'),
                               data.get('telepon'),
                               data.get('email'),
                               data.get('jumlahpesanan'))
    return jsonify(success=success)

#menghapus data pelanggan berdasarkan id
@app.route('/hapus_pelanggan/<int:id>', methods=['DELETE'])
def hapus_pelanggan(id):
    success = pelanggan.delete_pelanggan(id)
    return jsonify(success=success)

if __name__ == '__main__':
    app.run(debug=True)
