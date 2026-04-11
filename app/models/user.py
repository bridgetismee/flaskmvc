from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
from pydantic import EmailStr

class UserBase(SQLModel):
    username: str = Field(index=True, unique=True)
    email: EmailStr = Field(index=True, unique=True)
    password: str
    role: str = ""

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    todos: list['Todo'] = Relationship(back_populates="user")

class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    text: str
    done: bool = False
    user_id: int = Field(foreign_key="user.id")
    user: User = Relationship(back_populates="todos")