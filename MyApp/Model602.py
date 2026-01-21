import sqlite3

DB_NAME = "UTS7.db"
#untuk mengkoneksikan database
def get_db_connection():
    conn = sqlite3.connect(DB_NAME)     
    conn.row_factory = sqlite3.Row
    return conn
#mendapatkan semua data pelanggan dari tabel pelanggan602
def get_pelanggan_all():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pelanggan602 ORDER BY id')
    rows = cursor.fetchall()        #menutup koneksi database
    conn.close()
    return rows

#menambahkan data pelanggan baru ke dalam tabel pelanggan602
def add_pelanggan(nama, alamat, telepon, email, jumlahpesanan=0):
    conn = get_db_connection()
    cur = conn.execute('INSERT INTO pelanggan602 (nama, alamat, telepon, email, jumlahpesanan) VALUES (?, ?, ?, ?, ?)',
                       (nama, alamat, telepon, email, jumlahpesanan))
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return new_id

#memperbarui data pelanggan yang sudah ada di dalam tabel pelanggan602
def update_pelanggan(id, nama=None, alamat=None, telepon=None, email=None, jumlahpesanan=None):
    conn = get_db_connection()
    
    row = conn.execute('SELECT * FROM pelanggan602 WHERE id = ?', (id,)).fetchone()
    if not row:
        conn.close()
        return False
#menggunakan nilai baru jika diberikan, jika tidak menggunakan nilai yang sudah ada
    nama = nama if nama is not None else row['nama']
    alamat = alamat if alamat is not None else row['alamat']
    telepon = telepon if telepon is not None else row['telepon']
    email = email if email is not None else row['email']
    jumlahpesanan = jumlahpesanan if jumlahpesanan is not None else row['jumlahpesanan']
#memperbarui data di database
    conn.execute('UPDATE pelanggan602 SET nama = ?, alamat = ?, telepon = ?, email = ?, jumlahpesanan = ? WHERE id = ?',
                 (nama, alamat, telepon, email, jumlahpesanan, id))
    conn.commit()
    conn.close()
    return True

#menghapus data pelanggan dari tabel pelanggan602 berdasarkan id
def delete_pelanggan(id):
    conn = get_db_connection()
    cur = conn.execute('DELETE FROM pelanggan602 WHERE id = ?', (id,))
    conn.commit()
    affected = cur.rowcount
    conn.close()
    return affected > 0
