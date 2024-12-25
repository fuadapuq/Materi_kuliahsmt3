ALTER TABLE transaksi
ADD CONSTRAINT fk_user
FOREIGN KEY (id_user) REFERENCES users(id_user);