#! /usr/bin/env python3

import cgi 
import json

print("Content-type: text/html\n\n")
print("<!DOCTYPE html>")
print("<html lang='en'>")
print("<head>")
print("<title>Bookmark</title>")
print("<meta charset='utf-8'>")
print("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">")
print("<style>")
print("html * {")
print("    font-family: Montserrat Light, sans-serif;")
print("    }")
print("</style>")
print("</head>")
print("<body>")
print("<script language='Javascript'>")

print("  function Pergunta_Grupo() {")
print("      var selecao = document.getElementById('Grupo_Selecao')")
print("      if (selecao.value == 'GRX') {")
print("              document.getElementById(\"NC\").innerHTML='<input type=text name=NovoNome>'")
print("              }")
print("    }")

print("function expande_atualizacao() {")
print("    document.getElementById(\"E_Atualizacao\").innerHTML=\"    \\")
print("   <form name='atualiza' method=post action='Javascript:chama_atualizacao()'>\\")
print("     <h2> Adicionar ao Bookmark </h2><br>\\")
print("     <tr><td>     Site: </td><td><input type=text name=site></td></tr><br>\\")
print("     <tr><td>Descrição: </td><td><input type=text name=descricao></td></tr><br>\\")
print("     <select id=Grupo_Selecao name=Grupo_S onchange='Javascript:Pergunta_Grupo()'>\\")
print("     </select>\\")
print("     <div id='NC'></div>\\")
print("        <input type=submit value=Atualiza>\\")
print("     <div id='res_atualizacao'></div>\\")
print("   </form>\"")
print("   grupos = document.querySelectorAll('[tipo=\"Grupo\"]');")
print("   IdGrp = [];")
print("   Grp = [];")
print("  for (var i = 0; i < grupos.length; i++){")
print("     IdGrp.push(grupos[i].getAttribute(\"grupo\"));")
print("     Grp.push(grupos[i].innerHTML);")
print("   } ")
print("   IdGrp.push(\"GRX\");")
print("   Grp.push(\"Novo grupo\");")
print("   var selecao = document.getElementById(\"Grupo_Selecao\");")
print("   for (var i = 0; i < IdGrp.length; i++) {")
print("     var opcao = document.createElement(\"option\");")
print("         opcao.value = IdGrp[i];")
print("         opcao.text = Grp[i];")
print("         selecao.add(opcao, selecao.options[i])")
print("   }")
print("}")

print("function chama_atualizacao() {")
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
print("      self.xmlHttpReq.open('POST', '/cgi-bin/funcoes.py', true);")
print("      self.xmlHttpReq.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');")
print("      self.xmlHttpReq.onreadystatechange = function() {")
print("          if (self.xmlHttpReq.readyState == 4) {")
print("              document.getElementById('res_atualizacao').innerHTML = self.xmlHttpReq.responseText;")
print("              chama_funcao(\"bookmark\")")
print("              document.getElementById(\"E_Atualizacao\").innerHTML=\"<input type=\\\"button\\\" value=\\\"Atualizar o Bookmark?\\\" onclick=\\\"Javascript:expande_atualizacao()\\\">\" ")
print("          }")
print("      }")
print("      dados = document.forms[\"atualiza\"]")
print("    parametros = 'funcao=atualizar'+'&site='+escape(dados.site.value)+'&descricao='+escape(dados.descricao.value)+'&Grupo='+escape(dados.Grupo_S.value);")
print("    try {")
print("            parametros = parametros +'&NovoNome='+escape(dados.NovoNome.value);")
print("    } catch { };")
print("      self.xmlHttpReq.send(parametros);")
print("    }")

print("function excluir(){")
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
print("      self.xmlHttpReq.open('POST', '/cgi-bin/funcoes.py', true);")
print("      self.xmlHttpReq.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');")
print("      self.xmlHttpReq.onreadystatechange = function() {")
print("          if (self.xmlHttpReq.readyState == 4) {")
print("              document.getElementById('corpo').innerHTML = self.xmlHttpReq.responseText;")
print("              chama_funcao(\"bookmark\")")
print("          }")
print("      }")
print("      parametro = \"funcao=excluir\"")
print("      CheckBoxes = document.getElementById(\"Sel_Excluir\").elements;")
print("      selecionados = \"\"")
print("      for (i = 0; i < CheckBoxes.length; i++){")
print("              if (CheckBoxes[i].checked) {")
print("                      selecionados = selecionados + CheckBoxes[i].id + \";\";")
print("                      }")
print("              }")
print("      parametro = parametro+\"&selecao=\" + escape(selecionados);")
print("      self.xmlHttpReq.send(parametro);")    
print("    }")

print("function chama_funcao(func) {")
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
print("      self.xmlHttpReq.open('POST', '/cgi-bin/funcoes.py', true);")
print("      self.xmlHttpReq.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');")
print("      self.xmlHttpReq.onreadystatechange = function() {")
print("          if (self.xmlHttpReq.readyState == 4) {")
print("              document.getElementById('corpo').innerHTML = self.xmlHttpReq.responseText;")
print("          }")
print("      }")
print("      parametro = \"funcao=\" + func;")
print("      self.xmlHttpReq.send(parametro);")
print("    }")

print("</script>")

print("<h1>Bookmark</h1>")

print("<div id=\"E_Atualizacao\"><input type=\"button\" value=\"Atualizar o Bookmark?\" onclick=\"Javascript:expande_atualizacao()\"></div>")

print("<div id=\"Excluir\"><input type=\"button\" value=\"Excluir entrada no Bookmark?\" onclick='Javascript:chama_funcao(\"Sel_Excluir\")'></div>")
print("<div id='corpo'><script>chama_funcao(\"bookmark\")</script></div>")

print("<br>")
print("<br>")
print("<br>")
print("<a href=\"/bookmark.json\" download>Bookmark</a>")
        
print("</body>")
print("</html>")
        






