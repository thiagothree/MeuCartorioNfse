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

def gerar_dps(dps):

    # Elemento raiz DPS
    dps_xml = etree.Element(
        f"{{{NS_NFSE}}}DPS",
        nsmap={None: NS_NFSE}
    )

    dps_xml.set("versao", "1.01")

    # Informações da DPS
    inf_dps = etree.SubElement(
        dps_xml,
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
    ).text = dps.data_competencia

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

    # CNPJ do prestador
    etree.SubElement(
        prest,
        f"{{{NS_NFSE}}}CNPJ"
    ).text = CNPJ_PRESTADOR

    # Regime tributário
    reg_trib = etree.SubElement(
        prest,
        f"{{{NS_NFSE}}}regTrib"
    )

    # Não optante pelo Simples Nacional
    etree.SubElement(
        reg_trib,
        f"{{{NS_NFSE}}}opSimpNac"
    ).text = OP_SIMP_NAC

    # Nenhum regime de apuração do Simples,
    # pois o cartório não é optante
    #
    # regApTribSN não será informado.

    # Regime especial: Notário ou Registrador
    etree.SubElement(
        reg_trib,
        f"{{{NS_NFSE}}}regEspTrib"
    ).text = REG_ESP_TRIB


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
    ).text = dps.cpf_cnpj

    etree.SubElement(
        toma,
        f"{{{NS_NFSE}}}xNome"
    ).text = "Tomador Teste"


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
    ).text = dps.descricao_servico

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
    ).text = f"{dps.valor_servico:.2f}"

    trib = etree.SubElement(
        valores,
        f"{{{NS_NFSE}}}trib"
    )

    trib_mun = etree.SubElement(
        trib,
        f"{{{NS_NFSE}}}tribMun"
    )

    etree.SubElement(
        trib_mun,
        f"{{{NS_NFSE}}}tribISSQN"
    ).text = "1"

    etree.SubElement(
        trib_mun,
        f"{{{NS_NFSE}}}tpRetISSQN"
    ).text = "2"

    tot_trib = etree.SubElement(
        trib,
        f"{{{NS_NFSE}}}totTrib"
    )

    etree.SubElement(
        tot_trib,
        f"{{{NS_NFSE}}}indTotTrib"
    ).text = "0"


    # =========================
    # SALVAR
    # =========================

    caminho = PASTA_XML / "DPS_teste.xml"

    arvore = etree.ElementTree(dps_xml)

    arvore.write(
        str(caminho),
        encoding="UTF-8",
        xml_declaration=True,
        pretty_print=True
    )

    return caminho

    print()
    print("=" * 60)
    print("DPS GERADA!")
    print("=" * 60)
    print(f"Arquivo: {caminho}")
    print()


