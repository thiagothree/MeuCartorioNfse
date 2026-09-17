from pathlib import Path
from lxml import etree
import shutil
import tempfile


BASE_DIR = Path(__file__).resolve().parent.parent

XSD_DIR = BASE_DIR / "schemas" / "nfse" / "1.01"
ARQUIVO_XSD = XSD_DIR / "DPS_v1.01.xsd"
ARQUIVO_XML = BASE_DIR / "xml" / "DPS_teste.xml"


print("Preparando validação...")
print()


with tempfile.TemporaryDirectory() as temp_dir:

    temp_dir = Path(temp_dir)

    # Copia todos os XSDs para uma pasta temporária
    pasta_temp = temp_dir / "1.01"

    shutil.copytree(XSD_DIR, pasta_temp)

    # Corrige somente os padrões incompatíveis do validador local.
    # NÃO altera os XSDs oficiais do projeto.
    for arquivo in pasta_temp.glob("*.xsd"):

        texto = arquivo.read_text(encoding="utf-8")

        texto_corrigido = texto.replace(r"\d", "[0-9]")
        texto_corrigido = texto_corrigido.replace(
        'value="^0{0,4}[0-9]{1,5}$"',
        'value="0{0,4}[0-9]{1,5}"'
        )

        if texto != texto_corrigido:
            arquivo.write_text(
                texto_corrigido,
                encoding="utf-8"
            )

    # XSD corrigido temporariamente
    xsd_temp = pasta_temp / "DPS_v1.01.xsd"

    print("XSD temporário:")
    print(xsd_temp)

    print()
    print("XML:")
    print(ARQUIVO_XML)

    # Carrega o XSD temporário
    schema_doc = etree.parse(str(xsd_temp))

    schema = etree.XMLSchema(schema_doc)

    # Carrega nossa DPS
    xml_doc = etree.parse(str(ARQUIVO_XML))

    print()
    print("Validando...")
    print()

    if schema.validate(xml_doc):

        print("=" * 60)
        print("✅ XML VÁLIDO!")
        print("=" * 60)

    else:

        print("=" * 60)
        print("❌ XML INVÁLIDO")
        print("=" * 60)
        print()

        for erro in schema.error_log:
            print(
                f"Linha {erro.line}: {erro.message}"
            )