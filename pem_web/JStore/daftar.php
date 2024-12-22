<?php
// Connection to the database
$host = 'localhost';
$dbname = 'jstore';
$username = 'root';
$password = '';

try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Connection failed: " . $e->getMessage());
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = htmlspecialchars(trim($_POST['username']));
    $password = password_hash(trim($_POST['password']), PASSWORD_BCRYPT);
    $email = htmlspecialchars(trim($_POST['email']));

    // Check if email already exists
    $checkEmail = $pdo->prepare("SELECT COUNT(*) FROM user WHERE email = :email");
    $checkEmail->execute([':email' => $email]);
    
    if ($checkEmail->fetchColumn() > 0) {
        echo "<p>Email already registered. Please <a href='daftar.html'>try again</a> with a different email.</p>";
        exit;
    }

    // Insert into database
    $sql = "INSERT INTO user (username, email, role, password) VALUES (:username, :email, 'user', :password)";
    $stmt = $pdo->prepare($sql);

    try {
        $stmt->execute([
            ':username' => $username,
            ':password' => $password,
            ':email' => $email
        ]);
        echo "<p>Registration successful! <a href='login.html'>Go to login</a>.</p>";
    } catch (PDOException $e) {
        echo "<p>Error: " . $e->getMessage() . "</p>";
    }
}
?>
