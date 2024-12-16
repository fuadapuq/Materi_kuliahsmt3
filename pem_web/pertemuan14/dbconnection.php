<?php
// membuat koneksi ke database
$host = "localhost";
$user = "root";
$pass = "";
$database = "sikampus";
$connect = mysqli_connect($host, $user, $pass, $database);
if (!$connect) {
    die("Koneksi gagal: " . mysqli_connect_error());
}else{
    echo "koneksi Berhasil";
} 