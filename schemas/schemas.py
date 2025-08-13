from pydantic import BaseModel
from typing import Optional, List

class EstacaoSchema(BaseModel):
    cd_oscar: str
    dc_nome: str 
    fl_capital: str 
    cd_situacao: str
    tp_estacao: str
    cd_wsi: str
    cd_distrito: str
    sg_estado: str
    sg_entidade: str
    cd_estacao: str
    vl_latitude: float
    vl_longitude: float
    vl_altitude: float
    dt_inicio_operacao: str
    dt_fim_operacao: str

    class Config:
        from_atributes = True

class UsuarioSchema(BaseModel):
    nome: str
    email: str 
    senha: str 
    ativo: Optional[bool]
    admin: Optional[bool]

    class Config:
        from_atributes = True

class LoginSchema(BaseModel):
    email: str
    senha: str

    class Config:
        from_atributes = True