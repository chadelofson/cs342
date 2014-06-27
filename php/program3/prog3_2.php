<?php
if (isset($_POST["postback"])) {
	$username = $_POST["username"];
	$password = $_POST["password"];
	$validUser = false;
	
	// File names
	$userfile = "user.txt";
	
	// Open the user file and verify the username and password
	$file = fopen($userfile,"r");
	while (!feof($file)) {
		$line = fgets($file);
		$info = split(",",$line);
		if (strcmp($info[0],$username) == 0 && strcmp($info[1],$password) == 0) {
			$validUser = true;
			break;
		}
	}
	fclose($file);

	if ($validUser) { // If a valid user then bring up the journal information
		header("Location:journal.php?user=$username");
		exit;	
	} else { // Otherwise load the code below
?>
<a href="prog3_2.php">Exit Application</a><br />
<a href="createuser.php">Create New User</a>
<?php
	}
} else {
?>
<!DOCTYPE HTML>
<html>
<body>
<form action="prog3_2.php" method="post">
UserName: <input type="text" name="username" /><br />
Password: <input type="password" name="password" /><br />
<input type="hidden" name="postback" value="true" />
<input type="submit" name="valid" value="login" />
</form>


</body>
</html>

<?php
}
?>
