CREATE TABLE Transaksi (
    id_transaksi VARCHAR(10) PRIMARY KEY,
    id_user VARCHAR(10),
    id_barang VARCHAR(10),
    total_harga INT,
    tgl_transaksi DATE,
    tgl_selesai DATE
);