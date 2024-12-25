DELIMITER $$

CREATE FUNCTION total_pendapatan()
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE total INT;
    SELECT SUM(total_harga) INTO total FROM transaksi;
    RETURN total;
END$$

DELIMITER ;
