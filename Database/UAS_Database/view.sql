CREATE VIEW view_transaksi_lengkap AS
SELECT 
    t.id_transaksi,
    u.nama_user,
    b.id_barang,
    b.harga_sewa,
    t.total_harga,
    t.tgl_transaksi,
    t.tgl_selesai
FROM 
    transaksi t
JOIN 
    users u ON t.id_user = u.id_user
JOIN 
    barang b ON t.id_barang = b.id_barang;
