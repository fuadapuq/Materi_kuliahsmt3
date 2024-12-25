SELECT 
    b.id_barang,
    b.harga_sewa,
    COUNT(t.id_transaksi) AS jumlah_sewa
FROM 
    Transaksi t
JOIN 
    Barang b ON t.id_barang = b.id_barang
GROUP BY 
    b.id_barang, b.harga_sewa
HAVING 
    COUNT(t.id_transaksi) > 1
ORDER BY 
    jumlah_sewa DESC;
