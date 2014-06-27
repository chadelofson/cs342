<?php
$filename = "journal.txt";
$username = $_GET["user"];
$entrySet = false;
$displaySet = false;
$clearSet = false;
if (isset($_POST["journalpost"])) {
	$username = $_POST["user"];
	$entry = $_POST["journalentry"];
	if (isset($_POST["entry"])) {
		
		$date = date("m-d-Y");
		$line = "$username,$entry,$date\n";
		file_put_contents($filename,$line,FILE_APPEND);
		$entrySet = true;
	}
	
	if (isset($_POST["display"])) {
		$displaySet = true;
	}
	if (isset($_POST["clear"])) {
		
		$clearSet = true;
	}
	
}
?>
<!DOCTYPE HTML>
<html>
<body>
<form action="journal.php" method="post">
<textarea name="journalentry" rows="4" columns="50">
</textarea>
<br />
<input type="hidden" name="journalpost" value="true" >
<input type="hidden" name="user" value="<?php echo $username; ?>">
<input type="submit" name="entry" value="Add Entry" >
<input type="submit" name="display" value="Display">
<input type="submit" name="clear" value="Clear">
</form>
<br />
<?php 
if (isset($_POST["journalpost"]) && $displaySet) {	
	$file = fopen($filename,"r");
	while (!feof($file)) {
		$line = fgets($file);
		echo "$line<br />\n";
	}
	fclose($file);
}

if (isset($_POST["journalpost"]) && $entrySet) {
	echo '<font color="blue">Entry added!</font>';
}
if (isset($_POST["journalpost"]) && $clearSet) {
	echo '<font color="blue">Entry added!</font>';
}
?>
</body>
</html>
