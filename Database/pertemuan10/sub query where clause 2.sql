SELECT * FROM tbl_barang WHERE stok <
(SELECT AVG(stok) FROM tbl_barang)