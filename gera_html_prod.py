#! /usr/bin/env python3

import xml.etree.cElementTree as ET

arq = open("../htdocs/bookmark.xml", "r")

tree = ET.parse(arq)

root = tree.getroot()

print("Content-type: text/html\n\n")
print("<!DOCTYPE html>")
print("<html lang='en'>")
print("<head>")
print("<title>Bookmark</title>")
print("<meta name='viewport' content='width=device-width, initial-scale=1.0'>")
print("<meta charset='utf-8'>")
print("</head>")
print("<body>")

for child in root:
    print("<h1><font face='Montserrat Light'>" + child.get("name") + "</font></h1>")
    
    for child2 in child:
        site = child2.find("field1").text
        descricao = child2.find("field2").text
        print("<a href=" + site + "><font face='Montserrat Light'>" + descricao + "</font></a><br>")
        
print("</body>")
print("</html>")
        
arq.close()





