from database.fake_db import agendamentos_db    
from fastapi import HTTPException   

def criar_agendamento(dados: dict): 
    novo_id = len(agendamentos_db) + 1  

    novo_agendamento = {    
        "id": novo_id,  
        "status": "pendente",   
        **dados 
    }   

    agendamentos_db.append(novo_agendamento)    
    return novo_agendamento     

def listar_agendamentos():  
        return agendamentos_db

def buscar_agendamento_por_id(agendamento_id: int): 
    for agendamento in agendamentos_db: 
        if agendamento["id"] == agendamento_id: 
            return agendamento  

    raise HTTPException(    
        status_code=404,    
        detail="Agendamento não encontrado" 
    )   

def marcar_como_realizado(agendamento_id: int): 
    agendamento = buscar_agendamento_por_id(agendamento_id_ )   

    if agendamento["status"] == "cancelado":    
        raise HTTPException(    
            status_code=400,    
            detail="Agendamento cancelado não pode ser realizado"   
        )       

    agendamento["status"] = "realizado" 
    return agendamento             