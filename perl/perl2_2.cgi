#!/usr/bin/perl -w
# perl1_1.cgi
# Author: Chad Elofson
# Date: 1/30/2013
use CGI ':standard';
print header,start_html('CS 342 - Program 2 - perl2_2.cgi');
$correct = 0;
@right = ('F','F','F','F','F');

#Print the form
print '<FORM METHOD="POST" ACTION="perl2_2.cgi">';
print "\n";
print '<p>';
print "\n";
print '1. What year did the Seattle Seahawks make the Super Bowl?';
print "\n";
if (param('postback')) {
	if (param('seahawks') =~ /2/) {
		$correct++;
		$right[0] = 'T';
		print '<IMG SRC="right.png" ALT="Correct" WIDTH="25" HEIGHT="25">';
		print "\n";
	} else {
		print '<IMG SRC="wrong.png" ALT="Incorrect" WIDTH="25" HEIGHT="25">';
		print "\n";
	}
}
print '<br />';
print '<INPUT TYPE="radio" NAME="seahawks" VALUE="1">1983<br />';
print "\n";
print '<INPUT TYPE="radio" NAME="seahawks" VALUE="2">2005<br />';
print "\n";
print '<INPUT TYPE="radio" NAME="seahawks" VALUE="3">2012<br />';
print "\n";
print '<INPUT TYPE="radio" NAME="seahawks" VALUE="4">2013<br />';
print '</p>';
print '<br /><br />';

print '<p>';
print "\n";
print '2. What is the name of the new Zombie TV Series?';
print "\n";
if (param('postback')) {
	if (param('twd') =~ /3/) {
		$correct++;
		$right[1] = 'T';
		print '<IMG SRC="right.png" ALT="Correct" WIDTH="25" HEIGHT="25">';
		print "\n";
	} else {
		print '<IMG SRC="wrong.png" ALT="Incorrect" WIDTH="25" HEIGHT="25">';
		print "\n";
	}
}
print '<br />';
print '<INPUT TYPE="radio" NAME="twd" VALUE="1">Zombie Land<br />';
print "\n";
print '<INPUT TYPE="radio" NAME="twd" VALUE="2">Dawn of the Dead<br />';
print "\n";
print '<INPUT TYPE="radio" NAME="twd" VALUE="3">The Walking Dead<br />';
print "\n";
print '<INPUT TYPE="radio" NAME="twd" VALUE="4">World War Z<br />';
print '</p>';
print '<br /><br />';

print '<p>';
print "\n";
print '3. What year did I start at Western?';
print "\n";
if (param('postback')) {
	if (param('wwu') =~ /2/) {
		$correct++;
		$right[2] = 'T';
		print '<IMG SRC="right.png" ALT="Correct" WIDTH="25" HEIGHT="25">';
		print "\n";
	} else {
		print '<IMG SRC="wrong.png" ALT="Incorrect" WIDTH="25" HEIGHT="25">';
		print "\n";
	}
}
print '<br />';
print "\n";
print '<INPUT TYPE="radio" NAME="wwu" VALUE="1">2009<br />';
print "\n";
print '<INPUT TYPE="radio" NAME="wwu" VALUE="2">2010<br />';
print "\n";
print '<INPUT TYPE="radio" NAME="wwu" VALUE="3">2011<br />';
print "\n";
print '<INPUT TYPE="radio" NAME="wwu" VALUE="4">2012<br />';
print '</p>';
print '<br /><br />';

print '<p>';
print "\n";
print '4. What year did the Seattle Mariners win 116 games?';
print "\n";
if (param('postback')) {
	if (param('mariners') =~ /4/) {
		$correct++;
		$right[3] = 'T';
		print '<IMG SRC="right.png" ALT="Correct" WIDTH="25" HEIGHT="25">';
		print "\n";
	} else {
		print '<IMG SRC="wrong.png" ALT="Incorrect" WIDTH="25" HEIGHT="25">';
		print "\n";
	}
}
print '<br />';
print "\n";
print '<INPUT TYPE="radio" NAME="mariners" VALUE="1">1983<br />';
print "\n";
print '<INPUT TYPE="radio" NAME="mariners" VALUE="2">2005<br />';
print "\n";
print '<INPUT TYPE="radio" NAME="mariners" VALUE="3">2010<br />';
print "\n";
print '<INPUT TYPE="radio" NAME="mariners" VALUE="4">2001<br />';
print '</p>';
print '<br /><br />';

print '<p>';
print "\n";
print '5. What is my favorie sport?';
print "\n";
if (param('postback')) {
	if (param('last') =~ /1/) {
		$correct++;
		$right[4] = 'T';
		print '<IMG SRC="right.png" ALT="Correct" WIDTH="25" HEIGHT="25">';
		print "\n";
	} else {
		print '<IMG SRC="wrong.png" ALT="Incorrect" WIDTH="25" HEIGHT="25">';
		print "\n";
	}
}
print '<br />';
print "\n";
print '<INPUT TYPE="radio" NAME="last" VALUE="1">Bowling<br />';
print "\n";
print '<INPUT TYPE="radio" NAME="last" VALUE="2">Basketball<br />';
print "\n";
print '<INPUT TYPE="radio" NAME="last" VALUE="3">Football<br />';
print "\n";
print '<INPUT TYPE="radio" NAME="last" VALUE="4">Soccer<br />';
print "\n";
print '</p>';
print "\n";
print '<br /><br />';
print "\n";
print '<INPUT TYPE="hidden" NAME="postback" value="true" />';
print '<INPUT TYPE="submit" NAME="submit" VALUE="Submit" />';
print "\n";
print '<INPUT TYPE="reset" NAME="reset" VALUE="Clear" />';
print '</FORM>';
print "\n\n";

$percent = 100*($correct/5);
$result =  sprintf("%.2f %",$percent);
if (param('postback')) {
	print '<TABLE border="1">';
	print '<TH>Details</TH><TH>Values</TH>';
	print '<TR>';
	print '<TD>Correct:</TD><TD>' . $correct . '</TD>';
	print '</TR>';
	print '<TR>';
	print '<TD>Percent:</TD><TD>' . $result . '</TD>';
	print '</TR>';
	print '<TR>';
	print '<TD>Answers:</TD>';
	print '<TD>';
	if ($right[0] =~ /T/) {
		print '#1 2005';
		if ($right[1] =~ /T/ || $right[2] =~ /T/ || $right[3] =~ /T/ || $right[4] =~ /T/) {
			print '<BR />';
		}
	}
	if ($right[1] =~ /T/) {
		print '#2 The Walking Dead';
		if ($right[2] || $right[3] || $right[4] =~ /T/) {
			print '<BR />';
		}
	}
	if ($right[2] =~ /T/) {
		print '#3 2010';
		if ($right[3] =~ /T/ || $right[4] =~ /T/) {
			print '<BR />';
		}
	}
	if ($right[3] =~ /T/) {
		print '#4 2001';
		if ($right[4] =~ /T/) {
			print '<BR />';
		}
	}
	if ($right[4] =~ /T/) {
		print '#5 Bowling';
	}
	print '</TD>';
	print '</TR>';
	print '</TABLE>';
}
print end_html;
