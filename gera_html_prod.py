#! /usr/bin/env python3

import xml.etree.cElementTree as ET
import cgi 

arq = open("../htdocs/bookmark.xml", "r")

tree = ET.parse(arq)

root = tree.getroot()

entrada = cgi.FieldStorage()

StatusAtualizacao = ""

try:
    for i in entrada.keys():
        StatusAtualizacao = entrada[i].value
except:
    StatusAtualizacao = "opa!"

print("Content-type: text/html\n\n")
print("<!DOCTYPE html>")
print("<html lang='en'>")
print("<head>")
print("<title>Bookmark</title>")
print("<meta charset='utf-8'>")
print("<style>")
print("html * {")
print("    font-family: Montserrat Light, sans-serif;")
print("    }")
print("</style>")
print("</head>")
print("<body>")

print("<script language='Javascript'>")
print("  function Pergunta_Grupo() {")
print("      var selecao = document.getElementById('Grupo')")
print("      if (selecao.value == 'Nova categoria') {")
print("              document.getElementById('NC').innerHTML='<input type=text name=NovoNome>'")
print("              }")
print("    }")

print("function chama_atualizacao(strURL) {")
print("      var xmlHttpReq = false;")
print("      var self = this;")
print("      // Mozilla/Safari")
print("      if (window.XMLHttpRequest) {")
print("	  self.xmlHttpReq = new XMLHttpRequest();")
print("      }")
print("      // IE")
print("      else if (window.ActiveXObject) {")
print("          self.xmlHttpReq = new ActiveXObject('Microsoft.XMLHTTP');")
print("      }")
print("      self.xmlHttpReq.open('POST', strURL, true);")
print("      self.xmlHttpReq.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');")
print("      self.xmlHttpReq.onreadystatechange = function() {")
print("          if (self.xmlHttpReq.readyState == 4) {")
print("              document.getElementById('res_atualizacao').innerHTML = self.xmlHttpReq.responseText;")
print("          }")
print("      }")
print("      dados = document.forms[\"atualiza\"]")
print("    parametros = 'site='+escape(dados.site.value)+'&descricao='+escape(dados.descricao.value)+'&Grupo='+escape(dados.Grupo.value);")
print("    try {")
print("            parametros = parametros +'&NovoNome='+escape(dados.NovoNome.value);")
print("    } catch { };")
print("      self.xmlHttpReq.send(parametros);")
print("    }")

print("</script>")

lista = []
idgrupo = []

for filho in root:
    lista.append(filho.attrib["name"])
    idgrupo.append(filho.attrib["id"])
lista.append("Nova categoria")
idgrupo.append("GRX")

print("<form name=\"atualiza\" method=post action='Javascript:chama_atualizacao(\"/cgi-bin/atualiza.py\")'>") ## accept-charset=\"utf-8\">")
print("  <h1> Adiciona ao Bookmkark </h1><br>")
print("  <tr><td>     Site: </td><td><input type=text name=site></td></tr><br>")
print("  <tr><td>Descrição: </td><td><input type=text name=descricao></td></tr><br>")
print("	 <select id=Grupo name=Grupo onchange='Javascript:Pergunta_Grupo()'>")
for j, i in zip(idgrupo, lista):
     print("<option value='" + j + "'>" + i + "</option>")
print("</select>")
print("<div id='NC'></div>")
print("     <input type=submit value=Atualiza>")
print("<div id='res_atualizacao'></div>")
print("</form>")

for child in root:
    print("<h1>" + child.get("name") + "</h1>")
    
    for child2 in child:
        site = child2.find("field1").text
        descricao = child2.find("field2").text
        print("<a href=" + site + ">" + descricao + "</a><br>")
        
print("</body>")
print("</html>")
        
arq.close()





