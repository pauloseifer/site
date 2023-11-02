#! /usr/bin/env python3
# _*_ coding: UTF-8 _*_

## O arquivo que vai ser gravado tem que ter permissão de escrita para quem é de outros grupos
## quem executa é o Apache, então é outro grupo.
## Usar chmod 757


import cgi
import json

dados = cgi.FieldStorage()

print("Content-type: text/html\n\n")

caminho = "../htdocs/bookmark.json"

arqBM = open(caminho)
BM = json.load(arqBM)
arqBM.close()


opcao = dados["funcao"].value

if opcao == "bookmark":

    corpo = ""

    lista = []
    idgrupo = []
    
    filhos = list(BM)
    for i in range(3, len(filhos)):
        corpo = corpo + "<h2 tipo=\"Grupo\" grupo=\"" + filhos[i] + "\">" + BM[filhos[i]]["Grupo"] + "</h2>\n"

        lista.append(BM[filhos[i]]["Grupo"])
        idgrupo.append(filhos[i])

        netos = list(BM[filhos[i]])
        for j in range(1, len(netos)):
            site = BM[filhos[i]][netos[j]]["site"]
            descricao = BM[filhos[i]][netos[j]]["descrição"]
            corpo = corpo + "<a href=" + site + ">" + descricao + "</a><br>\n"

    lista.append("Nova categoria")
    idgrupo.append("GRX")
            
    print(corpo)

## https://blog.betrybe.com/html/checkbox-html/

elif opcao == "Sel_Excluir":

    corpo = "<form id=\"Sel_Excluir\" method=\"POST\" action=\"Javascript:excluir()\"><br><br><h2>Selecione as entradas que devem ser excluídas</h2>"
    filhos = list(BM)
    for i in range(3, len(filhos)):
        corpo = corpo + "<h2><input type=\"checkbox\" id="+ filhos[i] +">" + BM[filhos[i]]["Grupo"] + "</h2>\n"

        netos = list(BM[filhos[i]])
        for j in range(1, len(netos)):
            site = BM[filhos[i]][netos[j]]["site"]
            descricao = BM[filhos[i]][netos[j]]["descrição"]
            corpo = corpo + "<input type=\"checkbox\" id="+ netos[j] +"><a href=" + site + ">" + descricao + "</a><br>\n"
    corpo = corpo + "<input type=\"submit\" value=\"Excluir\"></form>"
    print(corpo)

elif opcao == "excluir":

    lista = dados["selecao"].value
    lista = lista[:len(lista)-1]
    selecionados = lista.split(";")

    for selecionado in selecionados:
        partes = selecionado.split("_")
        if len(partes) == 2:
            try:
                BM.pop(selecionado)
            except:
                pass
        else:
            if len(partes) == 3:
                try:
                    grupo = selecionado.split("_")[0] + "_" + selecionado.split("_")[1]
                    BM[grupo].pop(selecionado)
                except:
                    pass
    arqBM = open(caminho, "w")
    json.dump(BM, arqBM, ensure_ascii=False, indent=3)
    arqBM.close()
                

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
            filhos = list(BM)
            ultimo = filhos[len(filhos)-1]
            novo_indice = int(ultimo.split("_")[1])+1
            novo_grupo = "GR_"+str(novo_indice)
            BM[novo_grupo] = {}
            BM[novo_grupo]["Grupo"]= S_NovoNome
            BM[novo_grupo][novo_grupo+"_1"] = {}
            BM[novo_grupo][novo_grupo+"_1"]["site"]= S_site
            BM[novo_grupo][novo_grupo+"_1"]["descrição"]= S_descricao
        else:
            netos = list(BM[S_Grupo])
            ultimo = netos[len(netos)-1]
            novo_indice = int(ultimo.split("_")[2])+1
            novo_subgrupo = S_Grupo+"_"+str(novo_indice)
            BM[S_Grupo][novo_subgrupo] = {}
            BM[S_Grupo][novo_subgrupo]["site"] = S_site
            BM[S_Grupo][novo_subgrupo]["descrição"] = S_descricao

        arqBM = open(caminho, "w")
        json.dump(BM, arqBM, ensure_ascii=False, indent=3)
        arqBM.close()
        
    print(StatusAtualizacao)

else:
    print("Não pegou nenhuma!")


