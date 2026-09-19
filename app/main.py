from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.gerar_dps import gerar_dps


app = FastAPI()


class DPS(BaseModel):
    cpf_cnpj: str
    data_competencia: str

    tipo_servico: Literal[
        "certidao",
        "retificacao",
        "averbacao",
        "casamento"
    ]

    valor_servico: float = Field(gt=0)
    descricao_servico: str


@app.get("/")
def inicio():
    return {
        "sistema": "MeuCartório NFS-e",
        "status": "online"
    }


@app.post("/dps")
def criar_dps(dps: DPS):

    arquivo = gerar_dps(dps)

    return {
        "mensagem": "DPS gerada com sucesso!",
        "arquivo": str(arquivo),
        "dados": dps
    }