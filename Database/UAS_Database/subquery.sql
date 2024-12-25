SELECT 
    b.id_barang,
    b.harga_sewa,
    b.durasi_sewa
FROM 
    Barang b
WHERE 
    NOT EXISTS (
        SELECT 1 
        FROM Transaksi t
        WHERE b.id_barang = t.id_barang
    );
