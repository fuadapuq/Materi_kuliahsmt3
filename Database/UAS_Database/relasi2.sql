ALTER TABLE transaksi
ADD CONSTRAINT fk_barang
FOREIGN KEY (id_barang) REFERENCES barang(id_barang);
