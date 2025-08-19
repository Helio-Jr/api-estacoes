from fastapi import APIRouter, Depends, HTTPException
from dependencies.dependencies import iniciar_sessao, verificar_token   
from sqlalchemy.orm import Session
from models.models import Usuario, Estacao

station_router = APIRouter(prefix="/station", tags=["station"], dependencies=[Depends(verificar_token)])

@station_router.get("/")
async def estacao():
    return {"mensagem": "Você está na rota de solicitações do aplicativo."}

@station_router.get("/listar")
async def listar_estacoes(session: Session = Depends(iniciar_sessao), usuario: Usuario = Depends(verificar_token)):
    if not usuario.admin:
        raise HTTPException(status_code=401, detail="Você não tem autorização para listar as estações.")
    else:
        pedidos = session.query(Estacao).all()
    return pedidos

@station_router.get("/{id_estacao}")
async def visualizar_estacao(id_estacao: int, session: Session = Depends(iniciar_sessao)):
    pedido = session.query(Estacao).filter(Estacao.id == id_estacao).first()
    if not pedido:
        raise HTTPException(status_code=400, detail="Estação não encontrada.")
    
    return {
        pedido
    }
