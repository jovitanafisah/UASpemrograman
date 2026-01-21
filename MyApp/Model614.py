import sqlite3

DB_NAME = "UTS7.db"
#untuk mengkoneksikan database
def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def get_barang_all():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM barang614 ORDER BY id')       #mengambil semua data dari tabel barang614 dan mengurutkannya berdasarkan id
    rows = cursor.fetchall()
    conn.close()        #menutup koneksi database
    return rows
    

#menambahkan data barang baru ke dalam tabel barang614
def add_barang(nama, kategori, stok=0, harga=0, catatan=''):
    conn = get_db_connection()
    cur = conn.execute('INSERT INTO barang614 (nama, kategori, stok, harga, catatan) VALUES (?, ?, ?, ?, ?)',
                       (nama, kategori, stok, harga, catatan))
    conn.commit()       #menyimpan perubahan ke database
    new_id = cur.lastrowid
    conn.close()
    return new_id

#memperbarui data barang yang sudah ada di dalam tabel barang614
def update_barang(id, nama=None, kategori=None, stok=None, harga=None, catatan=None):
    conn = get_db_connection()
    row = conn.execute('SELECT * FROM barang614 WHERE id = ?', (id,)).fetchone()
    if not row:
        conn.close()
        return False
#menggunakan nilai baru jika diberikan, jika tidak menggunakan nilai yang sudah ada
    nama = nama if nama is not None else row['nama']
    kategori = kategori if kategori is not None else row['kategori']
    stok = int(stok) if stok is not None else row['stok']
    harga = int(harga) if harga is not None else row['harga']
    catatan = catatan if catatan is not None else row['catatan']
#memperbarui data di database
    conn.execute('UPDATE barang614 SET nama = ?, kategori = ?, stok = ?, harga = ?, catatan = ? WHERE id = ?',
                 (nama, kategori, stok, harga, catatan, id))
    conn.commit()
    conn.close()
    return True

#menghapus data barang dari tabel barang614 berdasarkan id
def delete_barang(id):
    conn = get_db_connection()
    cur = conn.execute('DELETE FROM barang614 WHERE id = ?', (id,))
    conn.commit()
    affected = cur.rowcount
    conn.close()
    return affected > 0
