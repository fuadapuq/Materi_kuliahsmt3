# menghapus transaksi penjualan jika jumlahnya itu lebih besar dari stok di tbl_barang
DELETE FROM tbl_detailtransaksi
WHERE qty > (
SELECT stok FROM tbl_barang)