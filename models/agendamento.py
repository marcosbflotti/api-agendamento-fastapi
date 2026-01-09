from pydantic import BaseModel, EmailStr
from typing import Optional


class AgendamentoCreate(BaseModel):
    nome: str
    email: EmailStr
    data: str
    hora: str
    servico: str    
    valor: float

class AgendamentoResponse(AgendamentoCreate):
    id: int
    status: str 
    observacao: Optional[str] = None