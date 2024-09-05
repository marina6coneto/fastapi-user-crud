from fastapi import FastAPI, HTTPException
from typing import List
from uuid import UUID
from models import User, Role

app = FastAPI()

# Simulação de um banco de dados em memória com alguns usuários
db: List[User] = [
    User(
         id=UUID("e812c926-642b-499d-b2fd-c941f20fb8f6"),
         first_name='Ana',
         last_name='Maria',
         email='ana.maria@gmail.com',
         role=[Role.role_1]
    ),
    User(
         id=UUID('1a003712-99a8-4b96-96c4-3fd2a11937ff'),
         first_name='Marina',
         last_name='Cesconeto',
         email='marina.cesconeto@gmail.com',
         role=[Role.role_2]
    ),
    User(
         id=UUID('9ac49a42-f3a8-4c03-a026-2defec3c45bf'),
         first_name='Hermione',
         last_name='Granger',
         email='hermione.granger@hogwarts.com',
         role=[Role.role_3]
    ),
]

# Rota raiz para uma mensagem simples de boas-vindas
@app.get('/')
async def root():
    return {"message": "Olá, WoMakers!"} 

# Rota GET para buscar todos os usuários
@app.get('/api/users', response_model=List[User])
async def get_users():
    return db

# Rota GET para buscar um usuário específico pelo UUID
@app.get('/api/users/{id}', response_model=User)
async def get_user(id: UUID):
    for user in db:
        if user.id == id:
            return user
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

# Rota POST para adicionar um novo usuário à base de dados
@app.post('/api/users', response_model=User)
async def add_user(user: User):
    '''
    Adiciona um usuário na base de dados:
    - **id**: UUID gerado automaticamente
    - **first_name**: Nome do usuário
    - **last_name**: Sobrenome do usuário
    - **email**: Email do usuário
    - **role**: Lista de funções do usuário (admin, aluna, instrutora)
    '''
    db.append(user)
    return user

# Rota DELETE para remover um usuário da base de dados pelo UUID
@app.delete('/api/users/{id}')
async def remove_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return {"message": f"Usuário com o id {id} removido com sucesso!"}
    
    raise HTTPException(
        status_code=404,
        detail=f"Usuário com o id {id} não encontrado!"
    )

# Rota PUT para atualizar os dados de um usuário existente
@app.put('/api/users/{id}', response_model=User)
async def update_user(id: UUID, updated_user: User):
    '''
    Atualiza as informações de um usuário existente na base de dados:
    - **id**: UUID
    - **first_name**: string
    - **last_name**: string
    - **email**: string
    - **role**: Role
    '''
    for index, user in enumerate(db):
        if user.id == id:
            # Atualiza o usuário na base de dados
            db[index] = updated_user
            return updated_user

    raise HTTPException(
        status_code=404,
        detail=f"Usuário com o id {id} não encontrado!"
    )
