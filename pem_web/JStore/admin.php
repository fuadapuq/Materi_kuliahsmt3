<?php
// Start session
session_start();

// Cek apakah user sudah login dan memiliki role admin
if (!isset($_SESSION['username']) || $_SESSION['role'] !== 'admin') {
    // Jika tidak, redirect ke halaman login
    header("Location: login.php");
    exit();
}

// Mengambil informasi user dari session
$username = $_SESSION['username'];
$role = $_SESSION['role'];

// Koneksi ke database
$server = "localhost";
$user = "root";
$pass = "";
$db = "jstore";

$conn = new mysqli($server, $user, $pass, $db);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Query untuk mengambil data pengguna
$sql_user = "SELECT * FROM user"; // Mengambil semua data pengguna
$result_user = $conn->query($sql_user);

// Query untuk mengambil data barang
$sql_barang = "SELECT * FROM barang"; // Mengambil semua data barang
$result_barang = $conn->query($sql_barang);
?>

<!DOCTYPE html>
<html lang="en">
<head>
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
        <h1>Admin Dashboard</h1>
        <p>Welcome, <strong><?php echo htmlspecialchars($username); ?></strong>!</p>

        <!-- Daftar Pengguna -->
        <h2>Daftar Pengguna</h2>
        <?php if ($result_user->num_rows > 0): ?>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Username</th>
                        <th>Role</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <?php while ($row = $result_user->fetch_assoc()): ?>
                        <tr>
                            <td><?php echo $row['id']; ?></td>
                            <td><?php echo htmlspecialchars($row['username']); ?></td>
                            <td><?php echo htmlspecialchars($row['role']); ?></td>
                            <td class="action-buttons">
                                <a href="edit_user.php?id=<?php echo $row['id']; ?>">Edit</a> |
                                <a href="delete_user.php?id=<?php echo $row['id']; ?>" onclick="return confirm('Are you sure you want to delete this user?')">Delete</a>
                            </td>
                        </tr>
                    <?php endwhile; ?>
                </tbody>
            </table>
        <?php else: ?>
            <p>No users found.</p>
        <?php endif; ?>

        <!-- Daftar Barang -->
        <h2>Daftar Barang</h2>
        <?php if ($result_barang->num_rows > 0): ?>
            <table>
                <thead>
                    <tr>
                        <th>ID Barang</th>
                        <th>Nama Barang</th>
                        <th>Stok</th>
                        <th>Harga</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <?php while ($row = $result_barang->fetch_assoc()): ?>
                        <tr>
                            <td><?php echo $row['id_barang']; ?></td>
                            <td><?php echo htmlspecialchars($row['namabarang']); ?></td>
                            <td><?php echo htmlspecialchars($row['stok']); ?></td>
                            <td><?php echo htmlspecialchars($row['harga']); ?></td>
                            <td class="action-buttons">
                                <a href="edit_barang.php?id=<?php echo $row['id_barang']; ?>">Edit</a> |
                                <a href="delete_barang.php?id=<?php echo $row['id_barang']; ?>" onclick="return confirm('Are you sure you want to delete this item?')">Delete</a>
                            </td>
                        </tr>
                    <?php endwhile; ?>
                </tbody>
            </table>
        <?php else: ?>
            <p>No items found.</p>
        <?php endif; ?>

        <br>
        <a href="login.html" class="logout-btn">Logout</a> <!-- Tombol logout -->
    </div>
</body>
</html>

<?php
// Menutup koneksi database
$conn->close();
?>
