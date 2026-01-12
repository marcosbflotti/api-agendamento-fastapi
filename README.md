# API de Agendamentos – FastAPI

API REST desenvolvida em Python utilizando **FastAPI**, com foco no gerenciamento de agendamentos
para profissionais da área de beleza (micropigmentação, design de sobrancelhas, estética em geral).

Projeto criado com objetivo de **estudo prático de backend**, organização em camadas
e exposição em portfólio.

---

## Funcionalidades

- Criar agendamentos
- Listar todos os agendamentos
- Buscar agendamento por ID
- Atualizar dados do agendamento
- Marcar agendamento como realizado
- Cancelar agendamento
- Controle de status (`pendente`, `realizado`, `cancelado`)
- Campo opcional de observações

---

## Regras de negócio

- Um agendamento cancelado não pode ser marcado como realizado
- Agendamentos realizados podem receber observações e ajustes de valor
- IDs são gerados automaticamente
- Persistência simulada em memória (fake database)

---

##  Tecnologias utilizadas

- Python 3
- FastAPI
- Pydantic
- Uvicorn
- Git e GitHub

---

##  Estrutura do projeto

```text
api_agendamento/
│
├── main.py
├── routes/
│   └── agendamentos.py
├── services/
│   └── agendamento_service.py
├── models/
│   └── agendamento.py
├── database/
│   └── fake_db.py
├── requirements.txt
└── README.md
```
---

##  Como executar o projeto
 
```bash
git clone https://github.com/marcosbflotti/api-agendamento-fastapi.git  
cd api-agendamento-fastapi      
```
---

##   Crie e ative o ambiete virtual

```bash
python -m venv venv 
venv/Scripts/activate *windows*
```
---

*instale as dependências* 
```bash    
pip install -r requirements.txt
```
---

*Execute a aplicação*
```bash 
uvicorn main:app --reload
```

--- 

##  Objetivo do projeto

```text
Este projeto faz parte do meu processo de aprendizagem e consolidação na área de Backend Developer,
com foco em boas práticas, organização de código e entendimento de regras de negócio.
```

---

##  Autor

```text
Marcos Brasil F.Lotti
Estudante de Backend | Python | FastAPI
GitHub: https://github.com/marcosbflotti    
``` 
---