from sqlalchemy import create_engine, Column, String, Integer, Float, Date, Boolean
from sqlalchemy.orm import declarative_base
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

# Dados de conexão
usuario = os.getenv("USUARIO_DB")
senha = os.getenv("SENHA_DB")
host = "localhost"
porta = "5432"
banco = "postgres"

# String de conexão
DATABASE_URL = f"postgresql://{usuario}:{senha}@{host}:{porta}/{banco}"

# Criando a engine
db = create_engine(DATABASE_URL)

#criando base do banco de dados
Base = declarative_base()

class Estacao(Base):
    __tablename__ = "estacoes"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    cd_oscar = Column("cd_oscar", String)
    dc_nome = Column("dc_nome", String)
    fl_capital = Column("fl_capital", String)
    cd_situacao = Column("cd_situacao", String)
    tp_estacao = Column("tp_estacao", String)
    cd_wsi = Column("cd_wsi", String)
    cd_distrito = Column("cd_distrito", String)
    sg_estado = Column("sg_estado", String)
    sg_entidade = Column("sg_entidade", String)
    cd_estacao = Column("cd_estacao", String)
    vl_latitude = Column("vl_latitude", Float)
    vl_longitude = Column("vl_longitude", Float)
    vl_altitude = Column("vl_altitude", Float)
    dt_inicio_operacao = Column("dt_inicio_operacao", Date)
    dt_fim_operacao = Column("dt_fim_operacao", Date)
    dt_registro = Column("dt_registro", Date)

    def __init__(
    self,
    cd_oscar,
    dc_nome,
    fl_capital,
    cd_situacao,
    tp_estacao,
    cd_wsi,
    cd_distrito,
    sg_estado,
    sg_entidade,
    cd_estacao,
    vl_latitude,
    vl_longitude,
    vl_altitude,
    dt_inicio_operacao,
    dt_fim_operacao,
    dt_registro=datetime.now()
):
        self.cd_oscar = cd_oscar
        self.dc_nome = dc_nome
        self.fl_capital = fl_capital
        self.cd_situacao = cd_situacao
        self.tp_estacao = tp_estacao
        self.cd_wsi = cd_wsi
        self.cd_distrito = cd_distrito
        self.sg_estado = sg_estado
        self.sg_entidade = sg_entidade
        self.cd_estacao = cd_estacao
        self.vl_latitude = vl_latitude
        self.vl_longitude = vl_longitude
        self.vl_altitude = vl_altitude
        self.dt_inicio_operacao = dt_inicio_operacao
        self.dt_fim_operacao = dt_fim_operacao
        self.dt_registro = dt_registro

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String, nullable=False)
    senha = Column("senha", String, nullable=False)
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean, default=False)

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

# CREATE TABLE estacoes (
#     id SERIAL PRIMARY KEY,
#     cd_oscar VARCHAR,
#     dc_nome VARCHAR,
#     fl_capital VARCHAR,
#     cd_situacao VARCHAR,
#     tp_estacao VARCHAR,
#     cd_wsi VARCHAR,
#     cd_distrito VARCHAR,
#     sg_estado VARCHAR,
#     sg_entidade VARCHAR,
#     cd_estacao VARCHAR,
#     vl_latitude FLOAT,
#     vl_longitude FLOAT,
#     vl_altitude FLOAT,
#     dt_inicio_operacao DATE,
#     dt_fim_operacao DATE,
#     dt_registro DATE
# );

# CREATE TABLE usuarios (
#     id SERIAL PRIMARY KEY,
#     nome VARCHAR,
#     email VARCHAR NOT NULL,
#     senha VARCHAR NOT NULL,
#     ativo BOOLEAN,
#     admin BOOLEAN DEFAULT FALSE
# );
