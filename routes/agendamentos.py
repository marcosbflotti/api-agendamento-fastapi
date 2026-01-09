from fastapi import APIRouter   
from models.agendamento import AgendamentoCreate, AgendamentoResponse
from services.agendamento_service import(   
    criar_agendamento,  
    listar_agendamentos,    
    buscar_agendamento_por_id,  
    marcar_como_realizado   
)   
from typing import List 

router = APIRouter(
    prefix="/agendamentos",
    tags=["Agendamentos"]
)   

@router.post("/", response_model=AgendamentoResponse)
def criar(dados: AgendamentoCreate):
    return criar_agendamento(dados.model_dump())   

@router.get("/", response_model=List[AgendamentoResponse])  
def listar():   
    return listar_agendamentos()    
        
@router.get("/{agendamento_id}", response_model=AgendamentoResponse)
def buscar(agendamento_id: int):
    return buscar_agendamento_por_id(agendamento_id)

@router.put("/{agendamento_id}/realizar", response_model=AgendamentoResponse)
def realizar(agendamento_id: int):
    return marcar_como_realizado(agendamento_id)