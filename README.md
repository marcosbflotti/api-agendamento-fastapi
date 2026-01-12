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

---

## Como executar o projeto

```bash
python -m venv venv
source venv/bin/activate  venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
