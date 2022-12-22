#! /usr/bin/env python3
# _*_ coding: UTF-8 _*_

## O arquivo que vai ser gravado tem que ter permissão de escrita para quem é de outros grupos
## quem executa é o Apache, então é outro grupo.
## Usar chmod 757


import xml.etree.cElementTree as ET
import cgi

dados = cgi.FieldStorage()

print("Content-type: text/html\n\n")

tree = ET.parse("../htdocs/bookmark.xml")
root = tree.getroot()

opcao = dados["funcao"].value

if opcao == "Sel_Excluir":

    corpo = "<form id=\"Sel_Excluir\" method=\"POST\" action=\"Javascript:excluir()\"><br><br><h2>Selecione as entradas que devem ser excluídas</h2>"

    for child in root:
        corpo = corpo + "<h2><input type=\"checkbox\" id="+ child.attrib["id"] +">" + child.get("name") + "</h2>\n"
        
        for child2 in child:
            site = child2.find("field1").text
            descricao = child2.find("field2").text
            corpo = corpo + "<input type=\"checkbox\" id="+ child2.attrib["id"] +"><a href=" + site + ">" + descricao + "</a><br>\n"
    corpo = corpo + "<input type=\"submit\" value=\"Excluir\"></form>"
    print(corpo)

elif opcao == "bookmark":

    corpo = ""
    for child in root:
        corpo = corpo + "<h2>" + child.get("name") + "</h2>\n"
        
        for child2 in child:
            site = child2.find("field1").text
            descricao = child2.find("field2").text
            corpo = corpo + "<a href=" + site + ">" + descricao + "</a><br>\n"
    
    print(corpo)

## https://blog.betrybe.com/html/checkbox-html/

elif opcao == "excluir":

    lista = dados["selecao"].value
    lista = lista[:len(lista)-1]
    selecionados = lista.split(";")

    for selecionado in selecionados:
        partes = selecionado.split("_")
        if len(partes) == 1:
            try:
                caminho = ".//*[@id=\"" + selecionado + "\"]"
                elemento = root.find(caminho)
                root.remove(elemento)
            except:
                pass
        else:
            if len(partes) == 2:
                try:
                    caminho = ".//*[@id=\"" + selecionado + "\"]"
                    caminho_pai = ".//*[@id=\"" + selecionado.split("_")[0] +"\"]"
                    elemento = root.find(caminho)
                    elemento_pai = root.find(caminho_pai)
                    elemento_pai.remove(elemento)
                except:
                    pass
    tree = ET.ElementTree(root)
    tree.write("../htdocs/bookmark.xml", encoding="utf-8")
                
        
elif opcao == "atualizar":
    StatusAtualizacao = ""
    try:
        S_site=dados["site"].value
        S_descricao=dados["descricao"].value
        S_Grupo=dados["Grupo"].value
    except:
        StatusAtualizacao = "Verifique os campos..."
    else:
        try:
            S_NovoNome=dados["NovoNome"].value
        except:
            S_NovoNome=""
    
    
        if S_Grupo=="GRX":
            Grupo=ET.SubElement(root, "Grupo")
            Grupo.set("name", S_NovoNome)
            Grupo.set("id", "GR" + str(len(root)))
            site=ET.SubElement(Grupo, "site")
            site.set("id", Grupo.attrib["id"] + "_" +  str(len(Grupo)))
            ET.SubElement(site, "field1", name = "href").text = S_site
            ET.SubElement(site, "field2", name = "descricao").text = S_descricao
            ##StatusAtualizacao = "Atualizado!"
        else:
            for filho in root:
                if filho.attrib["id"] == S_Grupo:
                    site = ET.SubElement(filho, "site")
                    site.set("id", filho.attrib["id"] + "_" +  str(len(filho)))
                    ET.SubElement(site, "field1", name = "href").text = S_site
                    ET.SubElement(site, "field2", name = "descricao").text = S_descricao
                    ##StatusAtualizacao = "Atualizado!"
    
                
        tree = ET.ElementTree(root)
        tree.write("../htdocs/bookmark.xml", encoding="utf-8")
                   
    print(StatusAtualizacao)

else:
    print("Não pegou nenhuma!")
      




