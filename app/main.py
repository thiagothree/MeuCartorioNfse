from typing import Literal
from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI()


class DPS(BaseModel):
    cpf_cnpj: str
    data_competencia: str
    tipo_servico: Literal[
        "certidao",
        "retificao",
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
    return {
        "mensagem": "DPS recebida com sucesso!",
        "dados": dps
    }