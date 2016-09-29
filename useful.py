#!/usr/bin/python
print 'content-type: text/html \n'

import cgitb
cgitb.enable()

import cgi

HTML_HEADER = """
<!DOCTYPE html>
<html>
<head><title>Hello</title></head>
<body>
"""

HTML_FOOTER = """
</body>
</html>
"""

data = cgi.FieldStorage()
name = data['name'].value

print HTML_HEADER
print '<center><h1>hello ' +  name + '</h1></center>'
print HTML_FOOTER
