#!/usr/local/bin/python
# Program to display CGI 

import os
import cgi

def printHeader( title ):               # Used to write header information
   print """Content-type: text/html

<?xml version = "1.0" encoding = "UTF-8"?>    
<!DOCTYPE html PUBLIC
   "-//W3C//DTD XHTML 1.0 Strict//EN"
   "DTD/xhtml1-strict.dtd">
<html xmlns = "http://www.w3.org/1999/xhtml">
<head><title>%s</title></head>

<body>""" % title

printHeader("CSCI 342 - Program 5 - program5_1.cgi")

path = "images"             # List of the directory where the images are
dirList = os.listdir(path)                                              # Get the list of files
for imageName in dirList:                                               # For every image file in the listing
    print """
<p>
<img  src='images/%s' alt='%s' /><br />                        
<b>%s</b></p>""" % (imageName,imageName,imageName.replace(".jpg",".txt"))

print """</table></body></html>"""
