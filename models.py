from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Optional, List
from enum import Enum

class Role(str, Enum):
    role_1 = 'admin'
    role_2 = 'aluna'
    role_3 = 'instrutora'

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    email: str
    role: List[Role]