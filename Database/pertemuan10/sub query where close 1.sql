SELECT * FROM tbl_barang WHERE stok >
(SELECT MAX(qty) FROM tbl_detailtransaksi)