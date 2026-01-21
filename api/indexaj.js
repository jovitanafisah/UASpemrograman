const express = require("express");
const sqlite3 = require("sqlite3").verbose();
const cors = require("cors");

const app = express();
app.use(express.json());
app.use(cors());
app.use(express.urlencoded({ extended: true }));

// Koneksi ke database

const db = new sqlite3.Database("../MyApp/UTS7.db", (err) => {
  if (err) {
    console.error("Database tidak bisa dibuka:", err.message);
  } else {
    console.log("Berhasil koneksi ke database UTS7.db");
  }
});

// =========================

// GET DATA With Pagination

// =========================

app.get("/pelanggan602", (req, res) => {
  let page = parseInt(req.query.page) || 1;
  let limit = parseInt(req.query.limit) || 10;
  let offset = (page - 1) * limit;

  const countQuery = "SELECT COUNT(*) AS total FROM pelanggan602";
  
  // Pastikan urutannya: ORDER BY -> LIMIT -> OFFSET
  const dataQuery = "SELECT * FROM pelanggan602 ORDER BY id DESC LIMIT ? OFFSET ?";

  db.get(countQuery, [], (err, countResult) => {
    if (err) return res.status(500).json({ error: err.message });

    // Pastikan parameter yang dikirim sesuai dengan jumlah tanda tanya (?)
    db.all(dataQuery, [limit, offset], (err, rows) => {
      if (err) return res.status(500).json({ error: err.message });

      res.json({
        total_data: countResult.total,
        page: page,
        limit: limit,
        total_page: Math.ceil(countResult.total / (limit || 1)), // Proteksi pembagian nol
        data: rows,
      });
    });
  });
});

// Endpoint 2: Get pelanggan by id

app.get("/pelanggan602/:id", (req, res) => {
  const query = "SELECT * FROM pelanggan602 WHERE id = ?";

  db.get(query, [req.params.id], (err, row) => {
    if (err) return res.status(500).json({ error: err.message });

    res.json(row);
  });
});

// Endpoint 3: Tambah pelanggan baru

app.post("/pelanggan602", (req, res) => {
  const { nama, alamat, telepon, email, jumlahpesanan } =
    req.body;

  const query = `

INSERT INTO pelanggan602 (nama, alamat, telepon, email, jumlahpesanan) 

VALUES (?, ?, ?, ?, ?)

`;

  db.run(
    query,
    [nama, alamat, telepon, email, jumlahpesanan],
    function (err) {
      if (err) return res.status(500).json({ error: err.message });

      res.json({
        message: "Data pelanggan602 berhasil ditambahkan",

        inserted_id: this.lastID,
      });
    }
  );
});

// Endpoint 4: Update pelanggan by id

app.put("/pelanggan602/:id", (req, res) => {
  const { nama, alamat, telepon, email, jumlahpesanan } =
    req.body;

  app.post("/pelanggan602", (req, res) => {
    const { nama, alamat, telepon, email, jumlahpesanan } =
      req.body;

    try {

      const query = `INSERT INTO pelanggan602 (nama, alamat, telepon, email, jumlahpesanan) VALUES (?, ?, ?, ?, ?) `;

      db.run(
        query,

        [nama, alamat, telepon, email, jumlahpesanan],

        function (err) {
          if (err) {
            return res.status(500).json({ error: err.message });
          }

          res.json({
            message: "Data pelanggan602 berhasil ditambahkan",

            inserted_id: this.lastID,
          });
        }
      );
    } catch (err) {
      res.status(500).json({ error: err.message });
    }
  });
  

 
    query = `

UPDATE pelanggan602 SET

nama = ?,
alamat = ?,
telepon = ?,
email = ?,
jumlahpesanan = ?
WHERE id = ?

`;
{
    params = [nama, alamat, telepon, email, jumlahpesanan, req.params.id];
  }

  db.run(query, params, function (err) {
    if (err) {
      return res.status(500).json({ error: err.message });
    }

    res.json({
      message: "Data pelanggan602 berhasil diperbarui",

      updated: this.changes,
    });
  });
});

// Endpoint 5: Delete pelanggan by id

app.delete("/pelanggan602/:id", (req, res) => {
  const query = "DELETE FROM pelanggan602 WHERE id = ?";

  db.run(query, [req.params.id], function (err) {
    if (err) return res.status(500).json({ error: err.message });

    res.json({ deleted: this.changes });
  });
});

// =========================

// GET DATA With Pagination

// =========================

app.get("/barang614", (req, res) => {
  let page = parseInt(req.query.page) || 1;
  let limit = parseInt(req.query.limit) || 10;
  let offset = (page - 1) * limit;

  const countQuery = "SELECT COUNT(*) AS total FROM barang614";
  
  const dataQuery = `SELECT * FROM barang614 ORDER BY id DESC LIMIT ? OFFSET ?`;

  db.get(countQuery, [], (err, countResult) => {
    if (err) return res.status(500).json({ error: err.message });

    db.all(dataQuery, [limit, offset], (err, rows) => {
      if (err) return res.status(500).json({ error: err.message });

      res.json({
        total_data: countResult.total,
        page: page,
        limit: limit,
        total_page: Math.ceil(countResult.total / limit),
        data: rows,
      });
    });
  });
});

// Endpoint 2: Get barang by id

app.get("/barang614/:id", (req, res) => {
  const query = "SELECT * FROM barang614 WHERE id = ?";

  db.get(query, [req.params.id], (err, row) => {
    if (err) return res.status(500).json({ error: err.message });

    res.json(row);
  });
});

// Endpoint 3: Tambah barang baru

app.post("/barang614", (req, res) => {
  const { nama, kategori, stok, harga, catatan } = req.body;

  const query = `
    INSERT INTO barang614 (nama, kategori, stok, harga, catatan)
    VALUES (?, ?, ?, ?, ?)
  `;

  db.run(
    query,
    [nama, kategori, stok, harga, catatan],
    function (err) {
      if (err) {
        return res.status(500).json({ error: err.message });
      }

      res.json({
        message: "Data barang berhasil ditambahkan",
        inserted_id: this.lastID,
      });
    }
  );
});

// Endpoint 4: Update barang by id

app.put("/barang614/:id", (req, res) => {
  const { nama, kategori, stok, harga, catatan } =
    req.body;

  const query = `UPDATE barang614 SET
nama = ?,
kategori = ?,
stok = ?,
harga = ?,
catatan = ?
WHERE id = ?`;

  const params = [nama, kategori, stok, harga, catatan, req.params.id];

  db.run(query, params, function (err) {
    if (err) {
      return res.status(500).json({ error: err.message });
    }

    res.json({
      message: "Data barang berhasil diperbarui",

      updated: this.changes,
    });
  });
});

// Endpoint 5: Delete barang by id

app.delete("/barang614/:id", (req, res) => {
  const query = "DELETE FROM barang614 WHERE id = ?"; 

  db.run(query, [req.params.id], function (err) {
    if (err) return res.status(500).json({ error: err.message });

    res.json({ deleted: this.changes });
  });
});

// Jalankan server

const PORT = 3000;

app.listen(PORT, () => {
  console.log("Server berjalan di port", PORT);
});