SELECT tbl_detailtransaksi.kode_faktur,
tbl_detailtransaksi.kode_barang,
tbl_barang.nama_barang, tbl_barang.harga
FROM tbl_barang RIGHT JOIN tbl_detailtransaksi ON
tbl_detailtransaksi.kode_barang = tbl_barang.kode_barang