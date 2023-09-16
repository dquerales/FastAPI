from pydantic import BaseModel


class ClientBase(BaseModel):
    name: str
    email: str
    phone: str


class ClientCreate(ClientBase):
    pass


class Client(ClientBase):
    id: int

    class Config:
        orm_mode = True
