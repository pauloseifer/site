import xml.etree.cElementTree as ET

arquivo = input("Arquivo: ")
arq = open(arquivo, "r")

tree = ET.parse(arq)

root = tree.getroot()

print("<!DOCTYPE html>")
print("<html lang='en'>")
print("<head>")
print("<title>Bookmark</title>")
print("</head>")
print("<body>")

for child in root:
    print("<h1>" + child.get("name") + "</h1>")
    
    for child2 in child:
        site = child2.find("field1").text
        descricao = child2.find("field2").text
        print("<a href=" + site + ">" + descricao + "</a>")
        
print("</body>")
print("</html>")
        
arq.close()





