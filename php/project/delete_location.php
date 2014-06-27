<?php
require("sqlajax_dbinfo.php");
if (!isset($_GET['id'])) {
	header("Location : phpsqlajax_map_v3.html");
} else {	
?>

<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8"/>
    <title>Google Maps AJAX + mySQL/PHP - Delete Locations</title>
  </head>
<body>

<?php
	$id = $_GET['id'];

	// Opens a connection to a MySQL server
	$connection=mysql_connect ("mysql.cs.wwu.edu", $username, $password);
	if (!$connection) {
	  die('Not connected : ' . mysql_error());
	}

	// Set the active MySQL database
	$db_selected = mysql_select_db($database, $connection);
	if (!$db_selected) {
	  die ('Can\'t use db : ' . mysql_error());
	}

	$query = "DELETE FROM `markers` WHERE id=$id";
	$result = mysql_query($query);
	if (!$result) {
	  die('Invalid query: ' . mysql_error());
	} else {
?>
<p>
Record Successfully Deleted!<br />
<a href="phpsqlajax_map_v3.html">Return to the Map View</a><br />
<a href="phpsqlajax_map_sat.html">Return to the Satellite View</a>
</p>
<?php
	}
}
?>
