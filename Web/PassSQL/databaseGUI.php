<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['username']) && isset($_POST['password'])) {
        $uname = $_POST['username'];
        $passwd = $_POST['password'];

        $conn = new mysqli("localhost", "hackable", "abc123", "ownedsite");

        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }

        $sql = "SELECT * FROM person WHERE nickname='$uname' AND Password='$passwd' LIMIT 1";
        $result = $conn->query($sql);

        if ($result != False && $result->num_rows != 0) {
            echo "flag_{GRAY_FEDORA_HATS}";
        } else {
            echo "Invalid Login!";
        }
    }
} else {
    echo <<<EOT
<!DOCTYPE html>
<html>
	<head>
		<title>Long Addition & Subtraction</title>
		<script type="text/javascript" charset="UTF-8" src="standard.js"></script>
		<link rel="stylesheet" type="text/css" charset="UTF-8" media="all" href="standard.css">
	</head>
	<body>
		<div id="main">
            <div class="island" style="border: 10px solid #ffffff">
                Grayhats Gray Router 2.0 Login
            </div>
            
            <div class="island">
                <form type="input" action="
EOT;
    echo $_SERVER["REQUEST_URI"] . "\" ";
    echo <<<EOT
method="POST">
                    Username: <input type="text" name="username" id="uname"> <br>
                    Password: <input type="password" name="password" id="pass"> <br>
                    <br> <input type="submit" id="submitLogin"> <br>
                </form>
            </div>
		</div>
	</body>
</html>
EOT;
}
?>
