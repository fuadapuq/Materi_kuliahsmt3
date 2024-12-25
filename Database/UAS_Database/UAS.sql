-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.30 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for uas_database
CREATE DATABASE IF NOT EXISTS `uas_database` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `uas_database`;

-- Dumping structure for table uas_database.barang
CREATE TABLE IF NOT EXISTS `barang` (
  `id_barang` varchar(10) NOT NULL,
  `harga_sewa` int DEFAULT NULL,
  `durasi_sewa` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_barang`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table uas_database.barang: ~3 rows (approximately)
REPLACE INTO `barang` (`id_barang`, `harga_sewa`, `durasi_sewa`) VALUES
	('BRG001', 650000, '1 hari'),
	('BRG002', 600000, '1 hari'),
	('BRG007', 700000, '2 hari');

-- Dumping structure for table uas_database.tbl_barang
CREATE TABLE IF NOT EXISTS `tbl_barang` (
  `kode_barang` varchar(20) NOT NULL,
  `nama_barang` varchar(50) DEFAULT NULL,
  `harga_sewa` int DEFAULT NULL,
  PRIMARY KEY (`kode_barang`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table uas_database.tbl_barang: ~0 rows (approximately)
REPLACE INTO `tbl_barang` (`kode_barang`, `nama_barang`, `harga_sewa`) VALUES
	('BRG_001', 'Iphone 16 Pro Max', 650000),
	('BRG_002', 'Iphone 16', 600000),
	('BRG_003', 'Iphone 15', 550000),
	('BRG_004', 'Samsung zflip', 500000),
	('BRG_005', 'Samsung zfold', 450000),
	('BRG_006', 'Macbook Pro', 700000),
	('BRG_007', 'TUF gaming', 400000);

-- Dumping structure for table uas_database.tbl_detailtransaksi
CREATE TABLE IF NOT EXISTS `tbl_detailtransaksi` (
  `kode_faktur` varchar(20) DEFAULT NULL,
  `kode_barang` varchar(20) DEFAULT NULL,
  `qty` int DEFAULT NULL,
  KEY `kode_faktur` (`kode_faktur`),
  KEY `kode_barang` (`kode_barang`),
  CONSTRAINT `tbl_detailtransaksi_ibfk_1` FOREIGN KEY (`kode_faktur`) REFERENCES `tbl_faktur` (`kode_faktur`),
  CONSTRAINT `tbl_detailtransaksi_ibfk_2` FOREIGN KEY (`kode_barang`) REFERENCES `tbl_barang` (`kode_barang`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table uas_database.tbl_detailtransaksi: ~7 rows (approximately)
REPLACE INTO `tbl_detailtransaksi` (`kode_faktur`, `kode_barang`, `qty`) VALUES
	('KD_001', 'BRG_001', 10),
	('KD_001', 'BRG_002', 9),
	('KD_001', 'BRG_003', 8),
	('KD_002', 'BRG_004', 7),
	('KD_002', 'BRG_005', 6),
	('KD_003', 'BRG_006', 5),
	('KD_003', 'BRG_007', 4);

-- Dumping structure for table uas_database.tbl_faktur
CREATE TABLE IF NOT EXISTS `tbl_faktur` (
  `kode_faktur` varchar(20) NOT NULL,
  `tanggal` date DEFAULT NULL,
  PRIMARY KEY (`kode_faktur`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table uas_database.tbl_faktur: ~3 rows (approximately)
REPLACE INTO `tbl_faktur` (`kode_faktur`, `tanggal`) VALUES
	('KD_001', '2024-10-13'),
	('KD_002', '2024-11-13'),
	('KD_003', '2024-12-14');

-- Dumping structure for table uas_database.transaksi
CREATE TABLE IF NOT EXISTS `transaksi` (
  `id_transaksi` varchar(10) NOT NULL,
  `id_user` varchar(10) DEFAULT NULL,
  `id_barang` varchar(10) DEFAULT NULL,
  `total_harga` int DEFAULT NULL,
  `tgl_transaksi` date DEFAULT NULL,
  `tgl_selesai` date DEFAULT NULL,
  KEY `id_transaksi` (`id_transaksi`),
  KEY `fk_barang` (`id_barang`),
  CONSTRAINT `fk_barang` FOREIGN KEY (`id_barang`) REFERENCES `barang` (`id_barang`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table uas_database.transaksi: ~2 rows (approximately)
REPLACE INTO `transaksi` (`id_transaksi`, `id_user`, `id_barang`, `total_harga`, `tgl_transaksi`, `tgl_selesai`) VALUES
	('', 'IDS001', 'BRG001', 650000, '2024-12-12', '2024-12-13'),
	('', 'IDS002', 'BRG002', 600000, '2024-12-12', '2024-12-13');

-- Dumping structure for table uas_database.users
CREATE TABLE IF NOT EXISTS `users` (
  `id_user` varchar(10) NOT NULL,
  `nama_user` varchar(100) NOT NULL,
  PRIMARY KEY (`id_user`),
  CONSTRAINT `FK_users_transaksi` FOREIGN KEY (`id_user`) REFERENCES `transaksi` (`id_transaksi`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table uas_database.users: ~0 rows (approximately)

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
