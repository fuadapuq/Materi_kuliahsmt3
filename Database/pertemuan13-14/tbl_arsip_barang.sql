CREATE TABLE tbl_arsip_barang (
    id_arsip INT AUTO_INCREMENT PRIMARY KEY,
    kode_barang VARCHAR(10) NOT NULL,
    nama_barang VARCHAR(100) NOT NULL,
    stok INT NOT NULL,
    waktu_hapus DATETIME NOT NULL
);

-- Menghapus data dari tbl_barang
DELETE FROM tbl_barang WHERE kode_barang = 'BRG_001';

-- Periksa tabel arsip
SELECT * FROM tbl_arsip_barang;