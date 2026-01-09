from fastapi import FastAPI    
from routes.agendamentos import router as agendamentos_router    

app = FastAPI(  
    title="API de Agendamentos",    
    version="1.0.0" 
)

app.include_router(agendamentos_router)    