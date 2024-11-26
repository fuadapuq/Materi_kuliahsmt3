SELECT * FROM tbl_pengadaan WHERE kode_supplier
IN ( SELECT kode_supplier FROM supplier
WHERE nama_supplier LIKE "PT. ABC")