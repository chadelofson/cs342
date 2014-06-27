#!/usr/bin/perl -w
# perl1_3.cgi
# Author: Chad Elofson
# Date: 1/19/2013
use CGI ':standard';
use Scalar::Util qw(looks_like_number);
use Switch '__';

print header,start_html('CS 342 - Program 1 - perl1_3.cgi');
print '<FORM METHOD="POST" ACTION="perl1_3.cgi">';
print '<INPUT TYPE="text" NAME="program" WIDTH="30" />';
print '<INPUT TYPE="hidden" NAME="submitted" VALUE="true" > ';
print '<br /><br />';
print '<INPUT TYPE="submit" VALUE="Calculate" ><INPUT TYPE="reset" VALUE="Clear" >';
print '</FORM>';
if (param('submitted')) {
	my $result = param('program');
	my @operation = split(/ /,$result);
	#print $operation[0] . ' ' . $operation[1] . ' ' . $operation[2];
	if (looks_like_number($operation[0]) && looks_like_number($operation[2])) {
		$operator = uc $operation[1];
		switch($operator) {
			case (__ eq "PLUS") 	{ $output = sprintf("%d PLUS %d = %d",$operation[0],$operation[2],$operation[0]+$operation[2]);}
			case (__ eq "MINUS") 	{ $output = sprintf("%d MINUS %d = %d",$operation[0],$operation[2],$operation[0]-$operation[2]);}			
			case (__ eq "TIMES") 	{ $output = sprintf("%d TIMES %d = %d",$operation[0],$operation[2],$operation[0]*$operation[2]);}
			case (__ eq "OVER") 	{ $output = sprintf("%d OVER %d = %d",$operation[0],$operation[2],$operation[0]/$operation[2]);}
		}
		print '<br /><br />';		
		print '<FONT SIZE=4 COLOR="blue">';
		print $output;
		print '</FONT>';
	} elsif (looks_like_number($operation[1]) && looks_like_number($operation[2])) { 
		$operator = uc $operation[0];
		switch($operator) {
			case (__ eq "SUM") { $output = sprintf("SUM %d %d = %d",$operation[1],$operation[2],$operation[1]+$operation[2]); }
			case (__ eq "AVG") { $output = sprintf("AVG %d %d = %d",$operation[1],$operation[2],($operation[1]+$operation[2])/2); }
		}
		print '<br /><br />';		
		print '<FONT SIZE=4 COLOR="blue">';
		print $output;
		print '</FONT>';
	} else {
		print "<BR /><BR />";
		print '<FONT SIZE=4 COLOR="red">';
		print "Invalid input: NUMBER OPERATOR NUMBER or OPERATOR NUMBER NUMBER";
		print '</FONT>';
	}
}

print end_html;
