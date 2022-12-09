#! /usr/bin/env python3
# _*_ coding: UTF-8 _*_

import xml.etree.cElementTree as ET
import cgi

tree = ET.parse("../htdocs/bookmark.xml")
root = tree.getroot()

dados = cgi.FieldStorage()

S_site=dados["site"].value
S_descricao=dados["descricao"].value
S_Grupo=dados["Grupo"].value
try:
    S_NovoNome=dados["NovoNome"].value
except:
    S_NovoNome=""

print("Content-type: text/html\n\n")

StatusAtualizacao = "Não foi..."

if S_Grupo=="GRX":
    Grupo=ET.SubElement(root, "Grupo")
    Grupo.set("name", S_NovoNome)
    Grupo.set("", "GR" + str(len(root)+1))
    site=ET.SubElement(Grupo, "site")
    ET.SubElement(site, "field1", name = "href").text = S_site
    ET.SubElement(site, "field2", name = "descricao").text = S_descricao
    StatusAtualizacao = "Atualizado!"
else:
    for filho in root:
        if filho.attrib["id"] == S_Grupo:
            site = ET.SubElement(filho, "site")
            ET.SubElement(site, "field1", name = "href").text = S_site
            ET.SubElement(site, "field2", name = "descricao").text = S_descricao
            StatusAtualizacao = "Atualizado!"

print(StatusAtualizacao)
            
tree = ET.ElementTree(root)

## O arquivo que vai ser gravado tem que ter permissão de escrita para quem é de outros grupos
## quem executa é o Apache, então é outro grupo.
## Usar chmod 757

tree.write("../htdocs/bookmark.xml", encoding="utf-8")

