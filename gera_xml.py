import xml.etree.cElementTree as ET

root = ET.Element("Bookmark")
arquivo = input("Arquivo: ")

arq = open(arquivo, "r")

for linha in arq:
    if linha.find("Grupo = ") == 0:
        Grupo = ET.SubElement(root, "Grupo")
        Grupo.set("name", linha[len("Grupo = "):])   
    if linha.find("href = ") == 0:
        site = ET.SubElement(Grupo, "site")
        ET.SubElement(site, "field1", name = "href").text = linha[len("href = "):]
    if linha.find("descricao = ") == 0:
        ET.SubElement(site, "field2", name = "descricao").text = linha[len("descricao = "):]

tree = ET.ElementTree(root)
tree.write("teste.xml")

arq.close()





