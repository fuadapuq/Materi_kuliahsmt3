<?php
// Start session
session_start();

$server = "localhost";
$user = "root";
$pass = "";
$db = "jstore";

// Create database connection
$conn = new mysqli($server, $user, $pass, $db);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Retrieve form data
    $username = trim($_POST['username']);
    $password = trim($_POST['password']);
    
    // Prepare the SQL statement to check the username
    $stmt = $conn->prepare("SELECT * FROM user WHERE username = ?");
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $result = $stmt->get_result();

    // Check if a user with the provided username exists
    if ($result->num_rows == 1) {
        $row = $result->fetch_assoc();
        
        // Verify the password
        if (password_verify($password, $row['password'])) {
            // Store user data in session
            $_SESSION['username'] = $row['username'];
            $_SESSION['role'] = $row['role'];

            // Redirect based on user role
            if ($row['role'] == 'admin') {
                header("Location: admin.php"); // Redirect to admin dashboard
                exit();
            } else {
                // Redirect to user dashboard
                header("Location: biasa.php");
                exit();
            }
        } else {
            echo "Username atau Password salah!";
        }
    } else {
        echo "Username atau Password salah!";
    }
    $stmt->close();
}

$conn->close();
?>
