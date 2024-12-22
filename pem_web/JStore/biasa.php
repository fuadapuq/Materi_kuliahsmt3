<?php
// Memulai session untuk memeriksa login pengguna
session_start();

// Cek apakah pengguna sudah login dan memiliki role 'user'
if (!isset($_SESSION['role']) || $_SESSION['role'] !== 'user') {
    // Jika tidak, arahkan ke halaman login
    header("Location: login.php");
    exit();
}

// Jika pengguna memiliki role 'user', tampilkan form peminjaman
?>

<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Peminjaman Barang</title>
    <link rel="stylesheet" href="style.css"> <!-- Ganti dengan CSS jika diperlukan -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/remixicon@4.5.0/fonts/remixicon.css" rel="stylesheet"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css"/>
    <link rel="stylesheet" href="styles.css"> <!-- Gaya CSS -->
    <title>Admin Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        .container {
            width: 80%;
            margin: 30px auto;
            background-color: white;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
            color: #333;
        }

        h2 {
            color: #555;
        }

        p {
            font-size: 18px;
            color: #666;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }

        table, th, td {
            border: 1px solid #ddd;
        }

        th, td {
            padding: 12px;
            text-align: left;
        }

        th {
            background-color: #f2f2f2;
            color: #333;
        }

        tr:nth-child(even) {
            background-color: #f9f9f9;
        }

        tr:hover {
            background-color: #f1f1f1;
        }

        a {
            text-decoration: none;
            color: #007BFF;
        }

        a:hover {
            text-decoration: underline;
        }

        .logout-btn {
            display: inline-block;
            background-color: #ff4c4c;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            text-align: center;
            margin-top: 20px;
        }

        .logout-btn:hover {
            background-color: #ff1f1f;
        }

        .action-buttons {
            display: flex;
            gap: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
    <h2>Form Peminjaman Barang</h2>

    <form action="proses_pinjam.php" method="POST">
        <label for="barang">Pilih Barang:</label>
        <select name="barang" id="barang" required>
            <option value="handphone">iPhone 16 Pro</option>
            <option value="laptop">iPhone 15</option>
            <option value="tablet">Samsung ZFold</option>
        </select><br><br>

        <label for="jumlah">Jumlah Barang:</label>
        <input type="number" name="jumlah" id="jumlah" min="1" required><br><br>

        <label for="tanggal_pinjam">Tanggal Peminjaman:</label>
        <input type="date" name="tanggal_pinjam" id="tanggal_pinjam" required><br><br>

        <label for="tanggal_kembali">Tanggal Pengembalian:</label>
        <input type="date" name="tanggal_kembali" id="tanggal_kembali" required><br><br>

        <button type="submit">Ajukan Peminjaman</button>
        <a href="login.html" class="logout-btn">Logout</a> <!-- Tombol logout -->
    </form>
</body>
</html>