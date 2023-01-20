#! /bin/env python3

import xml.etree.ElementTree as ET
import json
import datetime

tree = ET.parse("/home/pseifer/repoprogs/site/bookmark.xml")
root = tree.getroot()

bookm = {}
ngrupo = 1
nsubgrupo = 1

bookm["Descrição = "] = "Registro de sites interessantes e temporários"
bookm["Autor = "] = "Paulo Seifer"
bookm["Última atualização"] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

for child in root:
  bookm["GR_"+str(ngrupo)] = {}
  grupo = child.get("name")
  bookm["GR_" + str(ngrupo)]["Grupo"] = grupo
  nsubgrupo = 1
  for child2 in child:
    site = child2.find("field1").text
    descricao = child2.find("field2"). text
    bookm["GR_" + str(ngrupo)]["GR_" + str(ngrupo) + "_" + str(nsubgrupo)] = {}
    bookm["GR_" + str(ngrupo)]["GR_" + str(ngrupo) + "_" + str(nsubgrupo)]["site"] = site
    bookm["GR_" + str(ngrupo)]["GR_" + str(ngrupo) + "_" + str(nsubgrupo)]["descrição"] = descricao
    nsubgrupo += 1
  nsubgrupo = 1
  ngrupo += 1

bookmjson = json.dumps(bookm, indent = 3, ensure_ascii=False).encode("utf-8")
  
print(bookmjson.decode())

with open('bookmark.json', 'w', encoding='utf-8') as f:
    json.dump(bookm, f, ensure_ascii=False, indent=4)
