from lxml import etree

arquivo = "schemas/nfse/1.01/DPS_v1.01.xsd"

tree = etree.parse(arquivo)
root = tree.getroot()

print("Arquivo:", arquivo)
print("Elemento raiz:", root.tag)

print("\nAtributos:")
for nome, valor in root.attrib.items():
    print(f"{nome} = {valor}")