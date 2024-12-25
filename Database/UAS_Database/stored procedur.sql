DELIMITER $$

CREATE PROCEDURE add_transaksi (
    IN p_id_transaksi VARCHAR(10),
    IN p_id_users VARCHAR(10),
    IN p_id_barang VARCHAR(10),
    IN p_total_harga INT,
    IN p_tgl_transaksi DATE,
    IN p_tgl_selesai DATE
)
BEGIN
    INSERT INTO transaksi (id_transaksi, id_user, id_barang, total_harga, tgl_transaksi, tgl_selesai)
    VALUES (p_id_transaksi, p_id_user, p_id_barang, p_total_harga, p_tgl_transaksi, p_tgl_selesai);
END$$

DELIMITER ;
