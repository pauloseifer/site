import xml.etree.cElementTree as ET



root = ET.Element("Bookmark")


doc = ET.SubElement(root, "doc")
doc.set("name", "Hum")
dec = ET.SubElement(doc, "dec")
ET.SubElement(dec, "field1", name="href").text = "http://oi"
ET.SubElement(dec, "field2", name="descricao").text = "nada"

doc = ET.SubElement(root, "doc")
doc.set("name", "Dois")
dec = ET.SubElement(doc, "dec")
ET.SubElement(dec, "field1", name="href").text = "http://oi2"
ET.SubElement(dec, "field2", name="descricao").text = "nada2"
ET.SubElement(dec, "field1", name="href").text = "http://oi2"
ET.SubElement(dec, "field2", name="descricao").text = "nada2"

tree = ET.ElementTree(root)
tree.write("teste.xml")




