#menampilkan total jumlah barang yg sudah dilakukan pengadaan
SELECT nama_barang, 
(select SUM(jumlah) AS jumlah_brg
FROM tbl_detail_pengadaan 
WHERE
tbl_detail_pengadaan.kode_pengadaan =
tbl_barang.kode_barang) AS jml_pengadaan
FROM tbl_barang; 