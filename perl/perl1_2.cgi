#!/usr/bin/perl -w
# perl1_2.cgi
# Author: Chad Elofson
# Date: 1/19/2013
use CGI ':standard';
use Scalar::Util qw(looks_like_number);

# Coversions
$ltrPerGallon =  3.785411784;
$cndToUsd = 1.01;
$usdToCnd = 0.99;

if (param('clear')) {
	$result = "";
}

print header,start_html('CS 342 - Program 1 - perl1_2.cgi');
print '<FORM METHOD="POST" ACTION="perl1_2.cgi">';
print '<SELECT NAME="conversion">';
print '		<option VALUE="liters">US to Canada</option>';
print '		<option VALUE="gallons">Canada to US</option>';
print '</SELECT><BR />';
print 'Price: <INPUT TYPE="text" NAME="price" SIZE="10" > <br />' ;
print 'Quantity: <INPUT TYPE="text" NAME="quantity" SIZE="10" ><br />';

print '<INPUT TYPE="hidden" NAME="submitted" VALUE="true" > ';
print '<br /><br />';
print '<INPUT TYPE="submit" VALUE="Calculate" ><INPUT TYPE="reset" NAME="clear" VALUE="Clear" >';
print '</FORM>';
$posted = param('submitted');
if($posted) {
	if (looks_like_number(param('price')) && looks_like_number(param('quantity'))) {
		$convert = param('conversion');
		$price = param('price');
		$quantity = param('quantity');
		if ($convert eq 'liters') {
			$convertPrice = ($price*$usdToCnd)/$ltrPerGallon;
			$totalLiters = $quantity*$ltrPerGallon;
			$result = sprintf("$quantity gallons is %.2f liters at %.2f per liter ",$totalLiters,$convertPrice);
		} else {
			$convertPrice = $price*$cndToUsd*$ltrPerGallon;
			$totalGallons = $quantity/$ltrPerGallon;
			$result = sprintf("$quantity liters is %.2f gallons at %.2f per gallon ",$totalGallons,$convertPrice);
		}
		print '<br /><br />';		
		print '<FONT SIZE=4 COLOR="blue">';
		print $result;
		print '</FONT>';
	} else {
		print '<FONT SIZE=4 COLOR="red">';
		print 'PLEASE USE NUMBERS ONLY!';
		print '</FONT>';
	}
}
print end_html;
