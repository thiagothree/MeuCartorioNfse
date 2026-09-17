from pathlib import Path
from lxml import etree


# =========================
# CONFIGURAÇÕES
# =========================

NS_NFSE = "http://www.sped.fazenda.gov.br/nfse"

BASE_DIR = Path(__file__).resolve().parent.parent
PASTA_XML = BASE_DIR / "xml"

PASTA_XML.mkdir(exist_ok=True)


# =========================
# DADOS DO CARTÓRIO
# =========================

CNPJ_PRESTADOR = "10538764000199"
CEP_PRESTADOR = "56903400"

CODIGO_MUNICIPIO = "2613903"

OP_SIMP_NAC = "1"       # Não optante
REG_ESP_TRIB = "4"      # Notário ou Registrador

CODIGO_TRIBUTACAO = "210101"
NBS = "113040000"


# =========================
# DADOS DA DPS
# =========================

CPF_CNPJ_TOMADOR = "12312312312"

DATA_COMPETENCIA = "2026-09-15"

VALOR_SERVICO = "55.62"

DESCRICAO_SERVICO = "Certidão em inteiro teor"


# =========================
# CRIA XML
# =========================

def criar_dps():

    # Elemento raiz DPS
    dps = etree.Element(
        f"{{{NS_NFSE}}}DPS",
        nsmap={None: NS_NFSE}
    )

    dps.set("versao", "1.01")

    # Informações da DPS
    inf_dps = etree.SubElement(
        dps,
        f"{{{NS_NFSE}}}infDPS"
    )

    inf_dps.set(
    "Id",
    "DPS261390310538764000199000000000000000000001"
)

    # Ambiente
    etree.SubElement(
        inf_dps,
        f"{{{NS_NFSE}}}tpAmb"
    ).text = "2"

    # Data/hora da emissão
    etree.SubElement(
        inf_dps,
        f"{{{NS_NFSE}}}dhEmi"
    ).text = "2026-09-15T20:00:00-03:00"

    # Versão da aplicação
    etree.SubElement(
        inf_dps,
        f"{{{NS_NFSE}}}verAplic"
    ).text = "MeuCartorio-0.1"

    # Série
    etree.SubElement(
    inf_dps,
    f"{{{NS_NFSE}}}serie"
    ).text = "1"

    # Número da DPS
    etree.SubElement(
        inf_dps,
        f"{{{NS_NFSE}}}nDPS"
    ).text = "1"

    # Competência
    etree.SubElement(
        inf_dps,
        f"{{{NS_NFSE}}}dCompet"
    ).text = DATA_COMPETENCIA

    # Emitente
    etree.SubElement(
        inf_dps,
        f"{{{NS_NFSE}}}tpEmit"
    ).text = "1"

    # Município de emissão
    etree.SubElement(
        inf_dps,
        f"{{{NS_NFSE}}}cLocEmi"
    ).text = CODIGO_MUNICIPIO


    # =========================
    # PRESTADOR
    # =========================

    prest = etree.SubElement(
        inf_dps,
        f"{{{NS_NFSE}}}prest"
    )

    etree.SubElement(
        prest,
        f"{{{NS_NFSE}}}CNPJ"
    ).text = CNPJ_PRESTADOR


    # =========================
    # TOMADOR
    # =========================

    toma = etree.SubElement(
        inf_dps,
        f"{{{NS_NFSE}}}toma"
    )

    etree.SubElement(
        toma,
        f"{{{NS_NFSE}}}CPF"
    ).text = CPF_CNPJ_TOMADOR


    # =========================
    # SERVIÇO
    # =========================

    serv = etree.SubElement(
        inf_dps,
        f"{{{NS_NFSE}}}serv"
    )

    # Local da prestação
    loc_prest = etree.SubElement(
        serv,
        f"{{{NS_NFSE}}}locPrest"
    )

    etree.SubElement(
        loc_prest,
        f"{{{NS_NFSE}}}cLocPrestacao"
    ).text = CODIGO_MUNICIPIO

    etree.SubElement(
        loc_prest,
        f"{{{NS_NFSE}}}cPaisPrestacao"
    ).text = "BR"


    # Serviço
    c_serv = etree.SubElement(
        serv,
        f"{{{NS_NFSE}}}cServ"
    )

    etree.SubElement(
        c_serv,
        f"{{{NS_NFSE}}}cTribNac"
    ).text = CODIGO_TRIBUTACAO

    etree.SubElement(
        c_serv,
        f"{{{NS_NFSE}}}xDescServ"
    ).text = DESCRICAO_SERVICO

    etree.SubElement(
        c_serv,
        f"{{{NS_NFSE}}}cNBS"
    ).text = NBS


    # =========================
    # VALORES
    # =========================

    valores = etree.SubElement(
        inf_dps,
        f"{{{NS_NFSE}}}valores"
    )

    v_serv_prest = etree.SubElement(
        valores,
        f"{{{NS_NFSE}}}vServPrest"
    )

    etree.SubElement(
        v_serv_prest,
        f"{{{NS_NFSE}}}vServ"
    ).text = VALOR_SERVICO


    # =========================
    # SALVAR
    # =========================

    caminho = PASTA_XML / "DPS_teste.xml"

    arvore = etree.ElementTree(dps)

    arvore.write(
        str(caminho),
        encoding="UTF-8",
        xml_declaration=True,
        pretty_print=True
    )

    print()
    print("=" * 60)
    print("DPS GERADA!")
    print("=" * 60)
    print(f"Arquivo: {caminho}")
    print()


if __name__ == "__main__":
    criar_dps()